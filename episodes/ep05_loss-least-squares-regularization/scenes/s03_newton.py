"""Keep the Gradient - Episode 5, s03: Newton's method

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Newton(PlaceholderScene):
    """Newton's method"""

    EPISODE = 5
    SCENE_ID = 's03_newton'
    TITLE = "Newton's method"
    PURPOSE = (
        'Use curvature, not just slope',
        'One step on a quadratic vs many GD steps',
    )
