"""Keep the Gradient - Episode 2, s02: Linear programs and the polytope

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class LpPolytope(PlaceholderScene):
    """Linear programs and the polytope"""

    EPISODE = 2
    SCENE_ID = 's02_lp_polytope'
    TITLE = 'Linear programs and the polytope'
    PURPOSE = (
        'Linear objective and constraints',
        'Level lines sweep to the last vertex',
        'Outcomes: infeasible, unbounded, optimal',
    )
