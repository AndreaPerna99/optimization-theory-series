"""Keep the Gradient - Episode 5, s08: Ridge and Lasso

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class RidgeLasso(PlaceholderScene):
    """Ridge and Lasso"""

    EPISODE = 5
    SCENE_ID = 's08_ridge_lasso'
    TITLE = 'Ridge and Lasso'
    PURPOSE = (
        'Penalties lambda ||w||_2^2 and lambda ||w||_1',
        'Shrinkage vs sparsity',
    )
