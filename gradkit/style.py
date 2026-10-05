"""Keep the Gradient - Series Style

Colours by role, sizes and timing shared by every scene. A colour names a
ROLE from the visual language in SERIES.md, never a decoration: the same
object keeps the same colour in all thirteen episodes, so viewers learn it.

The palette is provisional until the Episode 1 pilot fixes the look of the
series. Change values here, never in a scene file.
"""
from __future__ import annotations

from manim import MathTex, Tex, Text, config

# ---------------------------------------------------------------------------
# stage
BG = "#0E1116"          # dark stage so the mathematics carries the frame
TEXT = "#E8E6E3"        # default text and formulas
MUTED = "#8B949E"       # secondary text, axes, inactive things
GRID = "#30363D"        # background grids, faint guides

# ---------------------------------------------------------------------------
# single-agent optimization
ITERATE = "#FFD166"     # the ball: the current iterate x_k
STEP = "#FF8C42"        # the step direction, the negative gradient
OPTIMUM = "#06D6A0"     # the optimum x*, and anything that converged
DIVERGE = "#EF476F"     # divergence, error, anything that went wrong
LEVEL = "#5C7AEA"       # level curves of the objective
LANDSCAPE_LOW = "#14213D"   # colour scale of 3D landscapes, low values...
LANDSCAPE_HIGH = "#4CC9F0"  # ...to high values

# ---------------------------------------------------------------------------
# constraints and multipliers. Multipliers, shadow prices and sensitivities
# are ONE object seen four ways (SERIES.md, "the threads"), so they share ONE
# colour on purpose.
FEASIBLE = "#4CC9F0"    # feasible region (fill at FEASIBLE_OPACITY) and its walls
FEASIBLE_OPACITY = 0.18
MULTIPLIER = "#F72585"  # wall force mu_i, dual variable y_i, shadow price, sensitivity
PRICE = MULTIPLIER

# ---------------------------------------------------------------------------
# many agents
AGENT = "#90E0EF"       # agents / followers on a graph
LEADER = "#C77DFF"      # leaders (agents that do not update)
EDGE = "#4A5568"        # communication edges

# ---------------------------------------------------------------------------
# time
PLAN = "#ADB5BD"        # ghost trajectories: a plan, not what happens
PLAN_OPACITY = 0.45

HIGHLIGHT = "#FFF3B0"   # the quantity under discussion right now

# ---------------------------------------------------------------------------
# type
FONT = "sans-serif"     # replace with the brand font once it is in shared/fonts
TITLE_SIZE = 48
HEADING_SIZE = 40
BODY_SIZE = 32
EQ_SIZE = 40
CAPTION_SIZE = 28
NOTE_SIZE = 24

# ---------------------------------------------------------------------------
# layout and timing (frame units and seconds)
MARGIN = 0.5
FADE = 0.6              # standard fade in/out
BEAT = 1.0              # a pause that lets a picture land


def apply() -> None:
    """Set the global rendering defaults used by every scene.

        Parameters
        ----------
        None

        Returns
        -------
        None
    """
    from gradkit.tex import TEMPLATE

    config.background_color = BG
    config.tex_template = TEMPLATE
    Text.set_default(color=TEXT, font=FONT)
    MathTex.set_default(color=TEXT, tex_template=TEMPLATE)
    Tex.set_default(color=TEXT, tex_template=TEMPLATE)
