"""Keep the Gradient - LaTeX Template

One template for every formula in the series, with macros that follow the
notation table in SERIES.md. Use the macros instead of spelling things out,
so a notation change is made once, here.

Manim's default preamble loads amsmath and amssymb; everything else the
series needs is defined below. \\providecommand never overrides an existing
definition, so the template stays safe if manim's preamble grows.
"""
from __future__ import annotations

from manim import TexTemplate

PREAMBLE = r"""
\usepackage{mathtools}
\usepackage{bm}
\providecommand{\R}{\mathbb{R}}
\providecommand{\E}{\mathbb{E}}
\providecommand{\T}{^{\top}}
\providecommand{\opt}{^{\star}}
\providecommand{\grad}{\nabla}
\providecommand{\hess}{\nabla^2}
\providecommand{\norm}[1]{\left\lVert #1 \right\rVert}
\providecommand{\abs}[1]{\left\lvert #1 \right\rvert}
\providecommand{\Lag}{\mathcal{L}}
\providecommand{\Nb}{\mathcal{N}}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator*{\argmax}{arg\,max}
"""

TEMPLATE = TexTemplate()
TEMPLATE.add_to_preamble(PREAMBLE)
