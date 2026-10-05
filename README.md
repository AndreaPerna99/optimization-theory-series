# Keep the Gradient

**A Manim video series on optimization theory.** Thirteen episodes run from a single point feeling its way downhill, through limits, learning, cooperation and time, to systems that optimize without anyone in charge. The mathematics is the backbone; real projects (camera calibration, search-and-rescue robots, a quadrotor) show it working; and each episode closes with one or two sentences on what its mathematics says about improving when you can't see the whole landscape.

## Start Here

| If you want to... | Read |
|---|---|
| know what the series is trying to say | [MESSAGE.md](MESSAGE.md) |
| understand the series: idea, audience, rules, notation, visual language | [SERIES.md](SERIES.md) |
| know what one episode must contain | `episodes/epNN_*/README.md` (listed below) |
| build, render or narrate | [docs/PRODUCTION.md](docs/PRODUCTION.md) |
| work on this repository as an AI agent | [CLAUDE.md](CLAUDE.md) |
| see what is still undecided | [docs/OPEN_QUESTIONS.md](docs/OPEN_QUESTIONS.md) |
| check that nothing from the original plan was lost | [docs/COVERAGE.md](docs/COVERAGE.md) |
| read the original plan | [docs/source/](docs/source/) |

## Episodes

| Ep | Title |
|---|---|
| 0 | [Keep the Gradient (prologue)](episodes/ep00_keep-the-gradient/README.md) |
| 1 | [Which Way Is Down? Gradient Descent](episodes/ep01_gradient-descent/README.md) |
| 2 | [Corners and Bowls: Linear Programming and Convexity](episodes/ep02_linear-programming-convexity/README.md) |
| 3 | [Walls: Lagrange Multipliers, KKT and SVM](episodes/ep03_lagrange-kkt-svm/README.md) |
| 4 | [What If the World Changes? Sensitivity Analysis](episodes/ep04_sensitivity-analysis/README.md) |
| 5 | [Learning From Error: Loss, Least Squares and Regularization](episodes/ep05_loss-least-squares-regularization/README.md) |
| 6 | [Deep Landscapes: Neural Network Optimization](episodes/ep06_neural-network-optimization/README.md) |
| 7 | [Many Minds: Graphs and Consensus](episodes/ep07_graphs-consensus/README.md) |
| 8 | [Searching Together: Distributed Gradient Descent and SAR Robots](episodes/ep08_distributed-gd-sar/README.md) |
| 9 | [Planning Through Time: Optimal Control and the Quadrotor](episodes/ep09_optimal-control-quadrotor/README.md) |
| 10 | [Learning to Act: Reinforcement Learning](episodes/ep10_reinforcement-learning/README.md) |
| 11 | [Beyond Engineering: Economics, Fairness and Society](episodes/ep11_economics-fairness-society/README.md) |
| 12 | [Self-Organization and the Moving Optimum](episodes/ep12_self-organization-moving-optimum/README.md) |

Episode 1 is the pilot. The status of every episode (scenes, placeholders left, narration, open questions) is `./kg status`.

## Quick Start

```bash
# system: ffmpeg, LaTeX (texlive + dvisvgm), pango/cairo headers -- see docs/PRODUCTION.md
./tools/setup_env.sh            # one Python environment in .venv (add --tts for narration)
./kg status                     # where every episode stands
./kg check                      # validate every episode
./kg render 1 -q l              # draft-render Episode 1 (placeholders included)
./kg assemble 1 -q l            # join it into build/ep01/final/
.venv/bin/python -m pytest      # check the precise statements against the numerics
```

## Repository

| Path | Holds |
|---|---|
| [MESSAGE.md](MESSAGE.md) | the message of the series: its direction |
| [SERIES.md](SERIES.md) | the series bible |
| [episodes/](episodes/) | one folder per episode: specification, timeline, script, narration, scenes, assets |
| [gradkit/](gradkit/) | the shared scene library: style, LaTeX template, base scenes, recurring objects, algorithms |
| [tools/](tools/) | the `./kg` build tool: render, assemble, narrate, check, status |
| [tests/](tests/) | checks of the episodes' precise statements against `gradkit.algorithms` |
| [shared/](shared/) | brand, fonts, audio and footage used by several episodes |
| [docs/](docs/) | production guide, coverage checklist, open questions, assessment, original sources |
