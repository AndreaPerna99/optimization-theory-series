"""Keep the Gradient - Command-Line Build Tool

    ./kg status                       overview of every episode
    ./kg check [EP]                   validate manifests, scenes and narration
    ./kg render EP [-q l|m|h|k] [--only NAME ...]
    ./kg assemble EP [-q ...] [--copy]
    ./kg narrate EP [-q ...] [--check-only]
    ./kg new-scene EP sNN_name --title "..." [--purpose "..." ...]

EP is 1, 01 or ep01. Quality: l = 480p15 drafts, m = 720p30, h = 1080p60
(release), k = 2160p60. Outputs go to build/epNN/.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from tools import episodes as eps
from tools import media
from tools.templates import class_name, placeholder_scene

BUILD = eps.ROOT / "build"


def _load_valid(ref: str) -> eps.Episode:
    """Load an episode and stop with its problems if it is invalid."""
    ep = eps.load(eps.find(ref))
    errs = eps.validate(ep)
    if errs:
        raise SystemExit(f"{ep.code} is invalid:\n  - " + "\n  - ".join(errs))
    return ep


def _render_path(ep: eps.Episode, entry: eps.Entry, quality: str) -> Path:
    """Where manim writes a scene's video for a given quality."""
    res = media.QUALITIES[quality][1]
    return BUILD / ep.code / "videos" / Path(entry.file).stem / res / f"{entry.scene_class}.mp4"


def cmd_status(args) -> int:
    """Print one line per episode."""
    print(f"{'ep':4} {'status':10} {'scenes':>6} {'placeh.':>7} {'clips':>5} {'narr.':>5} {'confirm':>7}  title")
    for path in eps.all_paths():
        ep = eps.load(path)
        scenes = [e for e in ep.timeline if e.kind == "scene"]
        ph = sum(eps.is_placeholder(path / "scenes" / e.file) for e in scenes
                 if (path / "scenes" / e.file).exists())
        clips = sum(e.kind == "clip" for e in ep.timeline)
        print(f"{ep.code:4} {ep.status:10} {len(scenes):>6} {ph:>7} {clips:>5} {len(ep.segments):>5} "
              f"{len(eps.confirm_items(ep)):>7}  {ep.title}")
    return 0


def cmd_check(args) -> int:
    """Validate one or all episodes; nonzero exit if anything is wrong."""
    paths = [eps.find(args.episode)] if args.episode else eps.all_paths()
    bad = 0
    for path in paths:
        try:
            ep = eps.load(path)
        except Exception as exc:  # malformed TOML must not hide the other episodes
            print(f"{path.name}: cannot load: {exc}")
            bad += 1
            continue
        errs = eps.validate(ep)
        print(f"{ep.code}: {'ok' if not errs else f'{len(errs)} problem(s)'}")
        for e in errs:
            print(f"    - {e}")
        bad += bool(errs)
    return 1 if bad else 0


def cmd_render(args) -> int:
    """Render an episode's scenes with manim."""
    ep = _load_valid(args.episode)
    flag = media.QUALITIES[args.quality][0]
    env = dict(os.environ, PYTHONPATH=f"{eps.ROOT}{os.pathsep}{os.environ.get('PYTHONPATH', '')}")
    todo = [e for e in ep.timeline if e.kind == "scene"
            and (not args.only or e.scene_class in args.only or e.file in args.only)]
    if args.only and not todo:
        raise SystemExit(f"nothing in the {ep.code} timeline matches {args.only}")
    for e in todo:
        print(f"==> {ep.code} {e.scene_class} ({e.file})", flush=True)
        subprocess.check_call([sys.executable, "-m", "manim", "render", flag,
                               "--config_file", str(eps.ROOT / "manim.cfg"),
                               "--media_dir", str(BUILD / ep.code),
                               str(ep.path / "scenes" / e.file), e.scene_class], env=env)
    print(f"==> rendered {len(todo)} scene(s) under build/{ep.code}/videos/")
    return 0


def cmd_assemble(args) -> int:
    """Join scenes and clips in timeline order; write the timeline offsets."""
    ep = _load_valid(args.episode)
    res = media.QUALITIES[args.quality][1]
    fps = media.QUALITIES[args.quality][4]
    files, rows, t = [], [], 0.0
    for e in ep.timeline:
        if e.kind == "scene":
            f = _render_path(ep, e, args.quality)
            if not f.exists():
                raise SystemExit(f"missing {res} render of {e.scene_class}: run ./kg render {ep.number} -q {args.quality}")
        else:
            f = media.normalize_clip(ep.path / e.file, BUILD / ep.code / "clips" / res / (Path(e.file).stem + ".mp4"),
                                     args.quality)
        d = media.duration(f)
        files.append(f)
        rows.append({"entry": e.key, "file": str(f.relative_to(eps.ROOT)), "start": round(t, 3), "duration": round(d, 3)})
        t += d
    out = BUILD / ep.code / "final" / f"{ep.code}_{ep.slug}_{res}.mp4"
    media.concat(files, out, fps, copy=args.copy)
    (BUILD / ep.code / "final" / f"timeline_{res}.json").write_text(
        json.dumps({"episode": ep.code, "quality": res, "video": str(out.relative_to(eps.ROOT)),
                    "entries": rows}, indent=2))
    print(f"==> {out.relative_to(eps.ROOT)}  ({t:.1f} s, {len(files)} items)")
    return 0


def cmd_narrate(args) -> int:
    """Synthesise narration, check budgets and overlaps, and mux it onto the assembly."""
    from tools import tts

    ep = _load_valid(args.episode)
    if not ep.segments:
        raise SystemExit(f"{ep.code} has no narration segments yet (narration.toml)")
    res = media.QUALITIES[args.quality][1]
    tl_file = BUILD / ep.code / "final" / f"timeline_{res}.json"
    if not tl_file.exists():
        raise SystemExit(f"no {res} assembly: run ./kg assemble {ep.number} -q {args.quality}")
    tl = json.loads(tl_file.read_text())
    entries = {r["entry"]: r for r in tl["entries"]}
    wavs = tts.synthesise(ep, BUILD / ep.code / "narration" / ep.voice.get("engine", "piper"))
    cues, problems = [], 0
    timed = sorted(((entries[s.entry]["start"] + s.at, s) for s in ep.segments), key=lambda c: c[0])
    for i, (start, s) in enumerate(timed):
        d = media.duration(wavs[s.id])
        end = start + d
        notes = []
        if d > s.budget:
            notes.append(f"OVER budget by {d - s.budget:.2f} s")
        entry = entries[s.entry]
        if end > entry["start"] + entry["duration"]:
            notes.append("runs past the end of its entry")
        if i + 1 < len(timed) and end > timed[i + 1][0]:
            notes.append(f"overlaps {timed[i + 1][1].id}")
        problems += bool(notes)
        print(f"  {s.id:18} {start:8.2f} s  {d:5.2f}/{s.budget:5.2f} s  {'; '.join(notes) or 'ok'}")
        cues.append((wavs[s.id], start))
    if args.check_only:
        return 1 if problems else 0
    video = eps.ROOT / tl["video"]
    out = video.with_name(video.stem + "_narrated.mp4")
    media.mux_narration(video, cues, out)
    print(f"==> {out.relative_to(eps.ROOT)}" + (f"  ({problems} segment(s) need attention)" if problems else ""))
    return 0


def cmd_new_scene(args) -> int:
    """Create a placeholder scene and append it to the episode timeline."""
    path = eps.find(args.episode)
    ep = eps.load(path)
    try:
        cls = class_name(args.scene_id)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    f = path / "scenes" / f"{args.scene_id}.py"
    if f.exists():
        raise SystemExit(f"{f.relative_to(eps.ROOT)} already exists")
    f.write_text(placeholder_scene(ep.number, args.scene_id, args.title, args.purpose or []))
    with open(path / "episode.toml", "a") as fh:
        fh.write(f'\n[[timeline]]\nscene = "{args.scene_id}.py:{cls}"\n')
    print(f"created {f.relative_to(eps.ROOT)} ({cls}); appended to the END of the timeline, "
          f"move the entry in episode.toml if it belongs elsewhere")
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse the command line and dispatch."""
    p = argparse.ArgumentParser(prog="kg", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="overview of every episode").set_defaults(fn=cmd_status)
    c = sub.add_parser("check", help="validate manifests, scenes and narration")
    c.add_argument("episode", nargs="?")
    c.set_defaults(fn=cmd_check)
    for name, fn, hlp in (("render", cmd_render, "render scenes with manim"),
                          ("assemble", cmd_assemble, "join scenes and clips"),
                          ("narrate", cmd_narrate, "synthesise and mux narration")):
        s = sub.add_parser(name, help=hlp)
        s.add_argument("episode")
        s.add_argument("-q", "--quality", choices=list(media.QUALITIES), default="l")
        s.set_defaults(fn=fn)
        if name == "render":
            s.add_argument("--only", nargs="+", help="scene class names or files to render")
        if name == "assemble":
            s.add_argument("--copy", action="store_true", help="stream-copy instead of re-encoding")
        if name == "narrate":
            s.add_argument("--check-only", action="store_true", help="synthesise and report, do not mux")
    n = sub.add_parser("new-scene", help="create a placeholder scene")
    n.add_argument("episode")
    n.add_argument("scene_id", help="e.g. s05_step_size")
    n.add_argument("--title", required=True)
    n.add_argument("--purpose", action="append", help="what the scene must show (repeatable)")
    n.set_defaults(fn=cmd_new_scene)
    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
