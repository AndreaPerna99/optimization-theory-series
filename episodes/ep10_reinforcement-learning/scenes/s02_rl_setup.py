"""Keep the Gradient - Episode 10, s02: Rewards and returns

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class RlSetup(PlaceholderScene):
    """Rewards and returns"""

    EPISODE = 10
    SCENE_ID = 's02_rl_setup'
    TITLE = 'Rewards and returns'
    PURPOSE = (
        'Agent, environment, reward = -cost',
        'Discounted return',
    )
