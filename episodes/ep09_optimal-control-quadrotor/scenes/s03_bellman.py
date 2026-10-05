"""Keep the Gradient - Episode 9, s03: The Bellman principle

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Bellman(PlaceholderScene):
    """The Bellman principle"""

    EPISODE = 9
    SCENE_ID = 's03_bellman'
    TITLE = 'The Bellman principle'
    PURPOSE = (
        'Cost now + value of where you land',
        'Backward sweep over a grid of states',
    )
