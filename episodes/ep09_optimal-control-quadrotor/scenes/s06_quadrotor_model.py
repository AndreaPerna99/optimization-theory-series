"""Keep the Gradient - Episode 9, s06: The quadrotor

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class QuadrotorModel(PlaceholderScene):
    """The quadrotor"""

    EPISODE = 9
    SCENE_ID = 's06_quadrotor_model'
    TITLE = 'The quadrotor'
    PURPOSE = (
        '12 states, 4 thrusts, underactuated',
        'Must tilt to move sideways',
    )
