"""Keep the Gradient - Episode 1, s06: The narrow valley

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class IllConditioning(PlaceholderScene):
    """The narrow valley"""

    EPISODE = 1
    SCENE_ID = 's06_ill_conditioning'
    TITLE = 'The narrow valley'
    PURPOSE = (
        'Zigzag in an elongated bowl',
        'Condition number kappa on screen',
        'Rate (kappa - 1)/(kappa + 1)',
    )
