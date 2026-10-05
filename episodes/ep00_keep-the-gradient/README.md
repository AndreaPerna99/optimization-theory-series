# Episode 0 · Keep the Gradient

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 6–8 min |
| From the original PDF | Video 0 |
| Watch first | none |
| Anchor | quadrotor cold open (footage to confirm) |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** What do a navigation app, a hospital schedule, a trained AI model and a flying drone have in common?

**Technical content.**
- Optimization as finding the best possible solution within given constraints: improving efficiency, maximizing productivity, or reaching a target with a limited budget or limited resources.
- The three ingredients of every problem: **decision variables** (what you can change), an **objective** (what "better" means), and **constraints** (what you cannot violate). Each example below is shown with these three labelled on screen.
- Why it matters: a fundamental approach to problem-solving across engineering, economics, AI and the social sciences, from businesses maximizing profit to researchers building predictive models.
- Everyday examples: a **navigation app** finding the fastest route; **household budgeting**, distributing income across expenses to maximize savings or cover essential needs.
- Professional examples, hinting at the series' depth: **hospitals** allocating limited staff and equipment; **AI models** trained by minimizing their error.
- Series preview: a building-block structure from fundamental tools to complex applications (gradient descent, constrained optimization, machine learning, distributed optimization, control, interdisciplinary applications), with a practical example in every episode.
- What viewers will gain: an understanding of optimization that applies across fields and in everyday life; the point that optimization is not only for engineers and mathematicians, but also shapes natural systems and social structures; and an invitation to look for optimization problems in their own lives and work.

**Precise statements.**
- Route finding is optimization over a *discrete* set (paths in a road graph), solved by graph-search algorithms such as Dijkstra's or A\*, not by gradient descent. Say so in one line ("not every optimization problem is a landscape you can roll down; this series focuses on the ones that are, plus the tools they share with the rest").

**Key visuals.** The series map drawn as a landscape, each episode a location the ball will visit. The three ingredients appearing as labels over each example.

**Project.** Cold open on the quadrotor with the line "this machine is solving an optimization problem many times per second." **[CONFIRM]** that this matches what the controller actually does (e.g. MPC running onboard), and the real rate, before using the line.

**Corrections.** Keep it short. A long "why optimization matters" video from a new channel loses viewers, so this is a trailer with substance. The series preview and the "think broadly" invitation are woven in visually rather than listed.

**Closing line.** You never see the whole landscape, only the slope beneath your feet. That is enough to start.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_cold_open.py` | `ColdOpen` | **Cold open: the quadrotor.** Quadrotor footage (confirm); Line: this machine solves an optimization problem many times per second; Only if the controller really does (confirm) |
| 2 | `s02_three_ingredients.py` | `ThreeIngredients` | **Variables, objective, constraints.** Optimization: the best solution within constraints; Decision variables, objective, constraints labelled; Efficiency, productivity, targets on a budget |
| 3 | `s03_everyday_examples.py` | `EverydayExamples` | **Everyday optimization.** Navigation app: fastest route (discrete: graph search, not GD); Household budgeting: income across expenses; Three ingredients shown on each |
| 4 | `s04_professional_examples.py` | `ProfessionalExamples` | **Optimization at work.** Hospitals allocating staff and equipment; AI models trained by minimizing error; Businesses (profit) and researchers (predictive models) |
| 5 | `s05_series_map.py` | `SeriesMap` | **The series map.** Landscape map, one location per episode; Building blocks and practical examples in every episode; Not only engineering: natural and social systems too |
| 6 | `s06_closing.py` | `Closing` | **Keep the gradient.** Motto: you only see the slope beneath your feet; Invitation to find optimization in your own life and work; Closing line |

### Files

| Path | Holds |
|---|---|
| [episode.toml](episode.toml) | metadata and the timeline (the cut) |
| [script.md](script.md) | narration draft and shot list, scene by scene |
| [narration.toml](narration.toml) | final narration as timed segments |
| [scenes/](scenes/) | one manim scene per file |
| `assets/footage/` | video clips for this episode (not versioned; see [docs/PRODUCTION.md](../../docs/PRODUCTION.md)) |
| `assets/figures/` | still images and plots for this episode |
| `takes/` | recorded narration, one file per segment id, when the engine is `takes` |

### Build

```bash
./kg check 0                     # validate manifest, scenes and narration
./kg render 0 -q l               # draft render (480p15); -q h for release
./kg assemble 0 -q l             # join the timeline into one video
./kg narrate 0 -q l --check-only # synthesise narration and check timing
```
