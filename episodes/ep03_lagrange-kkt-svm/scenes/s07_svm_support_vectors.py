"""Keep the Gradient - Episode 3, s07: Support vectors

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SvmSupportVectors(PlaceholderScene):
    """Support vectors"""

    EPISODE = 3
    SCENE_ID = 's07_svm_support_vectors'
    TITLE = 'Support vectors'
    PURPOSE = (
        'Points with mu_i > 0 light up',
        'Delete a non-support point: nothing moves',
        'Delete a support vector: the boundary moves',
    )
