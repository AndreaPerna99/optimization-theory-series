"""Keep the Gradient - Episode 8, s03: Distributed gradient descent

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Dgd(PlaceholderScene):
    """Distributed gradient descent"""

    EPISODE = 8
    SCENE_ID = 's03_dgd'
    TITLE = 'Distributed gradient descent'
    PURPOSE = (
        'Mix with neighbours, step on the local gradient',
    )
