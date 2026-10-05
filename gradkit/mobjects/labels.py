"""Keep the Gradient - Price Tags

A price tag hangs on a constraint and shows its shadow price, which is the
same number as its multiplier and its sensitivity (one colour for all three).
A slack constraint carries a tag reading zero, shown dimmed.
"""
from __future__ import annotations

from manim import MathTex, RoundedRectangle, VGroup

from gradkit import style


class PriceTag(VGroup):
    """A rounded tag showing a shadow price."""

    def __init__(self, value: float, symbol: str = r"\mu", decimals: int = 2) -> None:
        """Create the tag.

            Parameters
            ----------
            value : float
                The shadow price.
            symbol : str
                LaTeX symbol shown before the value, e.g. "\\mu_1".
            decimals : int
                Number of decimals shown.

            Returns
            -------
            None
        """
        text = MathTex(rf"{symbol} = {value:.{decimals}f}", font_size=style.CAPTION_SIZE,
                       color=style.MULTIPLIER)
        box = RoundedRectangle(corner_radius=0.12, width=text.width + 0.35,
                               height=text.height + 0.25, color=style.MULTIPLIER, stroke_width=2)
        box.move_to(text)
        super().__init__(box, text)
        if abs(value) < 10 ** (-decimals):
            self.set_opacity(0.45)
        self.value = value
