# Production

How an episode goes from specification to published video, and the conventions that keep thirteen episodes consistent. *What* each episode says is in [SERIES.md](../SERIES.md) and the episode READMEs; this document covers *how* it is built.

## The Pipeline

Each episode moves through these stages. The current stage is the `status` field in its `episode.toml`; `./kg status` shows all of them.

| Status | Work | Done when |
|---|---|---|
| `planned` | specification exists in the episode README; scenes are placeholders | the README is reviewed and its [CONFIRM] items are answered |
| `scripting` | narration drafted in `script.md`, scene by scene; shot list refined | every scene has a narration draft and an on-screen plan |
| `animating` | placeholders replaced by real scenes, one at a time | `./kg status` shows 0 placeholders and a full draft assembles |
| `narrating` | final lines moved into `narration.toml` as timed segments; voice produced | `./kg narrate N --check-only` reports no problems |
| `review` | full-quality render, fact check against the precise statements, viewing | the review checklist below passes |
| `published` | uploaded | link recorded in the episode README |

A draft of the whole episode exists at every stage: placeholder cards stand in for unfinished scenes, so `./kg render N && ./kg assemble N` always produces a watchable rough cut with a realistic rhythm.

## Repository Layout

```text
optimization-theory-series/
├── README.md               start here
├── MESSAGE.md              the message of the series: its direction
├── SERIES.md               the series bible: idea, rules, notation, visual language, map
├── CLAUDE.md, AGENTS.md    instructions for AI agents working in the repository
├── docs/
│   ├── PRODUCTION.md       this file
│   ├── COVERAGE.md         every item of the original PDF -> its episode
│   ├── OPEN_QUESTIONS.md   decisions the author still has to make
│   ├── ASSESSMENT.md       why the project is worth doing, and its risks
│   └── source/             the original PDF and the archived single-file plan
├── episodes/
│   └── epNN_<slug>/
│       ├── README.md       the episode's specification (authoritative)
│       ├── episode.toml    metadata and the timeline (the cut)
│       ├── script.md       narration draft and shot list
│       ├── narration.toml  timed narration segments and the voice
│       ├── scenes/         one manim scene per file: s00_title.py, s01_*.py, ...
│       ├── assets/         footage/ and figures/ used only by this episode
│       └── takes/          recorded narration, one file per segment id
├── gradkit/                the shared scene library (style, LaTeX, scenes, mobjects, algorithms)
├── shared/                 brand, fonts, audio and footage used by several episodes
├── tools/                  the build tool behind ./kg
├── tests/                  checks of the precise statements against gradkit.algorithms
├── manim.cfg               render defaults (1920x1080, 60 fps, build/ as media dir)
├── pyproject.toml          the single Python environment
└── build/                  everything generated (not versioned)
```

## Environment

One environment for everything (the previous project needed two because manim's numpy clashed with a research environment; this project has no such constraint).

System packages (Ubuntu/Debian):

```bash
sudo apt install -y ffmpeg texlive texlive-latex-extra dvisvgm libpango1.0-dev libcairo2-dev pkg-config
```

Python environment:

```bash
./tools/setup_env.sh          # creates .venv with manim, numpy, scipy and pytest
./tools/setup_env.sh --tts    # also installs piper-tts and kokoro-onnx
```

`./kg` runs with `.venv/bin/python`; set `KG_PYTHON=/path/to/python` to use another interpreter.

## The `kg` Tool

| Command | Does |
|---|---|
| `./kg status` | one line per episode: status, scenes, placeholders left, clips, narration segments, open [CONFIRM] items |
| `./kg check [N]` | validates manifests, scene files and classes, clips and narration; nonzero exit on any problem |
| `./kg render N [-q l\|m\|h\|k] [--only Class ...]` | renders the timeline's scenes into `build/epNN/videos/` |
| `./kg assemble N [-q ...] [--copy]` | joins scenes and clips in timeline order into `build/epNN/final/`, and writes the timeline offsets |
| `./kg narrate N [-q ...] [--check-only]` | synthesises every segment, reports budget, overrun and overlap problems, and muxes the narration |
| `./kg new-scene N sNN_name --title "..." [--purpose "..."]` | creates a placeholder scene and appends it to the timeline |

Qualities: `l` 480p15 (drafts, default), `m` 720p30, `h` 1080p60 (release), `k` 2160p60. Renders of different qualities coexist; every command selects its quality explicitly, never "whatever file is found first".

`python -m pytest` runs the tests; run it after touching `gradkit/algorithms` or a precise statement.

## Scenes

- **One scene per file**, named `sNN_snake_case.py` with one class `CamelCase` (e.g. `s05_step_size.py` → `StepSize`). `s00_title.py` → `Title` opens every episode. Use letter suffixes (`s05b_...`) to insert a scene without renumbering.
- **Start as a placeholder.** A new scene derives from `PlaceholderScene` with the purpose from the README. It becomes real by deriving from `SeriesScene` (or `SeriesThreeDScene`) and writing `construct()`.
- **Keep scenes short** (roughly 20–90 s). Narration is timed per scene, so short scenes keep every retiming local.
- **Compute, don't draw.** Every iterate, trajectory, value or boundary comes from `gradkit.algorithms`, with fixed seeds, so renders are reproducible and correct by construction. If an algorithm is missing, add it there with a test, not inside the scene.
- **No private helpers.** Anything a second scene could use goes into `gradkit` (mobjects, layout helpers). Scene files contain only the scene.
- **Colours by role.** Only `gradkit.style` constants, chosen by meaning (`ITERATE`, `MULTIPLIER`, `FEASIBLE`, ...), never raw colour values in a scene.
- **Math through the template.** `MathTex` uses the series template automatically; use its macros (`\R`, `\argmin`, `\T`, `\opt`, `\Lag`, ...) and the notation table in SERIES.md.
- **Header.** Each file starts with a docstring `Keep the Gradient - Episode N, sNN: Title` and a short description of what the scene shows; functions use the numpy-style docstrings found throughout `gradkit`.

## Narration

The narration lives in `narration.toml`, in segments pinned to timeline entries. A segment's `at` is measured from the start of **its own entry**, and `./kg assemble` records where every entry starts. That fixes the main problem of the previous video, where cues were absolute timestamps and any change to one scene shifted every later line.

Workflow:

1. Draft the lines in `script.md` while the scene is designed.
2. Once the scene renders, move the final lines into `narration.toml` with `entry`, `at` and `budget`.
3. `./kg narrate N --check-only` synthesises the lines and reports any that run over budget, past their scene, or into the next line.
4. Adjust the text or the timing, then `./kg narrate N` to mux.

Engines (`[voice] engine`): `piper` and `kokoro` (local TTS), or `takes` (recorded files `takes/<segment id>.wav`, for the author's own voice or exports from a commercial TTS). Audio is keyed by segment **id**, never by position, and the output folder is wiped before each run, so two voices or two versions of a line can never be mixed into one track.

Rules learned on the previous video:

- Pin `at` to a **picture beat** (the moment an animation plays), not the moment a caption appears.
- **Never split one sentence across two segments**: each segment is synthesised separately, so the join sounds like a hard stop.
- **Commas change TTS pause length** (in Piper about 0.25 s with a comma, 0.1 s without); listen to a line in the engine before timing it.
- Pin the voice in `narration.toml`; never rely on a default that could change silently.
- For Piper, `noise_w = 0` makes line durations reproducible between builds.
- The narration track is padded half a second past the picture so `-shortest` never cuts the last frames (handled by `tools/media.py`).

## Footage and Large Files

Video footage, recorded takes and TTS models are **not versioned** in git (see `.gitignore`); only the folders and their README files are. Keep the master copies outside the repository (see [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md), question 8) and copy them in before building.

- Footage used by one episode: `episodes/epNN_*/assets/footage/`, referenced in the timeline as `clip = "assets/footage/name.mp4"`.
- Footage used by several episodes (e.g. the quadrotor in Episodes 0 and 9): `shared/footage/`, referenced as `clip = "../../shared/footage/name.mp4"`.
- Clips may arrive in any format; `./kg assemble` re-encodes them to the episode's resolution and frame rate (cached in `build/`).
- Small source figures (SVG, PNG) may be versioned under `assets/figures/`.

## Review Checklist

Before an episode moves to `published`:

- [ ] Every claim on screen or in narration matches a precise statement in the episode README, **with its conditions**.
- [ ] Symbols follow the notation table in SERIES.md; colours follow the visual language.
- [ ] No **[CONFIRM]** marker remains for any content that is actually used.
- [ ] No project fact (number, result, capability, footage) appears that the author has not confirmed.
- [ ] The closing line is at most two sentences, comes after the mathematics, and passes the test in [MESSAGE.md](../MESSAGE.md).
- [ ] `python -m pytest` passes; `./kg check N` passes; `./kg narrate N -q h --check-only` reports no problems.
- [ ] A full 1080p60 render has been watched end to end.
- [ ] [COVERAGE.md](COVERAGE.md) still matches the episode's content.

## Release Order

Episode 1 first, as the pilot: it fixes the visual language (the ball, the landscape, the step), the palette and the production pipeline, and it is where `ContourMap` and `Landscape3D` get implemented. Then Episode 0 as a short trailer, once the look of the series is settled. Then Episodes 2–4, the foundation everything else depends on. Episode 8 (SAR) is probably the most shareable, so it is worth reaching early. Episodes may differ in length.

## Lessons From the Previous Video

The paper video (manim 0.21, Piper/Kokoro/ElevenLabs narration) is the starting point. What it got right is kept: a style module with colours by role, render and assembly driven by a list, the per-segment narration pipeline with budget checks, and animations computed from the real mathematics. Its pain points are designed out:

| Previous pain point | Here |
|---|---|
| Narration cues were absolute timestamps; changing one scene shifted all later lines | cues are relative to their own timeline entry |
| Whole scene folders and the compositor were copied for each cut, then drifted | one scene library per episode; a cut is a timeline in `episode.toml` |
| Helpers duplicated in every scene file | shared `gradkit` library |
| Audio files keyed by index once mixed two voices | keyed by segment id; output wiped every run |
| The voice fell back silently to a default | voice pinned in `narration.toml`, required for TTS engines |
| Default LaTeX, no macros | one series template with notation macros (`gradkit/tex.py`) |
| Two virtual environments | one environment (`pyproject.toml`) |
| Scripts silently did the wrong thing without a flag | `./kg check` validates before every build; failures stop with a message |
