"""Keep the Gradient - Episode 6, s04: Keeping the signal alive

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Remedies(PlaceholderScene):
    """Keeping the signal alive"""

    EPISODE = 6
    SCENE_ID = 's04_remedies'
    TITLE = 'Keeping the signal alive'
    PURPOSE = (
        'ReLU, Xavier/He initialization, normalization',
        'Residual connections, gradient clipping',
    )
