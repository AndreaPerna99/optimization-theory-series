"""Keep the Gradient - Episode 1, s08: Respecting constraints

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class ProjectedPreview(PlaceholderScene):
    """Respecting constraints"""

    EPISODE = 1
    SCENE_ID = 's08_projected_preview'
    TITLE = 'Respecting constraints'
    PURPOSE = (
        'Projected gradient descent: step, then project',
        'Preview of linear programming and duality',
    )
