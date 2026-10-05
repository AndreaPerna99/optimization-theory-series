"""Keep the Gradient - Episode 6, s03: Vanishing and exploding gradients

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class VanishingExploding(PlaceholderScene):
    """Vanishing and exploding gradients"""

    EPISODE = 6
    SCENE_ID = 's03_vanishing_exploding'
    TITLE = 'Vanishing and exploding gradients'
    PURPOSE = (
        'Product of Jacobians through depth',
        'Signal bars shrinking or exploding per layer',
    )
