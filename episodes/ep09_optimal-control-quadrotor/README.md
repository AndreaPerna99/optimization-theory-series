# Episode 9 · Planning Through Time: Optimal Control and the Quadrotor

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 6, control half |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md), [Ep 3](../ep03_lagrange-kkt-svm/README.md), [Ep 4](../ep04_sensitivity-analysis/README.md) |
| Anchor | quadrotor (to confirm) |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** A quadrotor must fly through a gust to a target without exceeding its motor limits. It can't optimize once and stop; the world keeps pushing. How does it decide what to do at every instant?

**Technical content.**
- **Optimal control:** determining a sequence of actions that achieves a goal optimally over time; managing dynamic systems that require both immediate and long-term considerations.
- **Application areas:** autonomous vehicles, industrial automation, energy management.
- **The objective:** a cumulative cost over a time horizon (total energy, total error), balancing current cost against future outcomes.
- **Constraints and control inputs:** limits on actions, like speed or energy capacity, shaping the feasible space within physical and safety limits.
- **Methods** (not named in the PDF, required): the **Bellman principle** (dynamic programming), **LQR** as the clean classic case, and **MPC** as the practical workhorse.
- **Quadrotor project:** stability, path following, obstacle avoidance, adapting trajectory and control inputs to sudden disturbances and changing goals, ensuring both safety and efficiency.
- **Real-world applications:** smart energy grids balancing supply and demand at minimum cost while ensuring reliability; medical treatment (dose control that minimizes side effects while maximizing therapeutic benefit); industrial robotics (efficiency and precision in automated manufacturing).
- **Recap:** optimal control as a framework for adaptive, real-time decision-making in systems that operate under changing conditions.

**Precise statements.**
- *Discrete-time optimal control.* Minimize $\sum_{t=0}^{N-1} \ell(x_t, u_t) + \ell_N(x_N)$ subject to $x_{t+1} = F(x_t, u_t)$, $u_t \in \mathcal{U}$, $x_t \in \mathcal{X}$.
- *Bellman principle.* With value function $V_t(x)$ = the best achievable cost-to-go from state $x$ at time $t$: $V_t(x) = \min_{u}\big[\ell(x,u) + V_{t+1}(F(x,u))\big]$. A long problem breaks into "cost now plus value of where you land". (Reused in Episode 10.)
- *LQR.* Linear dynamics $x_{t+1} = A_d x_t + B_d u_t$ and quadratic cost $\ell = x^\top Q x + u^\top R u$ with $Q \succeq 0$, $R \succ 0$. The optimal control is linear state feedback $u_t = -K_t x_t$, with gains from the Riccati equation (constant $K$ on an infinite horizon under standard stabilizability/detectability conditions). $Q$ versus $R$ is the trade-off between accuracy and effort. (Use $A_d$, $B_d$ to avoid clashing with the LP and graph matrices.)
- *MPC (receding horizon).* At every time step: measure the current state, solve a finite-horizon optimal control problem with constraints, apply **only the first** control input, then repeat. With linear dynamics, quadratic cost and linear constraints, each step is a quadratic program solved with the tools of Episode 3; nonlinear dynamics give nonlinear MPC.
- *Quadrotor model (for exposition).* State: position, velocity, attitude and angular rates (12 states); inputs: four rotor thrusts. It is underactuated (four inputs, six degrees of freedom), so it must tilt to move sideways. **[CONFIRM]** the controller architecture actually used.

**Key visuals.**
- The Bellman principle as a backward sweep over a small grid of states.
- LQR with a $Q/R$ slider: aggressive versus gentle responses on a simple cart or quadrotor model.
- MPC on the quadrotor: the predicted trajectory (ghost path) redrawn every instant, only its first piece executed; a gust pushes the drone and the plan re-forms. Ideally over real flight footage **[CONFIRM]**.
- An input-saturation constraint visibly active in the plan.

**Project.** The quadrotor, exactly as the PDF describes. **[CONFIRM]**: hardware or simulation, controller (MPC, LQR, other), what disturbances and obstacles can be shown.

**Corrections.** The PDF names no methods; without LQR, Bellman and MPC the episode would stay at the level of definitions. MPC is constrained optimization repeated in real time, so it pays off Episodes 3 and 4 directly.

**Callbacks.** KKT/QP (3), sensitivity and robustness (4). Forward: Bellman in RL (10), the moving optimum (12).

**Closing line.** Plan far ahead, commit only to the next step, then look again. It's possibly the most practical advice in all of control theory.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_gust.py` | `HookGust` | **Flying through a gust.** Reach the target within motor limits; The world keeps pushing |
| 2 | `s02_control_problem.py` | `ControlProblem` | **The optimal control problem.** Cumulative cost over a horizon; Dynamics and input/state constraints |
| 3 | `s03_bellman.py` | `Bellman` | **The Bellman principle.** Cost now + value of where you land; Backward sweep over a grid of states |
| 4 | `s04_lqr.py` | `Lqr` | **LQR.** Optimal control is linear feedback u = -K x; Q/R slider: aggressive vs gentle |
| 5 | `s05_mpc.py` | `Mpc` | **Model predictive control.** Plan, apply the first input, re-plan; Each step a QP (Episode 3) |
| 6 | `s06_quadrotor_model.py` | `QuadrotorModel` | **The quadrotor.** 12 states, 4 thrusts, underactuated; Must tilt to move sideways |
| 7 | `s07_quadrotor_flight.py` | `QuadrotorFlight` | **The quadrotor flies.** Ghost plan redrawn every instant; Gust, re-plan, saturation active; Footage and controller (confirm) |
| 8 | `s08_applications.py` | `Applications` | **Beyond drones.** Energy grids, dose control, industrial robots; Autonomous vehicles and automation |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Adaptive real-time decisions; Closing line |

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
./kg check 9                     # validate manifest, scenes and narration
./kg render 9 -q l               # draft render (480p15); -q h for release
./kg assemble 9 -q l             # join the timeline into one video
./kg narrate 9 -q l --check-only # synthesise narration and check timing
```
