"""Keep the Gradient - Episode 3, s01: The ball hits a wall

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class HookWall(PlaceholderScene):
    """The ball hits a wall"""

    EPISODE = 3
    SCENE_ID = 's01_hook_wall'
    TITLE = 'The ball hits a wall'
    PURPOSE = (
        'Where does it stop, and how hard does the wall push?',
    )
