"""Keep the Gradient - Episode 1, s03: The gradient

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Gradient(PlaceholderScene):
    """The gradient"""

    EPISODE = 1
    SCENE_ID = 's03_gradient'
    TITLE = 'The gradient'
    PURPOSE = (
        'Partial derivatives as a vector',
        'Steepest ascent (Cauchy-Schwarz), perpendicular to level curves',
        '3D landscape and contour map side by side',
    )
