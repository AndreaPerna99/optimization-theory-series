"""Keep the Gradient - Episode 9, s07: The quadrotor flies

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class QuadrotorFlight(PlaceholderScene):
    """The quadrotor flies"""

    EPISODE = 9
    SCENE_ID = 's07_quadrotor_flight'
    TITLE = 'The quadrotor flies'
    PURPOSE = (
        'Ghost plan redrawn every instant',
        'Gust, re-plan, saturation active',
        'Footage and controller [CONFIRM]',
    )
