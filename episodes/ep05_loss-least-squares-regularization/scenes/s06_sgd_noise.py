"""Keep the Gradient - Episode 5, s06: Stochastic gradient descent

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SgdNoise(PlaceholderScene):
    """Stochastic gradient descent"""

    EPISODE = 5
    SCENE_ID = 's06_sgd_noise'
    TITLE = 'Stochastic gradient descent'
    PURPOSE = (
        'Random minibatch: unbiased but noisy',
        'Constant step hovers; decreasing step settles',
    )
