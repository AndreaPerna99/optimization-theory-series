"""Keep the Gradient - Episode 1, s02: Objectives and constraints

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class ObjectiveConstraints(PlaceholderScene):
    """Objectives and constraints"""

    EPISODE = 1
    SCENE_ID = 's02_objective_constraints'
    TITLE = 'Objectives and constraints'
    PURPOSE = (
        'Objective: minimize error / maximize profit',
        'Constraints: a budget cap',
        '2D feasible region from budget or time limits',
    )
