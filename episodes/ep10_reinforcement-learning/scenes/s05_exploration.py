"""Keep the Gradient - Episode 10, s05: Explore or exploit

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Exploration(PlaceholderScene):
    """Explore or exploit"""

    EPISODE = 10
    SCENE_ID = 's05_exploration'
    TITLE = 'Explore or exploit'
    PURPOSE = (
        'epsilon-greedy',
        'Never exploring: stuck on a mediocre route',
    )
