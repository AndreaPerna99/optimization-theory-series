"""Keep the Gradient - Episode 12, s01: No map, no leader

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class HookAnts(PlaceholderScene):
    """No map, no leader"""

    EPISODE = 12
    SCENE_ID = 's01_hook_ants'
    TITLE = 'No map, no leader'
    PURPOSE = (
        'Ants find the shortest path',
        'What if the food moves?',
    )
