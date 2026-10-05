"""Keep the Gradient - Episode 9, s05: Model predictive control

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Mpc(PlaceholderScene):
    """Model predictive control"""

    EPISODE = 9
    SCENE_ID = 's05_mpc'
    TITLE = 'Model predictive control'
    PURPOSE = (
        'Plan, apply the first input, re-plan',
        'Each step a QP (Episode 3)',
    )
