"""Keep the Gradient - Episode 4, s03: The envelope theorem

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class Envelope(PlaceholderScene):
    """The envelope theorem"""

    EPISODE = 4
    SCENE_ID = 's03_envelope'
    TITLE = 'The envelope theorem'
    PURPOSE = (
        'dp*/dtheta = dL/dtheta at the optimum',
        'No need to re-solve',
    )
