"""Keep the Gradient - Episode 2, s03: The simplex method

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SimplexWalk(PlaceholderScene):
    """The simplex method"""

    EPISODE = 2
    SCENE_ID = 's03_simplex_walk'
    TITLE = 'The simplex method'
    PURPOSE = (
        'Walk vertex to vertex along edges',
        'Stop when no neighbour is better: global by convexity',
    )
