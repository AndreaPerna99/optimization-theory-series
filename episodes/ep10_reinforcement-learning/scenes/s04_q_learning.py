"""Keep the Gradient - Episode 10, s04: Q-learning in a grid world

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class QLearning(PlaceholderScene):
    """Q-learning in a grid world"""

    EPISODE = 10
    SCENE_ID = 's04_q_learning'
    TITLE = 'Q-learning in a grid world'
    PURPOSE = (
        'Values spreading back from the goal',
        'The update is a stochastic step (SGD callback)',
    )
