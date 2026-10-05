"""Keep the Gradient - Episode 10, s07: Policy gradient

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class PolicyGradient(PlaceholderScene):
    """Policy gradient"""

    EPISODE = 10
    SCENE_ID = 's07_policy_gradient'
    TITLE = 'Policy gradient'
    PURPOSE = (
        'Gradient ascent on expected return',
        'Actor-critic, PPO, SAC (names only)',
    )
