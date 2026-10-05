"""Keep the Gradient - Episode 4, s07: Sensitivity of a trajectory

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class TrajectorySensitivity(PlaceholderScene):
    """Sensitivity of a trajectory"""

    EPISODE = 4
    SCENE_ID = 's07_trajectory_sensitivity'
    TITLE = 'Sensitivity of a trajectory'
    PURPOSE = (
        "S' = (dF/dx) S + dF/dp",
        'Toy robot, uncertain wheel radius: two plans, two clouds',
        'First order: small perturbations only',
    )
