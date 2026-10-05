# Episode 1 · Which Way Is Down? Gradient Descent

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | 15–20 min |
| From the original PDF | Video 1, complete |
| Watch first | none |
| Anchor | landscape, damped pendulum |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it.

## Specification

**Central question.** You are blindfolded on a hillside and want to reach the lowest point. What do you do?

**Technical content.**
- **Objective functions and constraints.** The objective as the goal (minimize error, maximize profit); constraints as rules the solution must satisfy (a budget cap). A simple 2D graph shows a feasible region defined by budget or time limits; this sets up constrained problems later.
- **The gradient** as the vector of partial derivatives, pointing in the direction of steepest increase and perpendicular to level curves. Knowing this direction tells you which way leads toward (or away from) lower values.
- **Gradient descent** as an iterative method that moves opposite to the gradient. The key formula, presented early, as in the PDF:

$$
x_{k+1} = x_k - \alpha_k \nabla f(x_k)
$$

- **Iterations:** each step refines the solution; the step-by-step path on a cost landscape.
- **Step size $\alpha$:** larger steps can be faster but risk instability; too small and progress crawls. The threshold that separates the two (below).
- **Ill-conditioning:** the narrow valley where gradient descent zigzags. This is the honest reason faster methods exist, and it is paid off in Episode 6.
- **Momentum,** introduced through the pendulum (see Corrections).
- **Constraints, briefly:** projected gradient descent (take a step, then project back onto the feasible region), as a preview of Episodes 2–3.
- **Examples:** a physics example (potential energy, the pendulum), a machine learning example (reducing error when predicting prices or classifying images), and a data science example (reducing the mean squared error of a forecast).
- **3D cost landscape:** gradient descent navigating down slopes toward the minimum.
- **Practical takeaways:** the step size matters, and gradient descent is used everywhere because it is simple, cheap per step, and effective.
- **Preview:** gradient descent is one tool among many; next, linear problems, convexity and duality.

**Precise statements.**
- *Steepest ascent.* Among unit directions $d$, the directional derivative $\nabla f(x)^\top d$ is largest for $d = \nabla f(x)/\|\nabla f(x)\|$ (Cauchy–Schwarz). The gradient is perpendicular to the level set through $x$.
- *Descent.* For small enough $\alpha > 0$, $f(x - \alpha \nabla f(x)) \approx f(x) - \alpha \|\nabla f(x)\|^2 < f(x)$ whenever $\nabla f(x) \neq 0$.
- *Stationary points.* $\nabla f(x) = 0$ at minima, maxima and saddle points alike. Gradient descent stops at any of them in principle, which is why the landscape's shape matters (Episode 2).
- *Step-size threshold (quadratic case, exact).* For $f(x) = \tfrac12 x^\top H x$ with $H$ symmetric positive definite, gradient descent with constant $\alpha$ multiplies the error along each eigenvector of $H$ by $(1 - \alpha \lambda_i(H))$ per step. It converges for every starting point **if and only if** $0 < \alpha < 2/\lambda_{\max}(H)$, and if $\alpha > 2/\lambda_{\max}(H)$ it diverges from almost every starting point (any start with a component along the top eigenvector).
- *General smooth case.* If the curvature is bounded, $\nabla^2 f(x) \preceq M I$ everywhere (true in particular when $\nabla f$ is $M$-Lipschitz), any constant $\alpha < 2/M$ decreases $f$ at every non-stationary step (descent lemma: $f(x_{k+1}) \le f(x_k) - \alpha(1 - \alpha M/2)\|\nabla f(x_k)\|^2$). Above the threshold divergence is possible but not guaranteed; do not claim it is.
- *Conditioning.* On the quadratic, the best constant step $\alpha = 2/\big(\lambda_{\min}(H) + \lambda_{\max}(H)\big)$ shrinks the error by at most $(\kappa - 1)/(\kappa + 1)$ per step, with $\kappa = \lambda_{\max}(H)/\lambda_{\min}(H)$. Large $\kappa$ means slow, zigzagging progress: the step is limited by the steepest direction and crawls along the flattest.
- *Momentum (heavy ball).* $x_{k+1} = x_k - \alpha \nabla f(x_k) + \beta (x_k - x_{k-1})$, with $0 \le \beta < 1$.
- *Projected gradient descent.* $x_{k+1} = \Pi_C\big(x_k - \alpha \nabla f(x_k)\big)$, where $\Pi_C$ is the closest point in a convex feasible set $C$.

**Key visuals.**
- A slider on $\alpha$ on a 2D quadratic bowl, showing smooth convergence, then oscillation, then explosion as $\alpha$ crosses $2/\lambda_{\max}(H)$. One of the best shots of the series.
- The same descent seen as a 3D landscape and as a contour map, with the gradient arrow perpendicular to the level curves.
- The zigzag in a narrow valley, with $\kappa$ on screen.
- A damped pendulum next to the heavy-ball iterates on the same potential.

**Corrections.**
- The PDF says a smaller step "is more precise but may slow progress". For deterministic gradient descent that is not true: the minimum is a fixed point for any stable step, so small steps are slower but no more precise. (It *is* true for SGD, where a smaller step means less noise; save this for Episode 5.)
- The pendulum is not doing gradient descent. A damped pendulum obeys $\ddot\theta + \nu\dot\theta + \nabla U(\theta) = 0$ with $U(\theta) = (g/\ell)(1 - \cos\theta)$: it has inertia, overshoots and swings before settling. The heavy-ball method is a discretization of exactly this kind of dynamics, so use the pendulum to introduce **momentum**. In the heavily damped limit (a pendulum in honey) the motion becomes the gradient flow $\dot\theta = -\nabla U(\theta)/\nu$, which *is* continuous-time gradient descent. Both facts make the physics example correct and useful.

**Callbacks forward.** The $2/\lambda_{\max}(H)$ threshold reappears exactly in consensus (Ep 7). The zigzag is resolved in Ep 6.

**Closing line.** You don't need to see the minimum to reach it: local information, applied consistently, is enough. And pace matters: past a certain speed, you overshoot instead of arriving.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_blindfold.py` | `HookBlindfold` | **The blindfolded hiker.** Central question: reach the lowest point without seeing; The ball on a landscape |
| 2 | `s02_objective_constraints.py` | `ObjectiveConstraints` | **Objectives and constraints.** Objective: minimize error / maximize profit; Constraints: a budget cap; 2D feasible region from budget or time limits |
| 3 | `s03_gradient.py` | `Gradient` | **The gradient.** Partial derivatives as a vector; Steepest ascent (Cauchy-Schwarz), perpendicular to level curves; 3D landscape and contour map side by side |
| 4 | `s04_descent_rule.py` | `DescentRule` | **The descent rule.** x_{k+1} = x_k - alpha grad f(x_k), term by term; Iterates refining step by step on the landscape; Examples: predicting prices, MSE of a forecast |
| 5 | `s05_step_size.py` | `StepSize` | **The step-size threshold.** Slider on alpha: converge, oscillate, explode; Threshold 2 / lambda_max(H); Small steps: slower, not more precise |
| 6 | `s06_ill_conditioning.py` | `IllConditioning` | **The narrow valley.** Zigzag in an elongated bowl; Condition number kappa on screen; Rate (kappa - 1)/(kappa + 1) |
| 7 | `s07_pendulum_momentum.py` | `PendulumMomentum` | **The pendulum and momentum.** Damped pendulum next to heavy-ball iterates; Inertia overshoots: that is momentum; Pendulum in honey = gradient flow |
| 8 | `s08_projected_preview.py` | `ProjectedPreview` | **Respecting constraints.** Projected gradient descent: step, then project; Preview of linear programming and duality |
| 9 | `s09_recap_closing.py` | `RecapClosing` | **Recap and closing.** Step size matters; GD is simple, cheap and effective; Closing line |

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
./kg check 1                     # validate manifest, scenes and narration
./kg render 1 -q l               # draft render (480p15); -q h for release
./kg assemble 1 -q l             # join the timeline into one video
./kg narrate 1 -q l --check-only # synthesise narration and check timing
```
