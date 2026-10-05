"""Keep the Gradient - Episode 1, s07: The pendulum and momentum

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class PendulumMomentum(PlaceholderScene):
    """The pendulum and momentum"""

    EPISODE = 1
    SCENE_ID = 's07_pendulum_momentum'
    TITLE = 'The pendulum and momentum'
    PURPOSE = (
        'Damped pendulum next to heavy-ball iterates',
        'Inertia overshoots: that is momentum',
        'Pendulum in honey = gradient flow',
    )
