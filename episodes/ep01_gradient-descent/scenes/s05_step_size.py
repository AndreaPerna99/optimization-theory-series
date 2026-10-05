"""Keep the Gradient - Episode 1, s05: The step-size threshold

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class StepSize(PlaceholderScene):
    """The step-size threshold"""

    EPISODE = 1
    SCENE_ID = 's05_step_size'
    TITLE = 'The step-size threshold'
    PURPOSE = (
        'Slider on alpha: converge, oscillate, explode',
        'Threshold 2 / lambda_max(H)',
        'Small steps: slower, not more precise',
    )
