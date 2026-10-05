"""Keep the Gradient - ffmpeg Helpers"""
from __future__ import annotations

import subprocess
from pathlib import Path

# kg quality letter -> (manim flag, resolution folder, width, height, fps)
QUALITIES = {
    "l": ("-ql", "480p15", 854, 480, 15),
    "m": ("-qm", "720p30", 1280, 720, 30),
    "h": ("-qh", "1080p60", 1920, 1080, 60),
    "k": ("-qk", "2160p60", 3840, 2160, 60),
}


def duration(path: Path) -> float:
    """Length of a media file in seconds (ffprobe)."""
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", str(path)])
    return float(out.strip())


def normalize_clip(src: Path, dst: Path, quality: str) -> Path:
    """Re-encode a clip to the episode's frame size and rate, without audio.

    Footage arrives in any format; the assembly needs every item at the same
    resolution, frame rate and pixel format. The result is cached and redone
    only when the source is newer.

        Parameters
        ----------
        src : pathlib.Path
            Source clip.
        dst : pathlib.Path
            Destination mp4.
        quality : str
            kg quality letter (l, m, h, k).

        Returns
        -------
        pathlib.Path
            ``dst``.
    """
    _, _, w, h, fps = QUALITIES[quality]
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        return dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    vf = (f"scale={w}:{h}:force_original_aspect_ratio=decrease,"
          f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,fps={fps},format=yuv420p")
    subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, "-an",
                           "-c:v", "libx264", "-crf", "18", str(dst)])
    return dst


def concat(files: list[Path], out: Path, fps: int, copy: bool = False) -> None:
    """Join video files in order.

        Parameters
        ----------
        files : list of pathlib.Path
            Inputs in playback order.
        out : pathlib.Path
            Output mp4.
        fps : int
            Output frame rate (ignored with ``copy``).
        copy : bool
            Stream-copy instead of re-encoding: fast, but only safe when every
            input came out of the same encoder settings.

        Returns
        -------
        None
    """
    out.parent.mkdir(parents=True, exist_ok=True)
    lst = out.with_suffix(".txt")
    lst.write_text("".join(f"file '{f.resolve()}'\n" for f in files))
    codec = ["-c", "copy"] if copy else ["-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
                                         "-r", str(fps), "-an"]
    try:
        subprocess.check_call(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                               "-i", str(lst), *codec, str(out)])
    finally:
        lst.unlink(missing_ok=True)


def mux_narration(video: Path, cues: list[tuple[Path, float]], out: Path) -> None:
    """Place each narration wav at its absolute start time and mux onto the video.

    The mixed track is padded half a second PAST the picture: AAC quantises to
    1024-sample frames, so padding to exactly the video length lands short and
    -shortest would then cut the last frames of the picture.

        Parameters
        ----------
        video : pathlib.Path
            Assembled silent video.
        cues : list of (pathlib.Path, float)
            Each wav and its absolute start in seconds.
        out : pathlib.Path
            Narrated output mp4.

        Returns
        -------
        None
    """
    dur = duration(video)
    args = ["ffmpeg", "-v", "error", "-y", "-i", str(video)]
    parts, labels = [], []
    for i, (wav, start) in enumerate(cues):
        args += ["-i", str(wav)]
        ms = int(round(start * 1000))
        parts.append(f"[{i + 1}:a]adelay={ms}|{ms}[a{i}]")
        labels.append(f"[a{i}]")
    chain = ";".join(parts) + ";" + "".join(labels) + \
        f"amix=inputs={len(cues)}:normalize=0[mix];[mix]apad=whole_dur={dur + 0.5:.3f}[aout]"
    subprocess.check_call(args + ["-filter_complex", chain, "-map", "0:v", "-map", "[aout]",
                                  "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out)])
