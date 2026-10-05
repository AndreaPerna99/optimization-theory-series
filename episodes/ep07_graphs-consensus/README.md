# Episode 7 · Many Minds: Graphs and Consensus

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 5, first half |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md) |
| Anchor | swarm alignment |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** A dozen robots each hold a different reading, and each can only talk to its neighbours. Can they all agree on the average, with no one in charge?

**Technical content.**
- **Distributed optimization:** multiple independent agents solve a problem collectively using only local information or communication with nearby agents. Essential where central control is impractical: large-scale, real-time applications across dispersed agents.
- **Applications:** multi-robot systems, sensor networks, collaborative AI.
- **Graph-based modelling:** agents as nodes, communication pathways as edges.
- **Graph theory basics:** adjacency matrices (who is connected to whom) and Laplacian matrices (network structure; critical for connectivity and influence).
- **Consensus:** agents reaching agreement on a shared value, such as an average position or a common goal, through local interactions.
- **Average consensus algorithm:** each agent repeatedly moves toward its neighbours' values; all converge to a common value without central oversight.
- **Why the Laplacian matters:** convergence speed is set by its eigenvalues.
- **The reveal:** consensus *is* gradient descent (Episode 1) on the total disagreement.
- **Leaders, briefly:** if some agents don't update (leaders), the others converge to a weighted combination of the leaders' values (leader-following and containment). This is a natural extension and leads into multi-robot coordination.
- **Applications of consensus:** coordinated swarm behaviour, sensor alignment, multi-vehicle synchronization.

**Precise statements.**
- *Laplacian.* For an undirected graph, $L = D - A_G$. $L$ is symmetric and positive semidefinite, $L\mathbf{1} = 0$, and its eigenvalues are $0 = \lambda_1(L) \le \lambda_2(L) \le \dots \le \lambda_n(L)$. $\lambda_2(L) > 0$ **if and only if** the graph is connected; it is called the algebraic connectivity.
- *Disagreement.* $\tfrac12 x^\top L x = \tfrac12 \sum_{(i,j) \in E} (x_i - x_j)^2$.
- *Consensus update.*

$$
x_{k+1} = (I - \varepsilon L)\, x_k \qquad\Longleftrightarrow\qquad x_i \leftarrow x_i + \varepsilon \sum_{j \in \mathcal{N}_i} (x_j - x_i)
$$

  Each agent uses only its neighbours' values. This is exactly gradient descent with step $\varepsilon$ on the disagreement $\tfrac12 x^\top L x$, whose Hessian is $L$.
- *Convergence.* On a connected undirected graph, the average $\tfrac1n \mathbf{1}^\top x$ never changes (because $\mathbf{1}^\top L = 0$), and every $x_i$ converges to it if and only if $0 < \varepsilon < 2/\lambda_n(L)$: **Episode 1's step-size threshold, with the Laplacian as the Hessian**. A simple sufficient choice is $\varepsilon < 1/d_{\max}$ (maximum degree). The disagreement shrinks per step by the factor $\max\big(|1 - \varepsilon\lambda_2(L)|,\ |1 - \varepsilon\lambda_n(L)|\big)$; for small $\varepsilon$ it is governed by $\lambda_2(L)$.
- *Continuous time.* $\dot x = -L x$ converges to the average on any connected undirected graph, at a rate set by $\lambda_2(L)$.
- *Directed graphs (mention).* Agreement still happens if the graph has a directed spanning tree, but on the **average** only if the graph is balanced.
- *Leaders.* Split the agents into followers $F$ and fixed leaders. Followers run $\dot x_F = -(L_{FF} x_F + L_{FL} x_L)$. If every follower is connected to some leader through the graph, followers converge to $x_F = H x_L$ with $H = -L_{FF}^{-1} L_{FL}$. Every row of $H$ is nonnegative and sums to 1, so each follower ends inside the convex hull of the leaders. With one leader, everyone converges to the leader.

**Key visuals.**
- Numbers on nodes averaging out step by step; colour converging.
- A line of agents (sparse, $\lambda_2(L)$ small) agreeing slowly next to a well-connected group agreeing almost instantly. Values of $\lambda_2(L)$ on screen.
- The consensus iterates and Episode 1's ball side by side on the disagreement landscape; the $\varepsilon$ slider crossing $2/\lambda_n(L)$ and oscillating, exactly as in Episode 1.
- Flock-style heading alignment as consensus on angles.
- Leaders (fixed) and followers being pulled into their convex hull.

**Corrections.** The PDF introduces Laplacians only as "network structures critical for connectivity and influence". The episode explains *why*: the Laplacian is the Hessian of disagreement, and its eigenvalues set the speed of agreement.

**Callbacks.** Step-size threshold (1). Forward: distributed GD (8), flocking (12).

**Closing line.** Nobody sees everything. Agreement can emerge from local conversations, and how connected you are determines how fast a group learns.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_agreement.py` | `HookAgreement` | **Agreeing with no one in charge.** A dozen robots, different readings; Each talks only to neighbours |
| 2 | `s02_why_distributed.py` | `WhyDistributed` | **Why distributed.** Local information only; Multi-robot systems, sensor networks, collaborative AI |
| 3 | `s03_graphs_matrices.py` | `GraphsMatrices` | **Graphs, adjacency, Laplacian.** Agents as nodes, links as edges; A_G, D and L = D - A_G built on screen |
| 4 | `s04_average_consensus.py` | `AverageConsensus` | **Average consensus.** Values averaging step by step; Each agent uses neighbours only; the average is invariant |
| 5 | `s05_consensus_is_gd.py` | `ConsensusIsGd` | **Consensus is gradient descent.** Disagreement 1/2 x^T L x, Hessian L; Threshold 2 / lambda_n(L): Episode 1 again |
| 6 | `s06_connectivity_speed.py` | `ConnectivitySpeed` | **Connectivity and speed.** Line graph vs well-connected group; lambda_2(L) sets the speed |
| 7 | `s07_directed_flocking.py` | `DirectedFlocking` | **Directed graphs and flocks.** Agreement vs agreement on the average; Heading alignment as consensus |
| 8 | `s08_leaders_containment.py` | `LeadersContainment` | **Leaders.** Leaders fixed, followers pulled in; x_F = H x_L: inside the convex hull |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Swarms, sensor alignment, vehicle synchronization; Closing line |

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
./kg check 7                     # validate manifest, scenes and narration
./kg render 7 -q l               # draft render (480p15); -q h for release
./kg assemble 7 -q l             # join the timeline into one video
./kg narrate 7 -q l --check-only # synthesise narration and check timing
```
