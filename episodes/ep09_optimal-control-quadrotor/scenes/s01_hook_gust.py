"""Keep the Gradient - Episode 9, s01: Flying through a gust

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class HookGust(PlaceholderScene):
    """Flying through a gust"""

    EPISODE = 9
    SCENE_ID = 's01_hook_gust'
    TITLE = 'Flying through a gust'
    PURPOSE = (
        'Reach the target within motor limits',
        'The world keeps pushing',
    )
