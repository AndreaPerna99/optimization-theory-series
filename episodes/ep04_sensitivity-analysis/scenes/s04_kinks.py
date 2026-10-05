"""Keep the Gradient - Episode 4, s04: Kinks

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Kinks(PlaceholderScene):
    """Kinks"""

    EPISODE = 4
    SCENE_ID = 's04_kinks'
    TITLE = 'Kinks'
    PURPOSE = (
        'Solution path bends when the active set changes',
        'Strictly convex QP: continuous, piecewise linear',
    )
