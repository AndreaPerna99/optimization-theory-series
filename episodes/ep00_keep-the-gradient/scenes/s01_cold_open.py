"""Keep the Gradient - Episode 0, s01: Cold open: the quadrotor

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class ColdOpen(PlaceholderScene):
    """Cold open: the quadrotor"""

    EPISODE = 0
    SCENE_ID = 's01_cold_open'
    TITLE = 'Cold open: the quadrotor'
    PURPOSE = (
        'Quadrotor footage [CONFIRM]',
        'Line: this machine solves an optimization problem many times per second',
        'Only if the controller really does (CONFIRM)',
    )
