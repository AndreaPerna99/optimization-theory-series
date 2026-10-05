"""Keep the Gradient - Episode 3, s06: SVM: the widest street

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class SvmMargin(PlaceholderScene):
    """SVM: the widest street"""

    EPISODE = 3
    SCENE_ID = 's06_svm_margin'
    TITLE = 'SVM: the widest street'
    PURPOSE = (
        'Two classes, maximum margin 2/||w||',
        'Constraints y_i (w^T x_i + w_0) >= 1',
    )
