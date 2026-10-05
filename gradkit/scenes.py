"""Keep the Gradient - Base Scenes

Every scene in the series derives from one of these classes:

- ``SeriesScene`` / ``SeriesThreeDScene``: an ordinary 2D or 3D scene with
  the series style applied.
- ``EpisodeTitle``: the opening title card, configured by two class attributes.
- ``PlaceholderScene``: a card that states what the scene WILL show. Every
  planned scene starts as one, so the whole episode renders and assembles
  end to end before any animation exists. A scene is replaced by changing its
  base class to ``SeriesScene`` and writing ``construct``.
"""
from __future__ import annotations

from manim import (DOWN, LEFT, UP, FadeIn, FadeOut, Line, Scene, Text,
                   ThreeDScene, VGroup, config)

from gradkit import style

style.apply()

SERIES_NAME = "Keep the Gradient"


def fit_width(mob, width: float | None = None):
    """Scale a mobject down, never up, so it fits inside the safe width.

        Parameters
        ----------
        mob : Mobject
            The mobject to fit.
        width : float, optional
            Maximum width in frame units. Defaults to the frame minus margins.

        Returns
        -------
        Mobject
            The same mobject, for chaining.
    """
    limit = width if width is not None else config.frame_width - 2 * style.MARGIN
    if mob.width > limit:
        mob.scale_to_fit_width(limit)
    return mob


class SeriesScene(Scene):
    """A 2D scene with the series style applied."""


class SeriesThreeDScene(ThreeDScene):
    """A 3D scene (landscapes, surfaces) with the series style applied."""


class EpisodeTitle(SeriesScene):
    """The opening title card. Subclasses set ``EPISODE`` and ``TITLE``."""

    EPISODE: int = 0
    TITLE: str = ""
    HOLD: float = 3.0

    def construct(self) -> None:
        """Play the title card.

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        series = Text(SERIES_NAME.upper(), font_size=style.NOTE_SIZE, color=style.MUTED)
        number = Text(f"Episode {self.EPISODE}", font_size=style.CAPTION_SIZE, color=style.ITERATE)
        title = fit_width(Text(self.TITLE, font_size=style.TITLE_SIZE))
        card = VGroup(series, number, title).arrange(DOWN, buff=0.35)
        self.play(FadeIn(card, shift=UP * 0.15), run_time=style.FADE * 1.5)
        self.wait(self.HOLD)
        self.play(FadeOut(card), run_time=style.FADE)


class PlaceholderScene(SeriesScene):
    """A stand-in card describing a planned scene.

    Subclasses set ``EPISODE``, ``SCENE_ID``, ``TITLE`` and ``PURPOSE`` (what
    the finished scene must show, taken from the episode README). The card
    lasts about ``HOLD`` seconds, so draft assemblies have a realistic rhythm.
    """

    EPISODE: int = 0
    SCENE_ID: str = ""
    TITLE: str = ""
    PURPOSE: tuple[str, ...] = ()
    HOLD: float = 3.0

    def construct(self) -> None:
        """Play the placeholder card.

            Parameters
            ----------
            None

            Returns
            -------
            None
        """
        tag = Text(f"PLACEHOLDER  ·  Ep {self.EPISODE:02d}  ·  {self.SCENE_ID}",
                   font_size=style.NOTE_SIZE, color=style.DIVERGE)
        title = fit_width(Text(self.TITLE, font_size=style.HEADING_SIZE, color=style.ITERATE))
        rule = Line(LEFT * 3, LEFT * -3, color=style.GRID)
        items = VGroup(*[fit_width(Text(f"•  {p}", font_size=style.NOTE_SIZE))
                         for p in self.PURPOSE]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        card = VGroup(tag, title, rule, items).arrange(DOWN, buff=0.4)
        if card.height > config.frame_height - 2 * style.MARGIN:
            card.scale_to_fit_height(config.frame_height - 2 * style.MARGIN)
        self.play(FadeIn(card), run_time=style.FADE)
        self.wait(self.HOLD)
        self.play(FadeOut(card), run_time=style.FADE)
