# Episode 12 · Self-Organization and the Moving Optimum

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 7, second half + series wrap-up |
| Watch first | the whole series (Episodes 1–11) |
| Anchor | ants, flocks, moving target |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** Ants have no map and no leader, yet a colony finds the shortest path to food. How? And what happens when the food moves?

**Technical content.**
- **Self-organizing systems:** order emerging from local interactions without central control, as in ant colonies and bird flocks, where simple rules lead to complex, adaptive behaviour.
- **Stigmergy and collective intelligence:** agents coordinate by leaving markers in the environment (pheromones), influencing future actions; decentralized systems achieve optimization indirectly, without oversight.
- **Ant colonies:** foraging through pheromone trails that identify efficient food sources, a natural example of decentralized optimization; **ant colony optimization** as the algorithm inspired by it.
- **Flocking:** alignment as consensus on headings (callback to Ep 7).
- **Swarm robotics:** robots following simple local rules to produce an optimized group outcome (search and rescue, agricultural pest control), calling back to the SAR robots instead of repeating them.
- **Social networks:** information spreading through local interactions into large-scale patterns of influence and behaviour, and why those patterns are often *not* optimal.
- **The moving optimum:** time-varying optimization, and gradient tracking in its time-varying role.
- **Series wrap-up:** recap of the progression from basic principles to complex applications; encouragement to apply the ideas in viewers' own fields.

**Precise statements.**
- *Ant colony optimization.* An ant at a node chooses edge $(i,j)$ with probability proportional to $\tau_{ij}^{a}\,\eta_{ij}^{b}$, where $\tau$ is pheromone and $\eta$ a heuristic desirability (e.g. inverse length). After each round, $\tau_{ij} \leftarrow (1-\rho)\,\tau_{ij} + \Delta\tau_{ij}$: pheromone evaporates at rate $\rho$ and is reinforced in proportion to path quality. Short paths are completed faster and more often, so they accumulate pheromone faster. (Use $a$, $b$ for the exponents to avoid clashing with $\alpha$, $\beta$.)
- *The double-bridge experiment* (Deneubourg, Goss and colleagues, Argentine ants, late 1980s): given two bridges of different lengths, the colony comes to favour the shorter one. Cite as an experimental finding.
- *Stigmergy* was named by Pierre-Paul Grassé (1959) for termite nest building.
- *Flocking.* Reynolds' boids use three local rules: separation, alignment, cohesion. Alignment is consensus on headings.
- *Opinion dynamics.* In the DeGroot model, people repeatedly average their neighbours' opinions: it is exactly consensus (Ep 7). Real social networks add stubborn agents, homophily and amplification, which produce polarization and echo chambers: local rules don't guarantee a good global outcome.
- *Tracking a moving optimum.* Let each $f_k$ be $m$-strongly convex and $M$-smooth with the same $m, M$ for all $k$, and let its minimizer $x_k^\star$ drift by at most $\sigma$ per step. One gradient step per time step with $\alpha = 2/(m+M)$ contracts the distance to the current minimizer by $c = (M-m)/(M+m) < 1$, so the tracking error satisfies $\limsup_k \|x_k - x_k^\star\| \le \sigma/(1-c)$: proportional to the drift, and larger when each step contracts less. The error never goes to zero while the optimum moves, but it stays small as long as you keep stepping. In networks, the same role is played by gradient tracking / dynamic average consensus (Ep 8) following a time-varying average.

**Key visuals.**
- Ants on a double bridge, pheromone thickness growing on the short branch; evaporation erasing a stale trail when the food source moves.
- A flock aligning from random headings.
- A social network where opinions polarize, next to the colony that keeps re-optimizing.
- The finale shot: the landscape the ball has travelled since Episode 1 (the series map of Episode 0) starts to move. The ball that stops when the gradient is zero is left behind; the ball that keeps following the gradient stays close to the moving minimum.
- The series map from Episode 0, now with every location visited.

**Corrections.** The PDF says information spreads across social networks "in optimized ways". It spreads through local interactions that create large-scale patterns, but those patterns are often not optimal. Contrasting them with ant colonies, where evaporation keeps the system from locking into stale paths, is more honest and more interesting.

**The finale.** Everything so far assumed the landscape stays still, so the gradient eventually reaches zero and you stop. But real problems move: targets drift, environments change, people change. Return to tracking from Episode 8, now in its time-varying role: agents that keep following an optimum that never stops moving. In a changing world the gradient is never permanently zero.

**Closing line.** That is what Keep the Gradient means: not finding the best answer once, but never stopping to sense which way is better, because "better" keeps moving.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_ants.py` | `HookAnts` | **No map, no leader.** Ants find the shortest path; What if the food moves? |
| 2 | `s02_self_organization.py` | `SelfOrganization` | **Order from local rules.** Ant colonies, bird flocks; No central control |
| 3 | `s03_stigmergy_bridge.py` | `StigmergyBridge` | **Stigmergy and the double bridge.** Coordination through markers in the environment; Short branch gains pheromone faster |
| 4 | `s04_ant_colony_optimization.py` | `AntColonyOptimization` | **Ant colony optimization.** Choice probability tau^a eta^b; Reinforcement and evaporation |
| 5 | `s05_flocking.py` | `Flocking` | **Flocking.** Separation, alignment, cohesion; Alignment is consensus (Episode 7) |
| 6 | `s06_swarm_robotics.py` | `SwarmRobotics` | **Swarm robotics.** Callback to the SAR robots; Pest control and search-and-rescue |
| 7 | `s07_social_networks.py` | `SocialNetworks` | **Social networks.** DeGroot averaging = consensus; Polarization: local rules, poor global outcome |
| 8 | `s08_moving_optimum.py` | `MovingOptimum` | **The moving optimum.** The landscape starts to move; Stop at zero gradient: left behind; keep stepping: stay close |
| 9 | `s09_tracking_networks.py` | `TrackingNetworks` | **Tracking together.** Gradient tracking in its time-varying role; Error bounded, never zero |
| 10 | `s10_series_wrapup.py` | `SeriesWrapup` | **The whole journey.** The Episode 0 map, every location visited; From one ball to societies |
| 11 | `s11_closing.py` | `Closing` | **Keep the gradient.** 'Better' keeps moving; Final closing line |

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
./kg check 12                     # validate manifest, scenes and narration
./kg render 12 -q l               # draft render (480p15); -q h for release
./kg assemble 12 -q l             # join the timeline into one video
./kg narrate 12 -q l --check-only # synthesise narration and check timing
```
