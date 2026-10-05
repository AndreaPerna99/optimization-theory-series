# Episode 4 · What If the World Changes? Sensitivity Analysis

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 15–20 min |
| From the original PDF | Video 3, second half |
| Watch first | [Ep 3](../ep03_lagrange-kkt-svm/README.md) |
| Anchor | beam or truss, budgeting, robot toy model |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** You have found the best plan. Then the budget changes, a price moves, a measurement was slightly wrong. How much does your best plan change, and can you know in advance?

**Technical content.**
- **Purpose of sensitivity analysis:** assessing how robust an optimal solution is when constraints or parameters change, and how adaptable it is across scenarios.
- **Decision-making applications** from the PDF: budgeting, supply-chain management, and any field where conditions change over time.
- **Multipliers as derivatives:** the multipliers of Episodes 2 and 3 already measure sensitivity. They are the rate at which the optimal value changes when a constraint is loosened.
- **How the solution moves:** smoothly while the set of active constraints stays the same; with a kink when a constraint becomes active or inactive; and with a sudden jump when two candidate optima trade places.
- **Sensitivity of a trajectory,** briefly: when the solution is a path over time (a robot's motion), the same question becomes "how much does the path move if a physical parameter is slightly wrong?" This sets up control (Ep 9) and robustness.
- **Examples as anchors** from the PDF: mechanical engineering (constrained optimization uses material efficiently while maintaining structural integrity; a beam or truss under changing loads); financial planning (reallocating resources dynamically as market conditions fluctuate).
- **Recap** of KKT and sensitivity together: KKT is how you recognize the optimum; sensitivity is how you know how fragile it is.
- **Preview:** machine learning, where cost functions, regularization and training challenges take over.

**Precise statements.**
- *Multiplier = sensitivity.* Let $p^\star(u)$ be the optimal value of: minimize $f(x)$ subject to $g_i(x) \le u_i$. Under standard regularity conditions (linearly independent active constraint gradients, strict complementarity, second-order sufficiency), $\dfrac{\partial p^\star}{\partial u_i} = -\mu_i^\star$. Loosening an active constraint by $\delta$ lowers the optimal cost by about $\mu_i^\star \delta$; loosening an inactive one changes nothing.
- *General form (envelope theorem).* If the problem depends on a parameter $\theta$, then $\dfrac{d p^\star}{d\theta} = \dfrac{\partial \mathcal{L}}{\partial \theta}\Big|_{(x^\star, \lambda^\star, \mu^\star)}$ under the same conditions: you don't need to re-solve the problem to know how fast its optimum changes.
- *How the solution moves.* Under those conditions, $x^\star$ depends smoothly on the parameters (implicit function theorem applied to the KKT system). In strictly convex quadratic programs with linear constraints and a changing right-hand side, the solution path is **continuous and piecewise linear**, with kinks where the active set changes. **Jumps** happen in other situations: in an LP when the objective direction changes and the optimal vertex switches (with a tie at the switching moment), and in non-convex problems when the global minimum moves from one valley to another. Do not say that a constraint becoming active makes the solution jump.
- *Trajectory sensitivity.* For a system $\dot x = F(x, p)$, the sensitivity $S(t) = \partial x(t)/\partial p$ satisfies $\dot S = \dfrac{\partial F}{\partial x} S + \dfrac{\partial F}{\partial p}$, with $S(0) = \partial x(0)/\partial p$. To first order, $x(t; p + \delta p) \approx x(t; p) + S(t)\,\delta p$. This is valid only for small $\delta p$; say so.

**Key visuals.**
- A 2D constrained problem whose constraint slides: the optimum glides along the wall, the optimal value's curve has slope $-\mu$, and the multiplier arrow's length matches that slope.
- The kink: the solution path bending when a new wall becomes active.
- The jump: a tilting double-well where the global minimum suddenly switches valleys.
- A beam or truss with a changing load, the optimal design shifting with it.
- A simple robot (a toy model, not a project claim) with an uncertain wheel radius: two plans reach the same nominal goal, but a cloud of perturbed runs shows one is much more sensitive than the other.

**Project.** Sensitivity is a theory chapter, not a research chapter. If the author's own sensitivity work is used, it is at most one short example of trajectory sensitivity (e.g. a few seconds of footage of a robot fleet whose plan was chosen to reduce sensitivity), clearly labelled as an example. **[CONFIRM]** whether to include it at all, and that it is publicly shareable.

**Corrections.** The PDF frames sensitivity mainly as "robustness to changing constraints". The mathematical core it doesn't mention is that sensitivity is already contained in the multipliers; that makes the episode the payoff of Episodes 2–3 rather than a new, separate topic.

**Callbacks.** Shadow prices (2) and wall forces (3) become derivatives. Forward: robustness in control (9).

**Closing line.** Finding a good answer is half the problem. Knowing how fragile it is when the world shifts is the other half.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_world_changes.py` | `HookWorldChanges` | **The world changes.** The best plan, then the budget moves; How much does the optimum change? |
| 2 | `s02_multiplier_derivative.py` | `MultiplierDerivative` | **The multiplier is a derivative.** Sliding constraint, optimum gliding along the wall; Slope of the optimal value = -mu |
| 3 | `s03_envelope.py` | `Envelope` | **The envelope theorem.** dp*/dtheta = dL/dtheta at the optimum; No need to re-solve |
| 4 | `s04_kinks.py` | `Kinks` | **Kinks.** Solution path bends when the active set changes; Strictly convex QP: continuous, piecewise linear |
| 5 | `s05_jumps.py` | `Jumps` | **Jumps.** LP vertex switch as the objective turns; Tilting double-well: the global minimum changes valley |
| 6 | `s06_applications.py` | `Applications` | **Engineering and finance.** Beam or truss under changing load; Budgeting, supply chains, financial reallocation |
| 7 | `s07_trajectory_sensitivity.py` | `TrajectorySensitivity` | **Sensitivity of a trajectory.** S' = (dF/dx) S + dF/dp; Toy robot, uncertain wheel radius: two plans, two clouds; First order: small perturbations only |
| 8 | `s08_recap_closing.py` | `RecapClosing` | **Recap and closing.** KKT finds the optimum; sensitivity measures its fragility; Closing line |

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
./kg check 4                     # validate manifest, scenes and narration
./kg render 4 -q l               # draft render (480p15); -q h for release
./kg assemble 4 -q l             # join the timeline into one video
./kg narrate 4 -q l --check-only # synthesise narration and check timing
```
