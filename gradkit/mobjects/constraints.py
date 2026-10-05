"""Keep the Gradient - Constraints and Multipliers

The feasible region is a translucent fill bounded by walls; a wall carries
short hatch marks on its INFEASIBLE side; a force arrow is a multiplier mu_i,
drawn from the wall into the feasible region with length proportional to mu_i.
An inactive wall gets a force arrow of length zero (complementary slackness).
"""
from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from manim import Arrow, Line, MathTex, Polygon, VGroup

from gradkit import style


class FeasibleRegion(Polygon):
    """A convex feasible region given by its vertices in scene coordinates."""

    def __init__(self, *vertices: Sequence[float], **kwargs) -> None:
        """Create the region.

            Parameters
            ----------
            *vertices : sequence of float
                Polygon vertices in order, e.g. from ``algorithms.lp.vertices_2d``.
            **kwargs
                Forwarded to ``manim.Polygon``.

            Returns
            -------
            None
        """
        kwargs.setdefault("color", style.FEASIBLE)
        kwargs.setdefault("fill_opacity", style.FEASIBLE_OPACITY)
        kwargs.setdefault("stroke_width", 0)
        pts = [np.append(np.asarray(v, dtype=float), 0.0)[:3] for v in vertices]
        super().__init__(*pts, **kwargs)


class Wall(VGroup):
    """A constraint boundary with hatch marks on the infeasible side."""

    def __init__(self, start, end, infeasible_side: Sequence[float],
                 hatches: int = 12, hatch_length: float = 0.15) -> None:
        """Create the wall.

            Parameters
            ----------
            start, end : array-like
                End points of the wall in scene coordinates.
            infeasible_side : sequence of float
                Any vector pointing from the wall into the infeasible side
                (for g(x) <= 0 this is the direction of grad g).
            hatches : int
                Number of hatch marks.
            hatch_length : float
                Length of each hatch mark.

            Returns
            -------
            None
        """
        a, b = np.asarray(start, dtype=float), np.asarray(end, dtype=float)
        a, b = np.append(a, 0.0)[:3], np.append(b, 0.0)[:3]
        out = np.append(np.asarray(infeasible_side, dtype=float), 0.0)[:3]
        tangent = (b - a) / np.linalg.norm(b - a)
        normal = out - np.dot(out, tangent) * tangent
        if np.linalg.norm(normal) < 1e-9:
            raise ValueError("infeasible_side must not be parallel to the wall")
        normal /= np.linalg.norm(normal)
        hatch_dir = hatch_length * (normal * 0.8 + tangent * 0.6)
        line = Line(a, b, color=style.FEASIBLE, stroke_width=4)
        marks = VGroup(*[Line(p, p + hatch_dir, color=style.FEASIBLE, stroke_width=2)
                         for p in np.linspace(a, b, hatches)])
        super().__init__(line, marks)
        self.line, self.marks, self.normal = line, marks, normal


class ForceArrow(VGroup):
    """A multiplier as the force a wall exerts on the iterate."""

    def __init__(self, point, direction: Sequence[float], magnitude: float,
                 scale: float = 1.0, label: str | None = r"\mu") -> None:
        """Create the arrow.

            Parameters
            ----------
            point : array-like
                Where the force acts (the iterate on the wall).
            direction : sequence of float
                Direction of the push, into the feasible region (-grad g).
            magnitude : float
                The multiplier value mu_i >= 0.
            scale : float
                Frame units per unit of multiplier.
            label : str or None
                LaTeX label placed at the arrow tip; None for no label.

            Returns
            -------
            None
        """
        if magnitude < 0:
            raise ValueError("a wall can push but never pull: multipliers are >= 0")
        p = np.append(np.asarray(point, dtype=float), 0.0)[:3]
        d = np.append(np.asarray(direction, dtype=float), 0.0)[:3]
        d /= np.linalg.norm(d)
        arrow = Arrow(p, p + d * magnitude * scale, buff=0, color=style.MULTIPLIER,
                      max_tip_length_to_length_ratio=0.3)
        parts = [arrow]
        if label is not None and magnitude > 0:
            tex = MathTex(label, color=style.MULTIPLIER, font_size=style.CAPTION_SIZE)
            tex.next_to(arrow.get_end(), d, buff=0.1)
            parts.append(tex)
        super().__init__(*parts)
        self.arrow = arrow
