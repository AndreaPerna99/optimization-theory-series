# Episode 8 · Searching Together: Distributed Gradient Descent and SAR Robots

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 5, second half |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md), [Ep 3](../ep03_lagrange-kkt-svm/README.md), [Ep 7](../ep07_graphs-consensus/README.md) |
| Anchor | SAR robots (to confirm) |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** Each robot knows only its own part of the problem. How can the team find the solution that is best for all of them together?

**Technical content.**
- **The problem:** minimize a sum $\sum_i f_i(x)$ where each agent $i$ knows only its own $f_i$, and all must agree on a common $x$.
- **Distributed gradient descent (DGD):** each agent computes its local gradient and mixes its estimate with its neighbours'. The network collectively reaches (nearly) the optimum without global information.
- **Why DGD stalls** with a constant step, and **gradient tracking**, which fixes it.
- **Multipliers return,** briefly: primal–dual methods give each agreement constraint $x_i = x_j$ a multiplier, a "price of disagreement" (callback to Episodes 2–4; mention only).
- **The SAR project:** robots as independent agents searching for survivors, using consensus to coordinate search zones, prevent redundant coverage, agree on resource distribution, search boundaries and task assignments, enhance coverage and minimize wasted effort.
- **Real-world examples:** swarm robotics using local rules for group tasks (agricultural pest control, automated warehouse sorting); sensor networks coordinating data collection (environmental monitoring networks optimizing power use while maintaining data accuracy).
- **Recap:** consensus and distributed gradient descent enable decentralized decision-making; distributed optimization is a scalable, adaptive way to manage systems that act independently yet must coordinate.
- **Preview:** optimal control and reinforcement learning, where decisions unfold over time.

**Precise statements.**
- *DGD.* $x_i^{k+1} = \sum_{j} W_{ij}\, x_j^k - \alpha\, \nabla f_i(x_i^k)$, with $W$ a doubly stochastic mixing matrix that only has nonzero entries between neighbours (e.g. $W = I - \varepsilon L$, which is doubly stochastic, i.e. also nonnegative, when $0 < \varepsilon \le 1/d_{\max}$).
- *Why it stalls.* At the true optimum $x^\star$, $\sum_i \nabla f_i(x^\star) = 0$, but the individual $\nabla f_i(x^\star)$ are generally nonzero, so each agent keeps being pushed away. With a constant step DGD converges only to a neighbourhood of $x^\star$ whose size scales with $\alpha$. Diminishing steps make it exact but slow.
- *Gradient tracking.* Each agent keeps a second variable $s_i$ that estimates the network-average gradient:

$$
x^{k+1} = W x^k - \alpha\, s^k, \qquad s^{k+1} = W s^k + \nabla f(x^{k+1}) - \nabla f(x^k), \qquad s^0 = \nabla f(x^0)
$$

  (stacked over agents; $\nabla f(x)$ means the stack of local gradients $\nabla f_i(x_i)$). The average of the $s_i$ always equals the average of the local gradients. For smooth, strongly convex $f_i$, a connected graph and a small enough constant $\alpha$, all agents converge **exactly** to $x^\star$, and fast (linearly).
- *SAR coverage (reference formulation, use only if it matches the project).* A standard way to "divide search zones and avoid redundant coverage" is Voronoi coverage: robots at positions $p_i$ minimize $\int \min_i \|q - p_i\|^2 \phi(q)\,dq$, where $\phi$ is the probability density of where survivors may be. The gradient step moves each robot toward the centroid of its own Voronoi cell (Lloyd's algorithm), which needs only neighbouring robots' positions. **[CONFIRM]** which formulation the SAR project actually uses.

**Key visuals.**
- DGD and gradient tracking side by side on the same network and the same problem: DGD hovering around the target, gradient tracking landing on it.
- A map with a survivor-probability heat map; robots spreading out, Voronoi cells forming, each robot settling at its cell's centroid.
- Real SAR footage or simulation **[CONFIRM]**.

**Project.** The SAR robots: this is the flagship project episode. Show what went wrong in early versions as well as what worked. **[CONFIRM]**: platform, number of robots, simulation versus real hardware, which algorithms were used (consensus, coverage, task allocation), what results can be shown.

**Corrections.** The PDF describes gradient tracking as "keeping track of a global objective's changes dynamically, useful when the optimal solution is time-varying". Its central purpose is different: plain DGD with a constant step only gets *near* the optimum because each agent follows its own local gradient; gradient tracking has agents also run consensus on their gradients, so each estimates the *global* gradient and the network converges exactly. The time-varying aspect is real, but it is saved for the finale (Ep 12), where it becomes the series' closing idea.

**Callbacks.** Consensus (7), step size (1), multipliers (2–4). Forward: the moving optimum (12).

**Closing line.** A group improves best when each member shares not just what they know, but which direction they think is better.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_team.py` | `HookTeam` | **Each robot knows a part.** Best for the team, not for each robot |
| 2 | `s02_sum_problem.py` | `SumProblem` | **Minimizing a sum.** min sum_i f_i(x), f_i private to agent i; All must agree on x |
| 3 | `s03_dgd.py` | `Dgd` | **Distributed gradient descent.** Mix with neighbours, step on the local gradient |
| 4 | `s04_dgd_stalls.py` | `DgdStalls` | **Why DGD stalls.** Local gradients nonzero at the optimum; Constant step: only a neighbourhood |
| 5 | `s05_gradient_tracking.py` | `GradientTracking` | **Gradient tracking.** Consensus on gradients too; Side by side: hovering vs landing exactly |
| 6 | `s06_price_of_disagreement.py` | `PriceOfDisagreement` | **The price of disagreement.** Primal-dual: a multiplier per agreement constraint; Callback to Episodes 2-4 |
| 7 | `s07_sar_coverage.py` | `SarCoverage` | **Dividing the search.** Survivor-probability map; Voronoi cells, robots to centroids (if it matches confirm) |
| 8 | `s08_sar_project.py` | `SarProject` | **The SAR robots.** Project footage and results (confirm); What went wrong, what worked |
| 9 | `s09_swarms_sensors.py` | `SwarmsSensors` | **Swarms and sensor networks.** Pest control, warehouse sorting; Environmental monitoring: power vs accuracy |
| 10 | `s10_recap_closing.py` | `RecapClosing` | **Recap and closing.** Scalable, adaptive decentralized decisions; Closing line |

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
./kg check 8                     # validate manifest, scenes and narration
./kg render 8 -q l               # draft render (480p15); -q h for release
./kg assemble 8 -q l             # join the timeline into one video
./kg narrate 8 -q l --check-only # synthesise narration and check timing
```
