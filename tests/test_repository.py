"""Keep the Gradient - Checks of the Repository Structure

Every episode folder must validate (the same checks as ./kg check), and every
scene file must at least parse, so a broken manifest or scene is caught by the
test suite and not halfway through a render.
"""
from __future__ import annotations

import ast

from tools import episodes as eps


def test_there_are_thirteen_episodes_numbered_in_order():
    numbers = [eps.load(p).number for p in eps.all_paths()]
    assert numbers == list(range(13))


def test_every_episode_validates():
    problems = {p.name: eps.validate(eps.load(p)) for p in eps.all_paths()}
    assert not {k: v for k, v in problems.items() if v}


def test_every_scene_file_parses():
    for path in eps.all_paths():
        for f in sorted((path / "scenes").glob("*.py")):
            ast.parse(f.read_text(), filename=str(f))


def test_every_episode_has_its_production_files():
    for path in eps.all_paths():
        for name in ("README.md", "episode.toml", "narration.toml", "script.md"):
            assert (path / name).exists(), f"{path.name}/{name} is missing"
