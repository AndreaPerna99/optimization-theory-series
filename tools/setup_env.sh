#!/usr/bin/env bash
# Keep the Gradient - create the single project environment in .venv
#   ./tools/setup_env.sh          manim, numpy, scipy, pytest
#   ./tools/setup_env.sh --tts    also piper-tts and kokoro-onnx for narration
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

missing=()
for cmd in ffmpeg ffprobe latex dvisvgm pkg-config; do
  command -v "$cmd" >/dev/null || missing+=("$cmd")
done
pkg-config --exists pangocairo 2>/dev/null || missing+=("pango/cairo headers")
if (( ${#missing[@]} )); then
  echo "missing system dependencies: ${missing[*]}"
  echo "  sudo apt install -y ffmpeg texlive texlive-latex-extra dvisvgm libpango1.0-dev libcairo2-dev pkg-config"
  exit 1
fi

python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
extras="dev"
[[ "${1:-}" == "--tts" ]] && extras="dev,tts"
.venv/bin/python -m pip install -e ".[$extras]"
echo "==> ready: ./kg status, python -m pytest (with .venv activated)"
