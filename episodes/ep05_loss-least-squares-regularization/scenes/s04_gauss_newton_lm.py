"""Keep the Gradient - Episode 5, s04: Gauss-Newton and Levenberg-Marquardt

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class GaussNewtonLm(PlaceholderScene):
    """Gauss-Newton and Levenberg-Marquardt"""

    EPISODE = 5
    SCENE_ID = 's04_gauss_newton_lm'
    TITLE = 'Gauss-Newton and Levenberg-Marquardt'
    PURPOSE = (
        '(J^T J + rho I) Delta = -J^T r',
        'Residual arrows shrinking, image straightening',
        'Zhang: closed-form start, then LM; start matters',
    )
