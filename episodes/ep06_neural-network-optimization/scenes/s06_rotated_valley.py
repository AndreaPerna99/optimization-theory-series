"""Keep the Gradient - Episode 6, s06: What adaptivity can't fix

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class RotatedValley(PlaceholderScene):
    """What adaptivity can't fix"""

    EPISODE = 6
    SCENE_ID = 's06_rotated_valley'
    TITLE = "What adaptivity can't fix"
    PURPOSE = (
        'Same valley rotated 45 degrees',
        "Adam's advantage disappears, momentum still helps",
    )
