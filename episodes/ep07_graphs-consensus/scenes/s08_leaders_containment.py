"""Keep the Gradient - Episode 7, s08: Leaders

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class LeadersContainment(PlaceholderScene):
    """Leaders"""

    EPISODE = 7
    SCENE_ID = 's08_leaders_containment'
    TITLE = 'Leaders'
    PURPOSE = (
        'Leaders fixed, followers pulled in',
        'x_F = H x_L: inside the convex hull',
    )
