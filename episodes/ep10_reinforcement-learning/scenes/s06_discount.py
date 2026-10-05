"""Keep the Gradient - Episode 10, s06: Patience is a parameter

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Discount(PlaceholderScene):
    """Patience is a parameter"""

    EPISODE = 10
    SCENE_ID = 's06_discount'
    TITLE = 'Patience is a parameter'
    PURPOSE = (
        'Short-sighted vs patient agent',
        'Horizon about 1/(1 - gamma)',
    )
