"""Keep the Gradient - File Templates

The text of new scene files. ``kg new-scene`` uses these, so every scene file
in the series starts from the same shape.
"""
from __future__ import annotations

import re


def class_name(scene_id: str) -> str:
    """CamelCase class name from a scene id, e.g. s05_step_size -> StepSize.

        Parameters
        ----------
        scene_id : str
            Scene id of the form sNN_words.

        Returns
        -------
        str
            The class name.
    """
    m = re.fullmatch(r"s\d{2}[a-z]?_([a-z0-9_]+)", scene_id)
    if not m:
        raise ValueError(f"scene id {scene_id!r} must look like s05_step_size")
    return "".join(w.capitalize() for w in m.group(1).split("_"))


def title_scene(number: int, title: str) -> str:
    """Source of an episode's s00_title.py."""
    return f'''"""Keep the Gradient - Episode {number}, s00: Title Card"""
from __future__ import annotations

from gradkit.scenes import EpisodeTitle


class Title(EpisodeTitle):
    """Opening title card."""

    EPISODE = {number}
    TITLE = {title!r}
'''


def placeholder_scene(number: int, scene_id: str, title: str, purpose: list[str]) -> str:
    """Source of a placeholder scene file.

        Parameters
        ----------
        number : int
            Episode number.
        scene_id : str
            Scene id, e.g. s05_step_size.
        title : str
            Short human title of the scene.
        purpose : list of str
            What the finished scene must show (from the episode README).

        Returns
        -------
        str
            Python source of the scene file.
    """
    cls = class_name(scene_id)
    items = "\n".join(f"        {p!r}," for p in purpose) or "        'TODO: describe what this scene shows',"
    return f'''"""Keep the Gradient - Episode {number}, {scene_id.split("_")[0]}: {title}

PLACEHOLDER. Spec: the episode README (section "Specification", in particular
"Key visuals" and "Precise statements"). To build the real scene: derive from
SeriesScene (or SeriesThreeDScene), write construct(), compute everything
shown with gradkit.algorithms, and use gradkit.style roles for colour.
"""
from __future__ import annotations

from gradkit.scenes import PlaceholderScene


class {cls}(PlaceholderScene):
    """{title}"""

    EPISODE = {number}
    SCENE_ID = {scene_id!r}
    TITLE = {title!r}
    PURPOSE = (
{items}
    )
'''
