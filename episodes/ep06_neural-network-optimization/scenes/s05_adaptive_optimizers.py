"""Keep the Gradient - Episode 6, s05: Momentum, RMSprop, Adam

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class AdaptiveOptimizers(PlaceholderScene):
    """Momentum, RMSprop, Adam"""

    EPISODE = 6
    SCENE_ID = 's05_adaptive_optimizers'
    TITLE = 'Momentum, RMSprop, Adam'
    PURPOSE = (
        "Built from Episode 1's momentum and step size",
        'Narrow valley: zigzag vs smooth vs rescaled',
    )
