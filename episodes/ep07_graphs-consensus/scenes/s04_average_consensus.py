"""Keep the Gradient - Episode 7, s04: Average consensus

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class AverageConsensus(PlaceholderScene):
    """Average consensus"""

    EPISODE = 7
    SCENE_ID = 's04_average_consensus'
    TITLE = 'Average consensus'
    PURPOSE = (
        'Values averaging step by step',
        'Each agent uses neighbours only; the average is invariant',
    )
