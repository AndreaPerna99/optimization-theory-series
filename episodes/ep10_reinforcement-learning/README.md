# Episode 10 · Learning to Act: Reinforcement Learning

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 15–20 min |
| From the original PDF | Video 6, RL half |
| Watch first | [Ep 9](../ep09_optimal-control-quadrotor/README.md) |
| Anchor | grid world, continuous control (to confirm) |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** What if the quadrotor didn't have a model of its own physics? Can it learn to act just by trying?

**Technical content.**
- **Reinforcement learning:** agents learn sequential decisions by maximizing cumulative reward in an environment.
- **Policy optimization and control:** the overlap with optimal control, where policies guide actions to maximize reward (or minimize cost); RL agents improve policies through feedback, much as optimal control adjusts actions to evolving conditions.
- **Q-learning and value functions:** a foundational RL algorithm where agents use value functions to approximate optimal actions; how RL solves control problems when information about the system is limited.
- **The Bellman equation** as the bridge: RL is optimal control without a known model.
- **Exploration versus exploitation,** and the **discount factor**.
- **Policy gradient,** briefly, for continuous problems like flight.
- **Preview:** the final part, where optimization leaves engineering: economics, social sciences and self-organizing systems.

**Precise statements.**
- *Reward and cost.* Reward is negative cost; RL maximizes $\mathbb{E}\big[\sum_t \gamma^t r_t\big]$ with discount $0 \le \gamma < 1$. The effective planning horizon is about $1/(1-\gamma)$ steps.
- *Bellman optimality equation.* $Q^\star(s,a) = \mathbb{E}\big[r + \gamma \max_{a'} Q^\star(s', a')\big]$.
- *Q-learning update.* $Q(s,a) \leftarrow Q(s,a) + \alpha\big[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\big]$. It is a stochastic, step-size-driven update (callback to SGD in Ep 5). Tabular Q-learning converges to $Q^\star$ if every state–action pair keeps being visited and the step sizes decrease appropriately.
- *Exploration.* For example, $\epsilon$-greedy: take a random action with probability $\epsilon$, otherwise the best known one.
- *Policy gradient.* For a parametrized policy $\pi_\theta$, $\nabla_\theta J = \mathbb{E}\big[\nabla_\theta \log \pi_\theta(a \mid s)\, \hat A\big]$ with $\hat A$ an advantage estimate: gradient **ascent** on expected return (callback to Ep 1). Continuous control commonly uses actor-critic methods (e.g. PPO, SAC); name only.

**Key visuals.**
- A grid world: Q-values spreading backward from the goal, arrows of the greedy policy forming.
- The effect of $\gamma$: a short-sighted agent taking the nearby small reward versus a patient one taking the far large reward.
- An agent that never explores getting stuck on a mediocre route (local optimum, again).
- A continuous-control learning curve (simulated drone or simpler system).

**Project.** **[CONFIRM]** whether RL was done on the quadrotor. If yes, show it with the method actually used. If not, the quadrotor stays in Episode 9 and this episode uses the grid world and a simple simulated system.

**Corrections.** Tabular Q-learning suits small discrete problems; a quadrotor lives in continuous space, where policy-gradient or actor-critic methods are used. Don't pair Q-learning with the quadrotor directly.

**Callbacks.** Bellman (9), SGD and step size (5, 1), gradient ascent (1), local optima (2).

**Closing line.** When you don't know how the world works, you can still improve by acting, observing the outcome, and updating. Patience is literally a parameter.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_no_model.py` | `HookNoModel` | **No model of the world.** Can a drone learn to act just by trying? |
| 2 | `s02_rl_setup.py` | `RlSetup` | **Rewards and returns.** Agent, environment, reward = -cost; Discounted return |
| 3 | `s03_bellman_optimality.py` | `BellmanOptimality` | **Bellman optimality.** Q*(s,a) = E[r + gamma max Q*(s',a')]; Optimal control without a model |
| 4 | `s04_q_learning.py` | `QLearning` | **Q-learning in a grid world.** Values spreading back from the goal; The update is a stochastic step (SGD callback) |
| 5 | `s05_exploration.py` | `Exploration` | **Explore or exploit.** epsilon-greedy; Never exploring: stuck on a mediocre route |
| 6 | `s06_discount.py` | `Discount` | **Patience is a parameter.** Short-sighted vs patient agent; Horizon about 1/(1 - gamma) |
| 7 | `s07_policy_gradient.py` | `PolicyGradient` | **Policy gradient.** Gradient ascent on expected return; Actor-critic, PPO, SAC (names only) |
| 8 | `s08_continuous_control.py` | `ContinuousControl` | **Continuous control.** Learning curve on a simulated system; Quadrotor only if RL was used (confirm) |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Act, observe, update; Closing line |

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
./kg check 10                     # validate manifest, scenes and narration
./kg render 10 -q l               # draft render (480p15); -q h for release
./kg assemble 10 -q l             # join the timeline into one video
./kg narrate 10 -q l --check-only # synthesise narration and check timing
```
