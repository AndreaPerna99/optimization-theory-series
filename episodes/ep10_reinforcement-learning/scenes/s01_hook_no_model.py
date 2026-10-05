"""Keep the Gradient - Episode 10, s01: No model of the world

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class HookNoModel(PlaceholderScene):
    """No model of the world"""

    EPISODE = 10
    SCENE_ID = 's01_hook_no_model'
    TITLE = 'No model of the world'
    PURPOSE = (
        'Can a drone learn to act just by trying?',
    )
