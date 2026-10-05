"""Keep the Gradient - Episode 5, s05: Loss functions

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Losses(PlaceholderScene):
    """Loss functions"""

    EPISODE = 5
    SCENE_ID = 's05_losses'
    TITLE = 'Loss functions'
    PURPOSE = (
        'MSE for regression, cross-entropy for classification',
        'Convex for linear/logistic models, not for networks',
    )
