"""Keep the Gradient - Episode 3, s04: KKT as force balance

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class KktForceBalance(PlaceholderScene):
    """KKT as force balance"""

    EPISODE = 3
    SCENE_ID = 's04_kkt_force_balance'
    TITLE = 'KKT as force balance'
    PURPOSE = (
        'Downhill pull balanced by the wall force mu',
        'Walls push, never pull: mu >= 0',
        'When KKT is necessary, when sufficient',
    )
