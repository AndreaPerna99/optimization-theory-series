"""Keep the Gradient - Episode 2, s07: Bumps and saddles

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Nonconvex(PlaceholderScene):
    """Bumps and saddles"""

    EPISODE = 2
    SCENE_ID = 's07_nonconvex'
    TITLE = 'Bumps and saddles'
    PURPOSE = (
        'Several local minima; different starts, different answers',
        'Saddle points',
    )
