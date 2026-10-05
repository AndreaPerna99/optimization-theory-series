"""Keep the Gradient - Episode 8, s02: Minimizing a sum

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SumProblem(PlaceholderScene):
    """Minimizing a sum"""

    EPISODE = 8
    SCENE_ID = 's02_sum_problem'
    TITLE = 'Minimizing a sum'
    PURPOSE = (
        'min sum_i f_i(x), f_i private to agent i',
        'All must agree on x',
    )
