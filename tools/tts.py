"""Keep the Gradient - Narration Engines

Three ways to turn a narration segment into a wav, chosen per episode in
narration.toml ([voice] engine = ...):

- ``piper``   local TTS (piper-tts). Voice models are fetched once into
              shared/audio/voices/ (not versioned).
- ``kokoro``  local TTS (kokoro-onnx), less synthetic on long technical
              sentences. Model files go in shared/audio/kokoro/ (not versioned).
- ``takes``   recorded audio: one file per segment id in the episode's
              takes/ folder (own voice, or exports from a commercial TTS).

Files are always keyed by segment ID, never by position, so editing the
script can never mix two voices or two versions of a line into one track.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from tools.episodes import ROOT, Episode, Segment

VOICES = ROOT / "shared" / "audio" / "voices"
KOKORO = ROOT / "shared" / "audio" / "kokoro"
TAKE_EXTENSIONS = (".wav", ".flac", ".mp3", ".m4a")


def _piper(segments: list[Segment], voice: dict, out: Path) -> None:
    """Synthesise with piper; the voice is pinned in narration.toml, never defaulted silently."""
    name = voice.get("voice")
    if not name:
        raise SystemExit("narration.toml [voice] has no 'voice' for the piper engine")
    exe = Path(sys.executable).with_name("piper")
    exe = str(exe) if exe.exists() else shutil.which("piper")
    if not exe:
        raise SystemExit("piper is not installed: pip install -e '.[tts]'")
    model = VOICES / f"{name}.onnx"
    if not model.exists():
        VOICES.mkdir(parents=True, exist_ok=True)
        subprocess.check_call([sys.executable, "-m", "piper.download_voices", name,
                               "--data-dir", str(VOICES)])
    # noise_w = 0 makes the timing reproducible from build to build
    flags = ["--length-scale", str(voice.get("length_scale", 1.0)),
             "--noise-w-scale", str(voice.get("noise_w", 0.0))]
    for s in segments:
        subprocess.run([exe, "-m", str(model), *flags, "-f", str(out / f"{s.id}.wav")],
                       input=s.text.encode(), check=True, stderr=subprocess.DEVNULL)


def _kokoro(segments: list[Segment], voice: dict, out: Path) -> None:
    """Synthesise with kokoro-onnx."""
    try:
        import soundfile as sf
        from kokoro_onnx import Kokoro
    except ImportError as exc:
        raise SystemExit("kokoro-onnx is not installed: pip install -e '.[tts]'") from exc
    model = KOKORO / voice.get("model", "kokoro-v1.0.onnx")
    voices = KOKORO / voice.get("voices", "voices-v1.0.bin")
    if not model.exists() or not voices.exists():
        raise SystemExit(f"missing kokoro files in {KOKORO}; see shared/audio/README.md")
    name = voice.get("voice")
    if not name:
        raise SystemExit("narration.toml [voice] has no 'voice' for the kokoro engine")
    k = Kokoro(str(model), str(voices))
    for s in segments:
        audio, sr = k.create(s.text, voice=name, speed=float(voice.get("speed", 1.0)))
        sf.write(out / f"{s.id}.wav", audio, sr)


def _takes(segments: list[Segment], ep: Episode, out: Path) -> None:
    """Convert recorded takes (takes/<id>.<ext>) to wav."""
    missing = []
    for s in segments:
        src = next((ep.path / "takes" / f"{s.id}{x}" for x in TAKE_EXTENSIONS
                    if (ep.path / "takes" / f"{s.id}{x}").exists()), None)
        if src is None:
            missing.append(s.id)
            continue
        subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-i", str(src), str(out / f"{s.id}.wav")])
    if missing:
        raise SystemExit(f"no take for segment(s): {', '.join(missing)} in {ep.path / 'takes'}")


def synthesise(ep: Episode, out: Path) -> dict[str, Path]:
    """Produce one wav per narration segment of an episode.

        Parameters
        ----------
        ep : Episode
            The episode, with its [voice] settings and segments.
        out : pathlib.Path
            Output folder; wiped first so no stale file survives.

        Returns
        -------
        dict
            Segment id -> wav path.
    """
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    engine = ep.voice.get("engine", "piper")
    if engine == "piper":
        _piper(ep.segments, ep.voice, out)
    elif engine == "kokoro":
        _kokoro(ep.segments, ep.voice, out)
    elif engine == "takes":
        _takes(ep.segments, ep, out)
    else:
        raise SystemExit(f"unknown narration engine {engine!r}")
    return {s.id: out / f"{s.id}.wav" for s in ep.segments}
