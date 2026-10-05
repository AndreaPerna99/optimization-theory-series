# Episode 11 · Beyond Engineering: Economics, Fairness and Society

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 7, first half |
| Watch first | [Ep 2](../ep02_linear-programming-convexity/README.md), [Ep 3](../ep03_lagrange-kkt-svm/README.md) |
| Anchor | markets, Pareto front |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** Can a whole society be optimized? And if so, for whom?

**Technical content.**
- **Resource allocation:** allocating labour, capital and other resources across sectors to maximize productivity and minimize waste.
- **Utility and welfare maximization:** utility functions in consumer theory, where individuals maximize satisfaction within a budget (Episode 3 applied to people); welfare maximization in public policy, aiming for the best outcome for society as a whole.
- **Pareto efficiency and multi-objective optimization:** no one can be made better off without making someone else worse off; balancing competing goals such as economic growth and environmental sustainability (environmental economics).
- **Prices as multipliers:** market prices behave like the multipliers of a society-wide allocation problem; price adjustment as a distributed optimization algorithm.
- **Decision-making and fairness:** optimization for distributing resources in public services (healthcare, education, social welfare), aiming for fairness and equity.
- **Welfare economics and public policy:** governments using optimization to design policies that distribute resources fairly and effectively.
- **Ethics in social optimization:** when decisions affect people's access to resources or social equity.
- **Additional applications:** healthcare and public health (resource distribution during crises to maximize patient outcomes and equity); education and urban planning (infrastructure and policy decisions for maximum societal benefit).

**Precise statements.**
- *Consumer problem.* Maximize $u(x)$ subject to $p^\top x \le b$ (prices $p$, income $b$: the budget is the resource). At an optimum where the budget binds and every good is bought ($x^\star > 0$), KKT gives $\nabla u(x^\star) = \mu\, p$: the marginal utility per unit of money is equal across goods. $\mu$ is the **marginal utility of money**, a shadow price (callback to Ep 2; economists usually write it $\lambda$).
- *Pareto optimality (minimizing objectives $f_1,\dots,f_J$).* $x$ is Pareto optimal if no $y$ has $f_i(y) \le f_i(x)$ for all $i$ with strict inequality for at least one. The set of their objective values is the **Pareto front**.
- *Scalarization.* Minimizing a weighted sum $\sum_i w_i f_i$ with $w_i > 0$ always yields a Pareto-optimal point. In convex problems every Pareto-optimal point minimizes some weighted sum with $w \ge 0$, $w \ne 0$ (but with some weights zero, a minimizer may be only weakly Pareto optimal); on non-convex fronts some Pareto points can never be reached by weighted sums.
- *Welfare functions.* Utilitarian: maximize $\sum_i u_i$. Rawlsian (max-min): maximize $\min_i u_i$. They can select different points on the same Pareto front (and a max-min choice may be only weakly Pareto optimal). The choice between them is a value judgment, not a calculation.
- *Prices as multipliers.* In an idealized economy, a central planner's allocation problem has a dual whose multipliers are prices. The price-adjustment rule "raise the price of anything in excess demand" ($p \leftarrow p + \alpha\,(\text{demand} - \text{supply})$) is gradient ascent on that dual: each agent optimizes privately given prices, and prices coordinate them (dual decomposition, callback to Ep 8). Under idealized assumptions (price-taking agents, complete markets, no externalities, locally non-satiated preferences) competitive equilibria are Pareto efficient (First Welfare Theorem). **State the assumptions**; when they fail, as with pollution, the market misses a price. Environmental policy such as a carbon tax is setting the missing multiplier.

**Key visuals.**
- The budget line and indifference curves with the tangency point (Episode 3's tangency, now in economics).
- The Pareto front as a curve, with the two goals drawn as utilities (higher is better) on the axes: points below it are wasteful, points above impossible, every point on it a trade-off. A weight slider moving the chosen point along it; a non-convex front with a gap weighted sums can't reach.
- Utilitarian and Rawlsian choices on the same front.
- Price adjustment: a market with excess demand, the price rising until it clears.

**Corrections.**
- The ethics section should not preach. The mathematics can show the front; choosing a point on it is a value judgment. That is a strong, honest way to address ethics.
- Claims that markets or policies are "optimal" must state their assumptions.

**Callbacks.** KKT and tangency (3), shadow prices (2), sensitivity (4), dual decomposition (8).

**Closing line.** Some improvements cost nothing; others always cost someone something. Optimization can tell you which is which, but not which cost is acceptable.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_society.py` | `HookSociety` | **Optimizing a society.** Can it be done? For whom? |
| 2 | `s02_resource_allocation.py` | `ResourceAllocation` | **Allocating resources.** Labour and capital across sectors; Productivity vs waste |
| 3 | `s03_consumer_tangency.py` | `ConsumerTangency` | **The consumer problem.** Budget line and indifference curves; grad u = mu p: marginal utility of money |
| 4 | `s04_pareto_front.py` | `ParetoFront` | **The Pareto front.** Utilities on the axes: wasteful below, impossible above; Growth vs sustainability |
| 5 | `s05_scalarization.py` | `Scalarization` | **Weighted sums.** Weight slider moves along the front; Non-convex fronts: gaps weighted sums can't reach |
| 6 | `s06_welfare_fairness.py` | `WelfareFairness` | **Fairness.** Utilitarian vs Rawlsian on the same front; Choosing a point is a value judgment |
| 7 | `s07_prices_as_multipliers.py` | `PricesAsMultipliers` | **Prices as multipliers.** Price rises with excess demand: dual ascent; First Welfare Theorem and its assumptions |
| 8 | `s08_externalities.py` | `Externalities` | **Missing prices.** Pollution: a cost no market prices; Carbon tax = setting the missing multiplier |
| 9 | `s09_public_services.py` | `PublicServices` | **Public services.** Healthcare in crises, education, urban planning; Ethics when access is at stake |
| 10 | `s10_recap_closing.py` | `RecapClosing` | **Recap and closing.** What optimization can and cannot decide; Closing line |

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
./kg check 11                     # validate manifest, scenes and narration
./kg render 11 -q l               # draft render (480p15); -q h for release
./kg assemble 11 -q l             # join the timeline into one video
./kg narrate 11 -q l --check-only # synthesise narration and check timing
```
