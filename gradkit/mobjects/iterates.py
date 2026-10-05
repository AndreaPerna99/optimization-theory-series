"""Keep the Gradient - Iterates and Paths

The ball is the current iterate x_k; an iterate path is the sequence of points
an algorithm actually produced; a ghost path is a plan that has not happened
(an MPC horizon, a predicted trajectory). Paths take points already mapped to
scene coordinates, e.g. ``axes.c2p(*x)`` applied to the output of an algorithm
in ``gradkit.algorithms``.
"""
from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from manim import DashedVMobject, Dot, VGroup, VMobject

from gradkit import style


def _as_points(points: Sequence[Sequence[float]]) -> np.ndarray:
    """Lift 2D or 3D points to the (n, 3) array manim expects.

        Parameters
        ----------
        points : sequence of sequence of float
            Points with 2 or 3 coordinates each.

        Returns
        -------
        numpy.ndarray
            Array of shape (n, 3).
    """
    pts = np.asarray(points, dtype=float)
    if pts.ndim != 2 or pts.shape[1] not in (2, 3):
        raise ValueError(f"expected points of shape (n, 2) or (n, 3), got {pts.shape}")
    if pts.shape[1] == 2:
        pts = np.hstack([pts, np.zeros((len(pts), 1))])
    return pts


class Ball(Dot):
    """The current iterate x_k."""

    def __init__(self, point=None, radius: float = 0.12, **kwargs) -> None:
        """Create the ball.

            Parameters
            ----------
            point : array-like, optional
                Scene position. Defaults to the origin.
            radius : float
                Radius in frame units.
            **kwargs
                Forwarded to ``manim.Dot``.

            Returns
            -------
            None
        """
        kwargs.setdefault("color", style.ITERATE)
        super().__init__(point=np.zeros(3) if point is None else point, radius=radius, **kwargs)


class IteratePath(VGroup):
    """The polyline of iterates x_0, x_1, ... with a small dot on each."""

    def __init__(self, points: Sequence[Sequence[float]], color=style.ITERATE,
                 dot_radius: float = 0.04, stroke_width: float = 3.0) -> None:
        """Create the path.

            Parameters
            ----------
            points : sequence of sequence of float
                Iterates in scene coordinates.
            color : str
                Colour of segments and dots.
            dot_radius : float
                Radius of the per-iterate dots; 0 hides them.
            stroke_width : float
                Width of the segments.

            Returns
            -------
            None
        """
        pts = _as_points(points)
        line = VMobject(stroke_color=color, stroke_width=stroke_width)
        line.set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=dot_radius, color=color) for p in pts]) if dot_radius > 0 else VGroup()
        super().__init__(line, dots)
        self.line, self.dots = line, dots


class GhostPath(VGroup):
    """A planned trajectory: dashed and translucent, never mistaken for motion."""

    def __init__(self, points: Sequence[Sequence[float]], num_dashes: int = 40) -> None:
        """Create the ghost path.

            Parameters
            ----------
            points : sequence of sequence of float
                Planned positions in scene coordinates.
            num_dashes : int
                Number of dashes along the path.

            Returns
            -------
            None
        """
        line = VMobject(stroke_color=style.PLAN, stroke_width=3.0, stroke_opacity=style.PLAN_OPACITY)
        line.set_points_smoothly(_as_points(points))
        super().__init__(DashedVMobject(line, num_dashes=num_dashes))
