# Episode 2 · Corners and Bowls: Linear Programming and Convexity

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 15–20 min |
| From the original PDF | Video 2 |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md) |
| Anchor | factory production LP, logistics |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** A factory has limited machine hours and labour. How much of each product should it make, and what would one more hour of machine time be worth?

**Technical content.**
- **Linear programming:** optimization with a linear objective and linear constraints (maximize profit, minimize cost). Straight-line relationships make LPs efficient and reliable to solve for structured problems such as scheduling and budget optimization.
- **The feasible polytope** and why the optimum is found at a vertex.
- **The simplex method:** move along edges of the feasible region from vertex to adjacent vertex, improving the objective, until no neighbouring vertex is better. Visuals of simplex "jumping" between vertices to reach the best solution.
- **Applications:** resource allocation (time, budget or staff across projects); logistics and transportation (routes, capacities and schedules to meet delivery requirements at the lowest cost).
- **Types of solutions:** local versus global optima in nonlinear functions, with simple illustrations of non-convex functions with several local minima.
- **Convexity:** the bowl shape that guarantees any local minimum is global.
- **Non-convex functions:** multiple minima and saddle points, where finding the global minimum is no longer guaranteed.
- **Duality:** every LP (the primal) has a twin (the dual) that bounds it and, at the optimum, matches it. Made concrete with **shadow prices**.
- **Practical takeaways:** convexity makes optimization reliable; duality gives a second view of the problem that bounds and prices it.
- **Preview:** next, constrained optimization in general and the multipliers that make duality precise; then sensitivity analysis.

**Precise statements.**
- *LP form.* Maximize $c^\top x$ subject to $Ax \le b$, $x \ge 0$. The feasible set is a convex polyhedron.
- *Possible outcomes.* An LP is either infeasible, unbounded, or has an optimal value. If it has an optimal value and the feasible set has at least one vertex, then **some vertex is optimal**. The optimum may also be a whole edge or face.
- *Simplex.* Each step moves to an adjacent vertex with an objective at least as good. It stops when no adjacent edge improves the objective; because an LP is convex, this local test certifies global optimality. Worst-case running time is exponential (Klee–Minty examples), but it is typically fast in practice; interior-point methods are a polynomial-time alternative (mention only).
- *Convex function.* $f(\theta x + (1-\theta) y) \le \theta f(x) + (1-\theta) f(y)$ for all $x, y$ and $\theta \in [0, 1]$: the chord lies above the graph. A convex problem has a convex objective and a convex feasible set.
- *Key theorem.* In a convex problem every local minimum is a global minimum, and the set of minimizers is convex. **Strict** convexity additionally guarantees there is at most one minimizer. (Existence needs more, e.g. a closed and bounded feasible set.)
- *Saddle point.* A stationary point that is neither a local minimum nor a local maximum. A Hessian with both positive and negative eigenvalues is a sufficient test; degenerate saddles (e.g. the monkey saddle $x^3 - 3xy^2$ at the origin) fail the test but are still saddles.
- *Duality.* For the primal above, the dual is: minimize $b^\top \mu$ subject to $A^\top \mu \ge c$, $\mu \ge 0$.
  - *Weak duality:* $c^\top x \le b^\top \mu$ for every feasible pair, so any dual-feasible $\mu$ bounds the best possible profit. (The dual variables are written $\mu$ on purpose: Episode 3 reveals they are the KKT multipliers.)
  - *Strong duality:* if the primal has an optimum, so does the dual, with equal values.
  - *Complementary slackness:* at the optimum $\mu_i^\star\,(b - Ax^\star)_i = 0$ for every resource $i$ (a resource that is not fully used has price zero) and $x_j^\star\,(A^\top \mu^\star - c)_j = 0$ for every product $j$ (a product that is actually made earns exactly what its resources are worth at shadow prices).
- *Shadow price.* $\mu_i^\star$ equals the rate of change of the optimal profit as $b_i$ (resource $i$) increases, valid for small changes that do not change which constraints are binding (non-degenerate optimum).

**Key visuals.**
- The factory LP in 2D: the polygon, the objective's level lines sweeping across until they touch the last vertex.
- Simplex walking the vertices.
- The objective rotating until the optimal vertex becomes an optimal **edge**, then a different vertex (corrects the uniqueness claim and previews the "jump" of Episode 4).
- A convex bowl next to a bumpy non-convex surface, with balls landing in different minima from different starts; a saddle point.
- Shadow prices as price tags on the binding constraints; a zero tag on the slack one.

**Corrections.**
- The PDF says convexity "guarantees a single solution" / "ensures unique solutions". It guarantees that every local minimum is global; uniqueness needs *strict* convexity. LP itself proves it: when the objective is parallel to an edge of the polytope, the whole edge is optimal.
- The PDF's duality example ("a business may use the dual approach to maximize returns while minimizing resource use") is vague. The precise and understandable version is shadow prices: each dual variable is the value of one more unit of a resource (one more truck, one more machine hour).
- The PDF describes duality as a "mirror" of the problem. Keep the image only if it is followed by the concrete statements above (bound, equality at the optimum, prices).

**Callbacks forward.** Shadow prices become KKT multipliers (Ep 3) and sensitivities (Ep 4). "Optima live on corners" returns with Lasso (Ep 5).

**Closing line.** The best answer to a linear problem sits on the boundary of what's allowed: limits aren't only obstacles, the optimum is often found by using them fully. And every limit has a price; knowing which one binds tells you what is really holding you back.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_factory.py` | `HookFactory` | **The factory question.** Limited machine hours and labour; What to make, and what is one more hour worth? |
| 2 | `s02_lp_polytope.py` | `LpPolytope` | **Linear programs and the polytope.** Linear objective and constraints; Level lines sweep to the last vertex; Outcomes: infeasible, unbounded, optimal |
| 3 | `s03_simplex_walk.py` | `SimplexWalk` | **The simplex method.** Walk vertex to vertex along edges; Stop when no neighbour is better: global by convexity |
| 4 | `s04_applications.py` | `Applications` | **Resource allocation and logistics.** Time, budget, staff across projects; Routes, capacities and schedules at lowest cost |
| 5 | `s05_edge_optimum.py` | `EdgeOptimum` | **When the optimum is an edge.** Objective rotates: vertex -> whole edge -> new vertex; Convexity does not mean uniqueness |
| 6 | `s06_convexity.py` | `Convexity` | **Bowls: convexity.** Chord above the graph; Every local minimum is global; Strict convexity: at most one minimizer |
| 7 | `s07_nonconvex.py` | `Nonconvex` | **Bumps and saddles.** Several local minima; different starts, different answers; Saddle points |
| 8 | `s08_duality_prices.py` | `DualityPrices` | **Duality and shadow prices.** The dual problem as a bound; Strong duality and complementary slackness; Price tags on binding constraints, zero on slack |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Convexity makes optimization reliable; duality prices limits; Closing line |

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
./kg check 2                     # validate manifest, scenes and narration
./kg render 2 -q l               # draft render (480p15); -q h for release
./kg assemble 2 -q l             # join the timeline into one video
./kg narrate 2 -q l --check-only # synthesise narration and check timing
```
