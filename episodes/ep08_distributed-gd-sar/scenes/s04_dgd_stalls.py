"""Keep the Gradient - Episode 8, s04: Why DGD stalls

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class DgdStalls(PlaceholderScene):
    """Why DGD stalls"""

    EPISODE = 8
    SCENE_ID = 's04_dgd_stalls'
    TITLE = 'Why DGD stalls'
    PURPOSE = (
        'Local gradients nonzero at the optimum',
        'Constant step: only a neighbourhood',
    )
