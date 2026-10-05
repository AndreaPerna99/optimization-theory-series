"""Keep the Gradient - Episode 9, s04: LQR

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Lqr(PlaceholderScene):
    """LQR"""

    EPISODE = 9
    SCENE_ID = 's04_lqr'
    TITLE = 'LQR'
    PURPOSE = (
        'Optimal control is linear feedback u = -K x',
        'Q/R slider: aggressive vs gentle',
    )
