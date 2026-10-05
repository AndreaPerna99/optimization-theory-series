"""Keep the Gradient - Episode 3, s03: Lagrange multipliers

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class LagrangeTangency(PlaceholderScene):
    """Lagrange multipliers"""

    EPISODE = 3
    SCENE_ID = 's03_lagrange_tangency'
    TITLE = 'Lagrange multipliers'
    PURPOSE = (
        'Level curves slide until tangent to the constraint',
        'grad f and grad h become parallel',
    )
