# Episode 5 · Learning From Error: Loss, Least Squares and Regularization

| | |
|---|---|
| Series | [Keep the Gradient](../../SERIES.md) |
| Status | in [episode.toml](episode.toml); all episodes: `./kg status` |
| Target length | ~20 min |
| From the original PDF | Video 4, first half + handwritten note |
| Watch first | [Ep 1](../ep01_gradient-descent/README.md), [Ep 3](../ep03_lagrange-kkt-svm/README.md) |
| Anchor | camera calibration (setup to confirm) |

This README is the authoritative specification of the episode. Series-wide rules, the notation table and the visual language are in [SERIES.md](../../SERIES.md) and apply here without being repeated. Any fact about the author's projects that is not stated here is unknown: ask the author, never invent it (open points are marked **CONFIRM**).

## Specification

**Central question.** A camera looks at a checkerboard. How does it figure out its own lens?

**Technical content.**
- **Opening project: camera calibration.** The handwritten note asks to talk about optimization in computer vision, such as camera calibration. It opens the episode because it is learning from error in its purest, most visible form.
- **Least squares and Newton-type methods:** calibration is nonlinear least squares, solved with Gauss–Newton or Levenberg–Marquardt. This is where the series introduces **Newton's method** (using curvature, not just slope), which is missing from the PDF and needed.
- **Cost functions in ML:** mean squared error for regression, cross-entropy for classification, and how they guide a model toward accurate predictions.
- **Gradient descent and SGD in ML:** SGD as an efficient variant for large datasets, using small random batches.
- **Overfitting and underfitting:** examples where a model fails to generalize (overfit) or fails to capture key patterns (underfit).
- **Regularization:** L1 (Lasso) and L2 (Ridge) as techniques to prevent overfitting by penalizing complexity. (Dropout, also listed here in the PDF, moves to Episode 6, where neural networks are introduced.)
- **The link to KKT** that the PDF promises: regularization is a constraint in disguise.

**Precise statements.**
- *Newton's method.* $x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1}\nabla f(x_k)$: jump to the minimum of the local quadratic model. It solves a strictly convex quadratic (positive definite Hessian) in one step and converges very fast (quadratically) near a minimum with positive definite Hessian, but each step is expensive and it can fail far from the minimum.
- *Nonlinear least squares.* Minimize $\tfrac12\|r(\theta)\|^2$ with residual vector $r$ and Jacobian $J$. Gauss–Newton step: solve $(J^\top J)\,\Delta = -J^\top r$. Levenberg–Marquardt step: solve $(J^\top J + \rho I)\,\Delta = -J^\top r$ with damping $\rho > 0$. Large $\rho$ gives a short gradient-descent-like step; small $\rho$ gives a Gauss–Newton step. (Use $\rho$, not $\lambda$, to avoid a clash with multipliers.)
- *Camera calibration.* Parameters: intrinsics (focal lengths, principal point), lens distortion coefficients, and one pose (rotation, translation) per image. Objective: the total **reprojection error**, the sum over images and checkerboard corners of the squared distance between where a corner is detected and where the camera model projects it. Standard pipeline (Zhang's method): closed-form initial estimate from the board images, then Levenberg–Marquardt refinement. The problem is non-convex, so the initial estimate matters (callback to Ep 2).
- *Losses.* MSE: $\frac1N\sum_i (y_i - \hat y_i)^2$. Cross-entropy: $-\sum_c y_c \log p_c$ for a one-hot label $y$ and predicted probabilities $p$. For linear and logistic regression these losses are convex in the weights; for neural networks they are not.
- *SGD.* Using the gradient of one random sample (or a minibatch of size $B$) gives an **unbiased but noisy** estimate of the full gradient; averaging over $B$ samples divides its variance by $B$. With a constant step, SGD does not settle exactly; it hovers in a noisy region around the minimum whose size grows with $\alpha$. Decreasing steps (with $\sum_k \alpha_k = \infty$ and $\sum_k \alpha_k^2 < \infty$) remove the noise floor in convex settings. **This** is where "a smaller step is more precise" becomes true.
- *Over- and underfitting.* Training error keeps falling as model complexity grows; validation error first falls, then rises. Overfitting is the gap.
- *Ridge and Lasso.* Ridge: minimize $\text{loss}(w) + \lambda\|w\|_2^2$. Lasso: minimize $\text{loss}(w) + \lambda\|w\|_1$.
- *Constraint in disguise.* For a convex loss, the penalized problem with weight $\lambda > 0$ has the same solution as minimizing the loss subject to the matching constraint ($\|w\|_2^2 \le t$ for Ridge, $\|w\|_1 \le t$ for Lasso) for a suitable $t$, namely the penalty's value at that solution; the penalty weight $\lambda$ is exactly the KKT multiplier $\mu$ of that constraint ($\lambda = \mu$; the penalty keeps its traditional letter). The L2 ball is round; the L1 ball is a diamond with corners on the axes. The loss contours typically first touch the diamond at a corner, where some weights are **exactly zero**: that is why Lasso gives sparse models. Ridge shrinks weights but rarely makes them exactly zero.

**Key visuals.**
- Calibration: reprojection residual arrows on the checkerboard corners shrinking as Levenberg–Marquardt iterates; the distorted image straightening.
- Gradient descent versus Newton on the same bowl: many small steps versus one jump.
- SGD's noisy path trending downhill, then hovering; a decreasing step size calming it.
- Overfitting: a polynomial fit going from a straight line (underfit) to a wiggle through every point (overfit), with training and validation error curves beside it.
- The diamond and the circle with loss contours, the touching point snapping to a corner for L1.

**Project.** Camera calibration. **[CONFIRM]** whether the author has their own calibration setup or footage (real board, real residuals), or whether a simulated camera is used.

**Corrections.**
- The PDF says SGD "updates weights in batches, making it well-suited for large datasets". The defining feature is not batching itself: it is using a random sample to get a cheap, unbiased but noisy estimate of the true gradient. The noise is the interesting part (and may help escape shallow minima, which can be said as an observation, not a guarantee).
- The PDF promises a link to KKT that never appears in its outline; it is the regularization-as-constraint result above.

**Callbacks.** Step size (1), corners (2), multipliers (3). Forward: deep networks (6).

**Closing line.** Error is the most honest feedback there is. But learning the past too perfectly makes you worse at the future: regularization is mathematical humility.

## Production

### Scenes

The timeline in [episode.toml](episode.toml) is the playback order. Every scene starts as a placeholder card (`PlaceholderScene`) so the episode renders and assembles end to end from day one; `./kg status` counts the placeholders left.

| # | File | Class | Shows |
|---|---|---|---|
| 0 | `s00_title.py` | `Title` | Episode title card |
| 1 | `s01_hook_calibration.py` | `HookCalibration` | **A camera calibrates itself.** Checkerboard, detected vs projected corners; Calibration setup (confirm) |
| 2 | `s02_reprojection_error.py` | `ReprojectionError` | **Reprojection error.** Intrinsics, distortion, one pose per image; Sum of squared corner residuals |
| 3 | `s03_newton.py` | `Newton` | **Newton's method.** Use curvature, not just slope; One step on a quadratic vs many GD steps |
| 4 | `s04_gauss_newton_lm.py` | `GaussNewtonLm` | **Gauss-Newton and Levenberg-Marquardt.** (J^T J + rho I) Delta = -J^T r; Residual arrows shrinking, image straightening; Zhang: closed-form start, then LM; start matters |
| 5 | `s05_losses.py` | `Losses` | **Loss functions.** MSE for regression, cross-entropy for classification; Convex for linear/logistic models, not for networks |
| 6 | `s06_sgd_noise.py` | `SgdNoise` | **Stochastic gradient descent.** Random minibatch: unbiased but noisy; Constant step hovers; decreasing step settles |
| 7 | `s07_overfitting.py` | `Overfitting` | **Overfitting and underfitting.** Line -> wiggle through every point; Training vs validation error |
| 8 | `s08_ridge_lasso.py` | `RidgeLasso` | **Ridge and Lasso.** Penalties lambda ‖w‖_2^2 and lambda ‖w‖_1; Shrinkage vs sparsity |
| 9 | `s09_constraint_in_disguise.py` | `ConstraintInDisguise` | **Regularization is a constraint.** Penalty = constraint with multiplier lambda; Diamond corners give exact zeros |
| 10 | `s10_recap_closing.py` | `RecapClosing` | **Recap and closing.** Error is honest feedback; regularization is humility; Closing line |

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
./kg check 5                     # validate manifest, scenes and narration
./kg render 5 -q l               # draft render (480p15); -q h for release
./kg assemble 5 -q l             # join the timeline into one video
./kg narrate 5 -q l --check-only # synthesise narration and check timing
```
