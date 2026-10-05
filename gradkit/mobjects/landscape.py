"""Keep the Gradient - Landscapes (specified, not yet implemented)

The objective is shown two ways that must always agree: as a 3D surface
(the landscape the ball rolls on) and as a contour map seen from above (where
the gradient is perpendicular to the level curves). Both are needed from
Episode 1 on; implement them during the Episode 1 pilot.
"""
from __future__ import annotations

from collections.abc import Callable

from manim import VGroup

ObjectiveFn = Callable[[float, float], float]


class ContourMap(VGroup):
    """Level curves of f(x, y) on a set of 2D axes.

    Specification
    -------------
    - inputs: ``f``, ``axes`` (manim Axes), ``levels`` (sequence of values),
      optional sampling resolution;
    - level curves traced numerically (marching squares on a grid, or
      ``skimage.measure.find_contours``) and mapped with ``axes.c2p``;
    - colour ``style.LEVEL``, opacity rising from the outermost to the
      innermost level, so the minimum reads as the brightest region;
    - must work for non-convex f (several closed curves per level).
    """

    def __init__(self, f: ObjectiveFn, axes, levels, resolution: int = 200) -> None:
        raise NotImplementedError("ContourMap: implement during the Episode 1 pilot (see class docstring)")


class Landscape3D(VGroup):
    """The surface z = f(x, y) on ThreeDAxes.

    Specification
    -------------
    - inputs: ``f``, ``axes`` (ThreeDAxes), ``x_range``, ``y_range``, resolution;
    - built from ``manim.Surface`` mapped with ``axes.c2p(x, y, f(x, y))``;
    - fill coloured by height from ``style.LANDSCAPE_LOW`` to ``style.LANDSCAPE_HIGH``
      (``Surface.set_fill_by_value``);
    - a helper to place a ``Ball`` on the surface at (x, y), so iterates
      computed in 2D can be shown in 3D.
    """

    def __init__(self, f: ObjectiveFn, axes, x_range, y_range, resolution: int = 40) -> None:
        raise NotImplementedError("Landscape3D: implement during the Episode 1 pilot (see class docstring)")
