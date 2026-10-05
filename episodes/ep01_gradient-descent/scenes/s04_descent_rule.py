"""Keep the Gradient - Episode 1, s04: The descent rule

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class DescentRule(PlaceholderScene):
    """The descent rule"""

    EPISODE = 1
    SCENE_ID = 's04_descent_rule'
    TITLE = 'The descent rule'
    PURPOSE = (
        'x_{k+1} = x_k - alpha grad f(x_k), term by term',
        'Iterates refining step by step on the landscape',
        'Examples: predicting prices, MSE of a forecast',
    )
