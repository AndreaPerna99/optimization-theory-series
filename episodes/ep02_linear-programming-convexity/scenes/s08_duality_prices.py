"""Keep the Gradient - Episode 2, s08: Duality and shadow prices

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class DualityPrices(PlaceholderScene):
    """Duality and shadow prices"""

    EPISODE = 2
    SCENE_ID = 's08_duality_prices'
    TITLE = 'Duality and shadow prices'
    PURPOSE = (
        'The dual problem as a bound',
        'Strong duality and complementary slackness',
        'Price tags on binding constraints, zero on slack',
    )
