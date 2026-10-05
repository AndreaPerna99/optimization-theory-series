"""Keep the Gradient - Episode 2, s05: When the optimum is an edge

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class EdgeOptimum(PlaceholderScene):
    """When the optimum is an edge"""

    EPISODE = 2
    SCENE_ID = 's05_edge_optimum'
    TITLE = 'When the optimum is an edge'
    PURPOSE = (
        'Objective rotates: vertex -> whole edge -> new vertex',
        'Convexity does not mean uniqueness',
    )
