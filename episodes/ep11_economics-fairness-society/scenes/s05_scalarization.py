"""Keep the Gradient - Episode 11, s05: Weighted sums

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Scalarization(PlaceholderScene):
    """Weighted sums"""

    EPISODE = 11
    SCENE_ID = 's05_scalarization'
    TITLE = 'Weighted sums'
    PURPOSE = (
        'Weight slider moves along the front',
        "Non-convex fronts: gaps weighted sums can't reach",
    )
