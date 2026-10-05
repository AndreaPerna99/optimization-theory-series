# Instructions for AI Agents

This repository produces **Keep the Gradient**, a Manim video series on optimization theory. Agents write scripts, scenes and narration from a written specification. Accuracy matters more than speed: a wrong claim in a published video can't be patched.

## Read Before Working

1. [MESSAGE.md](MESSAGE.md): what the series is trying to say; every closing line, title and description must pass its test.
2. [SERIES.md](SERIES.md): the rules, the audience, the **notation table** and the **visual language**.
3. The README of the episode you are working on (`episodes/epNN_*/README.md`): its specification, especially **Precise statements**, **Key visuals** and **Corrections**.
4. [docs/PRODUCTION.md](docs/PRODUCTION.md): the pipeline and the scene conventions.

## Hard Rules

- **The specification is authoritative.** If what you are asked to build contradicts SERIES.md or the episode README, stop and say so; do not resolve it silently. A specification change comes first, in its own edit, and is reported to the author.
- **Precise statements keep their conditions.** Narration may simplify wording, never drop a condition (e.g. "convex ⇒ unique minimum" is false; it needs strict convexity).
- **Never invent project facts.** Anything about the author's projects (quadrotor, SAR robots, calibration setup, research) that the specification does not state is marked **[CONFIRM]**. Ask; never fill it in with plausible numbers, results, capabilities or footage descriptions.
- **Compute, don't draw.** Everything a scene shows comes from `gradkit.algorithms`, with fixed seeds. A missing algorithm is added there with a test in `tests/`, not inside a scene.
- **Use the shared library.** Colours only from `gradkit.style` roles; recurring objects from `gradkit.mobjects`; math through the series LaTeX template and its macros. No private helpers in scene files.
- **Notation is global.** Use the symbols of the notation table; never introduce a new symbol for an existing object.
- **The closing line** is at most two sentences, after the mathematics, and passes the test in [MESSAGE.md](MESSAGE.md).

## Common Tasks

| Task | Steps |
|---|---|
| Build a scene | read the README spec; replace the placeholder base class with `SeriesScene`; compute with `gradkit.algorithms`; `./kg render N --only ClassName -q l`; look at the frames |
| Add a scene | `./kg new-scene N sNN_name --title "..." --purpose "..." [--purpose "..."]`, then move its timeline entry to the right place in `episode.toml` |
| Write narration | draft in `script.md`; when the scene renders, add timed segments to `narration.toml`; `./kg narrate N --check-only` |
| Change episode content | edit the episode README first, then [docs/COVERAGE.md](docs/COVERAGE.md) if PDF items moved, then the material |
| Add or change an algorithm | edit `gradkit/algorithms`, add or update a test, run `python -m pytest` |

## Before You Report Done

- `./kg check` passes, and `python -m pytest` passes if `gradkit` changed.
- Rendered scenes were actually looked at (frames or video), not only rendered without errors.
- Report any **[CONFIRM]** item you ran into and any place where the specification seemed wrong.
