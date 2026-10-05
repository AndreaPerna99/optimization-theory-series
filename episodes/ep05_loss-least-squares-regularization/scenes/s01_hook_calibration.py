"""Keep the Gradient - Episode 5, s01: A camera calibrates itself

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class HookCalibration(PlaceholderScene):
    """A camera calibrates itself"""

    EPISODE = 5
    SCENE_ID = 's01_hook_calibration'
    TITLE = 'A camera calibrates itself'
    PURPOSE = (
        'Checkerboard, detected vs projected corners',
        'Calibration setup [CONFIRM]',
    )
