# Episode 3 · Walls: Lagrange Multipliers, KKT and SVM

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 15–20 min |
| From the original PDF | Video 3, first half |
| Watch first | [Ep 2](../ep02_linear-programming-convexity/README.md) |
| Anchor | SVM |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** A ball rolls downhill and hits a wall. Where does it stop, and how hard is the wall pushing?

**Technical content.**
- **Equality constraints** (the solution must lie exactly on a curve or surface) and **inequality constraints** (the solution must stay on one side), and how both define feasible regions. The budget-cap example from business.
- **Lagrange multipliers** for equality constraints: at the optimum, the level curve of $f$ is tangent to the constraint.
- **KKT conditions** extending Lagrange multipliers to inequality constraints: the mathematical foundation of optimality under real-world restrictions.
- **SVM** as the worked example where KKT determines the decision boundary; framed as an anticipation of the machine learning episodes.
- **The reveal:** these multipliers are the same objects as Episode 2's dual variables and shadow prices.

**Precise statements.**
- *Problem.* Minimize $f(x)$ subject to $h_j(x) = 0$ and $g_i(x) \le 0$. Lagrangian $\mathcal{L}(x,\lambda,\mu) = f(x) + \sum_j \lambda_j h_j(x) + \sum_i \mu_i g_i(x)$.
- *Lagrange condition (equalities only).* At a local minimum $x^\star$ where the $\nabla h_j(x^\star)$ are linearly independent, there exist $\lambda_j$ with $\nabla f(x^\star) + \sum_j \lambda_j \nabla h_j(x^\star) = 0$.
- *KKT conditions.*
  1. Stationarity: $\nabla f(x^\star) + \sum_j \lambda_j \nabla h_j(x^\star) + \sum_i \mu_i \nabla g_i(x^\star) = 0$
  2. Primal feasibility: $h_j(x^\star) = 0$, $g_i(x^\star) \le 0$
  3. Dual feasibility: $\mu_i \ge 0$
  4. Complementary slackness: $\mu_i\, g_i(x^\star) = 0$ for every $i$
- *When they hold.* KKT conditions are **necessary** at a local minimum when a constraint qualification holds (e.g. linearly independent active constraint gradients, or Slater's condition for convex problems). They are **sufficient** for a global minimum when the problem is convex ($f$, $g_i$ convex, $h_j$ affine). Do not present them as necessary and sufficient in general.
- *Force balance (inequalities).* Stationarity reads $-\nabla f(x^\star) = \sum_i \mu_i \nabla g_i(x^\star)$. The downhill pull $-\nabla f$ pushes into the walls (each $\nabla g_i$ points out of the feasible region); each active wall pushes back along $-\nabla g_i$ with strength $\mu_i$. $\mu_i \ge 0$ says walls can push but never pull. Complementary slackness says a wall you're not touching pushes with zero force.
- *Hard-margin SVM.* Minimize $\tfrac12\|w\|^2$ subject to $y_i (w^\top x_i + w_0) \ge 1$ for all data points $(x_i, y_i)$, $y_i \in \{-1, +1\}$. The margin width is $2/\|w\|$. KKT gives $w = \sum_i \mu_i y_i x_i$ and $\sum_i \mu_i y_i = 0$ with $\mu_i \ge 0$, and $\mu_i > 0$ only for points exactly on the margin. Those are the **support vectors**. Points with $\mu_i = 0$ can be deleted without changing the boundary. (A margin point may in degenerate cases have $\mu_i = 0$, so define support vectors as the points with $\mu_i > 0$.)
- *Soft margin (mention).* With slack variables and penalty $C$, misclassified or inside-margin points also get nonzero multipliers (bounded by $C$). Use the hard margin for the main explanation.
- *Link to LP.* For an LP, the KKT multipliers of the constraints $Ax \le b$ are exactly the optimal dual variables $\mu^\star$ of Episode 2: same letter, same object.

**Key visuals.**
- The ball rolling down a contour map into a wall and stopping, with $-\nabla f$ and the wall's reaction force drawn as equal and opposite arrows; the reaction arrow labelled $\mu$.
- An equality constraint as a curve, the level curves of $f$ sliding until one is tangent to it; $\nabla f$ and $\nabla h$ becoming parallel.
- A wall the ball doesn't touch, with a force arrow of length zero.
- SVM: two classes of points, the widest street between them, the support vectors lighting up; deleting a non-support point leaves the boundary unchanged, deleting a support vector can move it (choose an example where no support vector is redundant, so it visibly does).

**Corrections.**
- The PDF calls inequality constraints "flexible limits". They are as hard as equalities. What's special is that they can be **active** (you are pressed against them) or **inactive** (you're strictly inside and they don't matter). That is the heart of KKT.

**Callbacks.** Multipliers = shadow prices of Episode 2 (the reveal). Forward: the multiplier as a derivative (Ep 4); regularization as a hidden constraint (Ep 5).

**Closing line.** Most of what surrounds you doesn't constrain you. Only a few limits are active, and those are the ones worth understanding.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_wall.py` | `HookWall` | **The ball hits a wall.** Where does it stop, and how hard does the wall push? |
| 2 | `s02_constraint_types.py` | `ConstraintTypes` | **Equalities and inequalities.** On a curve vs on one side; Active vs inactive constraints; Budget-cap example |
| 3 | `s03_lagrange_tangency.py` | `LagrangeTangency` | **Lagrange multipliers.** Level curves slide until tangent to the constraint; grad f and grad h become parallel |
| 4 | `s04_kkt_force_balance.py` | `KktForceBalance` | **KKT as force balance.** Downhill pull balanced by the wall force mu; Walls push, never pull: mu >= 0; When KKT is necessary, when sufficient |
| 5 | `s05_complementary_slackness.py` | `ComplementarySlackness` | **Walls you don't touch.** Inactive wall: force of length zero; mu_i g_i(x*) = 0 |
| 6 | `s06_svm_margin.py` | `SvmMargin` | **SVM: the widest street.** Two classes, maximum margin 2/‖w‖; Constraints y_i (w^T x_i + w_0) >= 1 |
| 7 | `s07_svm_support_vectors.py` | `SvmSupportVectors` | **Support vectors.** Points with mu_i > 0 light up; Delete a non-support point: nothing moves; Delete a support vector: the boundary can move |
| 8 | `s08_multiplier_reveal.py` | `MultiplierReveal` | **Multipliers are prices.** KKT multipliers of an LP = its dual variables; Callback to shadow prices |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Only a few limits are active; Closing line |

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
./kg check 3                     # validate manifest, scenes and narration
./kg render 3 -q l               # draft render (480p15); -q h for release
./kg assemble 3 -q l             # join the timeline into one video
./kg narrate 3 -q l --check-only # synthesise narration and check timing
```
