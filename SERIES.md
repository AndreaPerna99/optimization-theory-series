# Keep the Gradient

**A Manim Video Series on Optimization Theory**

*Series bible: the idea, the rules, the notation and the map*

This file and the thirteen episode READMEs are the specification of the series. They were built from all 11 pages of the original `OptimizationTheoryPlan.pdf` (in [docs/source/](docs/source/)), including its three handwritten notes, and they are the source that scripts, storyboards and Manim scenes are built from, including by AI agents. Every technical topic from the PDF is kept, the imprecise ones are corrected, and each has a home in one connected story. [docs/COVERAGE.md](docs/COVERAGE.md) maps every item of the PDF to its episode.

| Document | Holds |
|---|---|
| [MESSAGE.md](MESSAGE.md) | the message of the series and how it may be delivered |
| **SERIES.md** (this file) | the core idea, audience and style, notation, visual language, series map |
| `episodes/epNN_*/README.md` | each episode's full specification: content, precise statements, visuals, corrections |
| [docs/COVERAGE.md](docs/COVERAGE.md) | every item of the original PDF and the episode that covers it |
| [docs/PRODUCTION.md](docs/PRODUCTION.md) | the pipeline, repository conventions and release order |
| [docs/OPEN_QUESTIONS.md](docs/OPEN_QUESTIONS.md) | what the author still has to decide or confirm |
| [docs/ASSESSMENT.md](docs/ASSESSMENT.md) | why the project is worth doing, and its risks |

> **Original working title (PDF):** *Optimization Theory: The Mechanics of Intelligent Solutions*. The handwritten note on page 1 renames the series **Keep the Gradient**, which the series adopts. The original subtitle can survive as a tagline or a playlist description.

---

## How to Use These Documents

These rules apply to anyone, human or agent, who builds material from this specification.

1. **The specification is authoritative.** If a script, storyboard or scene disagrees with SERIES.md or its episode README, the specification wins until it is changed explicitly. Change the specification first, then the material built from it.
2. **"Precise statements" are to be used as written.** Each episode README has a list of mathematical claims with their exact conditions. Narration may simplify the *wording* but must never drop a condition so that the claim becomes false. ("Convexity guarantees a unique minimum" is a typical error: it needs *strict* convexity.)
3. **Notation is global.** Use the symbols in [Notation and Conventions](#notation-and-conventions) in every episode. Do not introduce a new symbol for an existing object.
4. **Never invent project facts.** Anything about the author's own projects (quadrotor, SAR robots, calibration, research) that is not stated in the specification is marked **[CONFIRM]** and must be asked for, not made up. No invented numbers, results, footage or claims of what a system does.
5. **The math is the backbone.** The philosophical layer is at most two sentences per episode, at the end. It is never allowed to replace or distort a technical point.
6. **Every animation should be computed, not drawn.** Iterates, trajectories, consensus values, decision boundaries and so on are produced by actually running the algorithm (`gradkit.algorithms`) inside the scene, as in the earlier paper video, so the picture is correct by construction. The tests in `tests/` check the precise statements against that code.

---

## The Core Idea

### What the series is

An optimization theory course in video form. It runs from a single point feeling its way downhill, through limits, learning, cooperation and time, to systems that optimize without anyone in charge. The subject is optimization itself; applications and the author's projects are there to show the math working, not as the topic.

### Three layers per episode

**The mathematics** is the backbone and is never sacrificed. Every topic is explained properly, with formulas, and animated so that viewers understand *why* it works, not just what it is called.

**The projects** are the proof. The quadrotor, the SAR robots and camera calibration are where the math leaves the whiteboard. They make the series personal and hard to copy, but each one appears only where it illustrates the episode's theory.

**Keep the Gradient** is the meaning. Optimization is the mathematics of improving when you cannot see the whole landscape: you only feel the local slope, step, and feel again. Each episode closes with one or two quiet sentences about what its mathematics says about improvement, whether technological, collective or personal. Never more than that.

### Why the philosophical message is sound, and how to keep it honest

The metaphor works because it is mathematically literal. Gradient descent really does use only local information, and it really does reach the minimum of a convex function without ever seeing the whole landscape. But the honest version of the message also includes what gradient descent *cannot* do, and the series should say so, because that is what keeps the message from becoming a slogan:

- Local information can trap you in a local minimum (Episode 2). The series' answers are the same in mathematics as in life: noise (SGD, Episode 5), memory and momentum (Episodes 1 and 6), other people's information (Episodes 7 and 8), and exploration (Episode 10).
- Going faster is not always better: there is a step-size threshold beyond which you diverge (Episode 1).
- Some trade-offs cannot be optimized away; choosing among them is a value judgment (Episode 11).
- The landscape itself moves, so improvement never ends (Episode 12).

So "Keep the Gradient" does not mean "always go downhill". It means: keep sensing which way is better, keep taking steps, and stay humble about how much of the landscape you can see.

### The threads that tie the episodes together

These recurring ideas are what make the series one structure instead of a list of topics. Scripts should call them back explicitly.

| Thread | Where it appears |
|---|---|
| **The step and the slope.** One update rule, $x_{k+1} = x_k - \alpha \nabla f(x_k)$, and its step-size threshold. | Introduced in Ep 1; reappears as SGD (5), Adam (6), consensus (7), distributed GD (8), Q-learning (10), online tracking (12). |
| **Multipliers are prices are sensitivities.** One object seen four ways: dual variable, KKT force, shadow price, derivative of the optimum. | Shadow prices (2), wall forces (3), sensitivities (4), regularization weight (5), price of disagreement (8), market prices (11). |
| **Local information, global result.** Each agent or step sees only its neighbourhood, yet the whole converges. | Gradient (1), simplex (2), consensus (7), distributed GD (8), MPC (9), stigmergy (12). |
| **Corners and walls.** Optima live on the boundary of what is allowed. | LP vertices (2), active constraints (3), active-set changes (4), Lasso sparsity (5). |
| **The moving optimum.** Real optima drift. | Re-planning in MPC (9), the finale (12). |

---

## Audience and Style

**Target viewer.** Someone who knows single-variable calculus, has met vectors and matrices, and is curious: a strong high-school student, an engineering or science undergraduate, or a professional who wants the real picture. Partial derivatives, eigenvalues and graphs are explained when first used, briefly and visually. Episode 0 must be watchable by anyone.

**Tone rules.**
- Concrete before abstract: a picture or a problem first, then the formula.
- Every formula on screen is either explained term by term or not shown.
- No hype vocabulary ("revolutionary", "unsung hero", "limitless possibilities", "hidden engine"). The original PDF's introduction uses this register; the videos must not.
- Claims about applications are phrased at the level they are true. "Hospitals use optimization to schedule staff" is fine; "optimization saves lives every day" is not.
- Each episode opens with a hook: a question or a short visual problem that the episode answers.
- Recaps are short (30–60 s) and show, rather than list, the key ideas.

**Episode length.** Episodes 1–12 target 15–20 minutes, Episode 0 about 6–8 minutes. Lengths may vary with content; nothing should be padded to reach a target.

---

## Notation and Conventions

Use these everywhere. Where two fields traditionally use the same letter, this table decides.

| Symbol | Meaning |
|---|---|
| $x \in \mathbb{R}^n$ | decision variable (iterate $x_k$, optimum $x^\star$) |
| $f(x)$ | objective, always **minimized** unless explicitly stated; maximizing $u$ is written as minimizing $-u$ or stated as "maximize" in words |
| $\nabla f(x)$, $\nabla^2 f(x)$ | gradient, Hessian |
| $\alpha$ (or $\alpha_k$) | step size / learning rate. Used for *every* step size in the series (GD, SGD, Adam, DGD, Q-learning) |
| $\beta$ | momentum coefficient; $\beta_1, \beta_2$ in Adam |
| $h_j(x) = 0$ | equality constraints, multipliers $\lambda_j$ (any sign) |
| $g_i(x) \le 0$ | inequality constraints, multipliers $\mu_i \ge 0$ |
| $\mathcal{L}(x, \lambda, \mu)$ | Lagrangian, $f + \sum_j \lambda_j h_j + \sum_i \mu_i g_i$ |
| $\lambda_i(\cdot)$ | $i$-th eigenvalue of a symmetric matrix, ascending, e.g. $\lambda_2(L)$. Always written **with its argument** to distinguish it from a multiplier $\lambda_j$ |
| $M$, $m$ | curvature bounds: $\nabla^2 f(x) \preceq M I$ everywhere (holds when $\nabla f$ is $M$-Lipschitz); $\nabla^2 f(x) \succeq m I$ with $m > 0$ for strong convexity |
| $\kappa$ | condition number of a positive definite Hessian $H$, $\lambda_{\max}(H)/\lambda_{\min}(H)$ |
| $c, A, b$ | LP data: minimize/maximize $c^\top x$ subject to $Ax \le b$ |
| $\mu_i$ (in an LP) | LP dual variables / shadow prices. Written with the multiplier letter from Ep 2 on, because Ep 3 shows they *are* the KKT multipliers |
| $y$, $y_i$ | data: targets and labels (Ep 3 SVM, Ep 5, Ep 6) |
| $G = (V, E)$, $\mathcal{N}_i$ | communication graph, neighbours of agent $i$ |
| $A_G$, $D$, $L = D - A_G$ | adjacency, degree, and Laplacian matrices of the graph. ($A_G$ to avoid a clash with the LP matrix $A$.) |
| $W$ | mixing (weight) matrix in distributed algorithms |
| $\varepsilon$ | consensus gain |
| $x_i^k$ | in multi-agent algorithms the agent is the subscript and the iteration the superscript (Ep 8); single-agent iterates keep $x_k$ |
| $x_t, u_t$, $F(x,u)$, $\ell(x,u)$, $V(x)$ | control state, input, dynamics, stage cost, value function. Dynamics are always $F$, never $f$ (the objective) |
| $Q$, $R$ (matrices) | LQR state and input weights (Ep 9). The action-value function is always written with arguments, $Q(s,a)$ |
| $r$, $\gamma$, $Q(s,a)$, $\pi$ | RL reward, discount factor, action-value function, policy |
| $S(t) = \partial x(t)/\partial p$ | trajectory sensitivity to a parameter $p$ |

Damping in physical examples is written $\nu$ (never $\gamma$, which is the RL discount, and never $b$, which is the LP right-hand side). The SVM offset is written $w_0$ for the same reason. The small constant in RMSprop and Adam is written $\delta$ (the Adam paper calls it $\epsilon$).

**Local symbols.** A few letters have a second meaning inside a single episode, where the standard name is too well known to change. Each is defined on screen where it is used and never appears next to its other meaning: $\epsilon$ in *$\epsilon$-greedy* (Ep 10); $p$ as prices (Ep 11) and dropout probability (Ep 6); $\rho$ as Levenberg–Marquardt damping (Ep 5) and pheromone evaporation (Ep 12); $a$, $b$ as pheromone exponents (Ep 12).

---

## Visual Language

Recurring objects, so that viewers recognize ideas across episodes. The exact palette and Manim style module are defined separately (see [docs/PRODUCTION.md](docs/PRODUCTION.md) and `gradkit/style.py`), but the meanings are fixed here.

| Object | Represents | First appears |
|---|---|---|
| **The ball** on a landscape | the current iterate $x_k$ | Ep 0 |
| **Level curves** (contour map) | the objective seen from above; the gradient is always perpendicular to them | Ep 1 |
| **Arrow from the ball** | the negative gradient, the step direction | Ep 1 |
| **Shaded region / walls** | the feasible set and its constraints | Ep 1 (preview), Ep 2 |
| **Force arrow from a wall** | a multiplier $\mu_i$: how hard the constraint pushes back | Ep 3 |
| **Price tag on a constraint** | a shadow price / sensitivity | Ep 2, Ep 4 |
| **Dots joined by lines** | agents on a communication graph | Ep 7 |
| **Ghost trajectories** | a plan (MPC horizon, predicted path) as opposed to what actually happens | Ep 9 |

---

## Series Map

The PDF has eight videos. Videos 3, 4, 5 and 6 each contain two videos' worth of material, and Video 7 splits naturally into society and self-organization. To cover everything without rushing, the series has **thirteen episodes (0–12)**.

| Ep | Title | From PDF | Anchor example / project |
|---|---|---|---|
| 0 | [Keep the Gradient (prologue)](episodes/ep00_keep-the-gradient/README.md) | Video 0 | quadrotor cold open **[CONFIRM footage]** |
| 1 | [Which Way Is Down? Gradient Descent](episodes/ep01_gradient-descent/README.md) | Video 1 | landscape, damped pendulum |
| 2 | [Corners and Bowls: Linear Programming and Convexity](episodes/ep02_linear-programming-convexity/README.md) | Video 2 | production/logistics LP |
| 3 | [Walls: Lagrange Multipliers, KKT and SVM](episodes/ep03_lagrange-kkt-svm/README.md) | Video 3 (first half) | SVM |
| 4 | [What If the World Changes? Sensitivity Analysis](episodes/ep04_sensitivity-analysis/README.md) | Video 3 (second half) | beam/truss, budget, robot toy |
| 5 | [Learning From Error: Loss, Least Squares and Regularization](episodes/ep05_loss-least-squares-regularization/README.md) | Video 4 (first half) + note | **camera calibration** |
| 6 | [Deep Landscapes: Neural Network Optimization](episodes/ep06_neural-network-optimization/README.md) | Video 4 (second half) | image and text classifiers |
| 7 | [Many Minds: Graphs and Consensus](episodes/ep07_graphs-consensus/README.md) | Video 5 (first half) | swarm alignment |
| 8 | [Searching Together: Distributed Gradient Descent and SAR Robots](episodes/ep08_distributed-gd-sar/README.md) | Video 5 (second half) | **SAR robots** |
| 9 | [Planning Through Time: Optimal Control and the Quadrotor](episodes/ep09_optimal-control-quadrotor/README.md) | Video 6 (control) | **quadrotor** |
| 10 | [Learning to Act: Reinforcement Learning](episodes/ep10_reinforcement-learning/README.md) | Video 6 (RL) | grid world, continuous control |
| 11 | [Beyond Engineering: Economics, Fairness and Society](episodes/ep11_economics-fairness-society/README.md) | Video 7 (first half) | markets, Pareto front |
| 12 | [Self-Organization and the Moving Optimum (finale)](episodes/ep12_self-organization-moving-optimum/README.md) | Video 7 (second half) + wrap-up | ants, flocks, moving target |

**Dependencies.** 1 → 2 → 3 → 4 is the spine and must be watched in order. 5 needs 1 and 3; 6 needs 1, 3 and 5. 7 needs 1; 8 needs 1, 3 and 7 (3 for the multiplier callback). 9 needs 1, 3 and 4. 10 needs 9. 11 needs 2 and 3. 12 draws on everything. Episode 0 is a standalone trailer. The same lists are in each episode's `episode.toml` (`depends_on`).

---
