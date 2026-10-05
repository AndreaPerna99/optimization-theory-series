"""Keep the Gradient - Episode 5, s09: Regularization is a constraint

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class ConstraintInDisguise(PlaceholderScene):
    """Regularization is a constraint"""

    EPISODE = 5
    SCENE_ID = 's09_constraint_in_disguise'
    TITLE = 'Regularization is a constraint'
    PURPOSE = (
        'Penalty = constraint with multiplier lambda',
        'Diamond corners give exact zeros',
    )
