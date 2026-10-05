"""Keep the Gradient - Episode 0, s05: The series map

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SeriesMap(PlaceholderScene):
    """The series map"""

    EPISODE = 0
    SCENE_ID = 's05_series_map'
    TITLE = 'The series map'
    PURPOSE = (
        'Landscape map, one location per episode',
        'Building blocks and practical examples in every episode',
        'Not only engineering: natural and social systems too',
    )
