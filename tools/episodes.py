"""Keep the Gradient - Episode Manifests

An episode is a folder ``episodes/epNN_<slug>/`` holding:

- ``episode.toml``    metadata and the TIMELINE: scenes and clips in playback
                      order. Recutting an episode means editing this list,
                      never copying scene folders.
- ``narration.toml``  narration segments, each pinned to a timeline entry with
                      a start time RELATIVE to that entry, so changing one
                      scene's length never shifts another scene's lines.
- ``scenes/``         one manim scene per file.
- ``assets/``         footage and figures used by this episode only.

This module loads and validates both files; it has no third-party imports so
``kg check`` runs anywhere.
"""
from __future__ import annotations

import ast
import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"
STATUSES = ("planned", "scripting", "animating", "narrating", "review", "published")
TTS_ENGINES = ("piper", "kokoro", "takes")


@dataclass
class Entry:
    """One timeline item: a manim scene (file + class) or a finished clip."""

    kind: str                 # "scene" or "clip"
    file: str                 # scene file under scenes/, or clip path under the episode
    scene_class: str = ""     # manim class name, scenes only

    @property
    def key(self) -> str:
        """Name narration segments use to refer to this entry."""
        return self.scene_class if self.kind == "scene" else self.file


@dataclass
class Segment:
    """One narration utterance."""

    id: str
    entry: str
    at: float
    budget: float
    text: str


@dataclass
class Episode:
    """A loaded episode folder."""

    path: Path
    number: int
    slug: str
    title: str
    status: str
    meta: dict
    timeline: list[Entry]
    voice: dict = field(default_factory=dict)
    segments: list[Segment] = field(default_factory=list)

    @property
    def code(self) -> str:
        """Short identifier, e.g. ep01."""
        return f"ep{self.number:02d}"


def find(ref: str | int) -> Path:
    """Locate an episode folder from 1, "01", "ep01" or the folder name.

        Parameters
        ----------
        ref : str or int
            Episode reference.

        Returns
        -------
        pathlib.Path
            The episode folder.
    """
    s = str(ref).strip().lower().removeprefix("episodes/").rstrip("/")
    m = re.fullmatch(r"(?:ep)?(\d{1,2})(?:_.*)?", s)
    if not m:
        raise SystemExit(f"cannot read episode reference {ref!r}; use e.g. 1, 01 or ep01")
    hits = sorted(EPISODES.glob(f"ep{int(m.group(1)):02d}_*"))
    if not hits:
        raise SystemExit(f"no episode folder for {ref!r} under {EPISODES}")
    return hits[0]


def all_paths() -> list[Path]:
    """Every episode folder, in order."""
    return sorted(p for p in EPISODES.glob("ep[0-9][0-9]_*") if p.is_dir())


def load(path: Path) -> Episode:
    """Read episode.toml and narration.toml of one episode.

        Parameters
        ----------
        path : pathlib.Path
            Episode folder.

        Returns
        -------
        Episode
            The parsed episode (not yet validated; see ``validate``).
    """
    data = tomllib.loads((path / "episode.toml").read_text())
    ep = data.get("episode", {})
    timeline = []
    for item in data.get("timeline", []):
        if "scene" in item:
            file, _, cls = item["scene"].partition(":")
            timeline.append(Entry("scene", file, cls))
        elif "clip" in item:
            timeline.append(Entry("clip", item["clip"]))
        else:
            timeline.append(Entry("invalid", repr(item)))
    narr_path = path / "narration.toml"
    narr = tomllib.loads(narr_path.read_text()) if narr_path.exists() else {}
    segments = [Segment(id=str(s.get("id", "")), entry=str(s.get("entry", "")),
                        at=float(s.get("at", -1)), budget=float(s.get("budget", 0)),
                        text=str(s.get("text", "")).strip())
                for s in narr.get("segment", [])]
    return Episode(path=path, number=int(ep.get("number", -1)), slug=str(ep.get("slug", "")),
                   title=str(ep.get("title", "")), status=str(ep.get("status", "")), meta=ep,
                   timeline=timeline, voice=narr.get("voice", {}), segments=segments)


def scene_classes(file: Path) -> set[str]:
    """Class names defined at top level of a scene file (parsed, not imported)."""
    tree = ast.parse(file.read_text(), filename=str(file))
    return {n.name for n in tree.body if isinstance(n, ast.ClassDef)}


def is_placeholder(file: Path) -> bool:
    """True while a scene still derives from PlaceholderScene."""
    tree = ast.parse(file.read_text(), filename=str(file))
    return any(isinstance(n, ast.ClassDef) and any(
        getattr(b, "id", getattr(b, "attr", "")) == "PlaceholderScene" for b in n.bases)
        for n in tree.body)


def validate(ep: Episode) -> list[str]:
    """Return every problem found in an episode; an empty list means valid.

        Parameters
        ----------
        ep : Episode
            A loaded episode.

        Returns
        -------
        list of str
            Human-readable problems.
    """
    errs: list[str] = []
    folder = ep.path.name
    if not re.fullmatch(rf"ep{ep.number:02d}_{re.escape(ep.slug)}", folder):
        errs.append(f"folder name {folder!r} does not match number {ep.number} and slug {ep.slug!r}")
    if ep.status not in STATUSES:
        errs.append(f"status {ep.status!r} is not one of {', '.join(STATUSES)}")
    if not ep.title:
        errs.append("episode title is empty")
    if not (ep.path / "README.md").exists():
        errs.append("README.md is missing")
    if not ep.timeline:
        errs.append("timeline is empty")
    keys: set[str] = set()
    for e in ep.timeline:
        if e.kind == "invalid":
            errs.append(f"timeline entry {e.file} has neither 'scene' nor 'clip'")
            continue
        if e.key in keys:
            errs.append(f"timeline entry {e.key!r} appears twice")
        keys.add(e.key)
        if e.kind == "scene":
            f = ep.path / "scenes" / e.file
            if not e.scene_class:
                errs.append(f"scene {e.file!r} has no ':ClassName'")
            elif not f.exists():
                errs.append(f"scene file scenes/{e.file} does not exist")
            elif e.scene_class not in scene_classes(f):
                errs.append(f"class {e.scene_class} is not defined in scenes/{e.file}")
        elif not (ep.path / e.file).exists():
            errs.append(f"clip {e.file} does not exist (expected under {folder}/)")
    engine = ep.voice.get("engine", "piper")
    if engine not in TTS_ENGINES:
        errs.append(f"narration engine {engine!r} is not one of {', '.join(TTS_ENGINES)}")
    ids: set[str] = set()
    for s in ep.segments:
        where = f"narration segment {s.id or '<no id>'}"
        if not s.id:
            errs.append(f"{where}: missing id")
        elif s.id in ids:
            errs.append(f"{where}: duplicate id")
        ids.add(s.id)
        if s.entry not in keys:
            errs.append(f"{where}: entry {s.entry!r} is not in the timeline")
        if s.at < 0:
            errs.append(f"{where}: 'at' must be >= 0 seconds from the start of its entry")
        if s.budget <= 0:
            errs.append(f"{where}: 'budget' must be > 0 seconds")
        if not s.text:
            errs.append(f"{where}: empty text")
    return errs


def confirm_items(ep: Episode) -> list[str]:
    """Lines of the episode README still marked [CONFIRM]."""
    readme = ep.path / "README.md"
    if not readme.exists():
        return []
    return [line.strip() for line in readme.read_text().splitlines() if "[CONFIRM]" in line]
