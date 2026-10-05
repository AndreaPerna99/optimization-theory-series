"""Keep the Gradient - Episode 12, s08: The moving optimum

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class MovingOptimum(PlaceholderScene):
    """The moving optimum"""

    EPISODE = 12
    SCENE_ID = 's08_moving_optimum'
    TITLE = 'The moving optimum'
    PURPOSE = (
        'The landscape starts to move',
        'Stop at zero gradient: left behind; keep stepping: stay close',
    )
