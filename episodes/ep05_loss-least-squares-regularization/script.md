# Episode 5 · Script and Shot List

Draft narration and on-screen plan, scene by scene, in timeline order. The
specification is [README.md](README.md); notation, tone rules and the visual
language are in [SERIES.md](../../SERIES.md). When a scene's narration is final,
move it into [narration.toml](narration.toml) as timed segments.

**Status:** not started.

---

## s00 · Title (`Title`)

**On screen:** the episode title card.

**Narration:** none.

## s01 · A camera calibrates itself (`HookCalibration`)

**On screen (from the spec):**
- Checkerboard, detected vs projected corners
- Calibration setup [CONFIRM]

**Narration draft:**

> TODO

## s02 · Reprojection error (`ReprojectionError`)

**On screen (from the spec):**
- Intrinsics, distortion, one pose per image
- Sum of squared corner residuals

**Narration draft:**

> TODO

## s03 · Newton's method (`Newton`)

**On screen (from the spec):**
- Use curvature, not just slope
- One step on a quadratic vs many GD steps

**Narration draft:**

> TODO

## s04 · Gauss-Newton and Levenberg-Marquardt (`GaussNewtonLm`)

**On screen (from the spec):**
- (J^T J + rho I) Delta = -J^T r
- Residual arrows shrinking, image straightening
- Zhang: closed-form start, then LM; start matters

**Narration draft:**

> TODO

## s05 · Loss functions (`Losses`)

**On screen (from the spec):**
- MSE for regression, cross-entropy for classification
- Convex for linear/logistic models, not for networks

**Narration draft:**

> TODO

## s06 · Stochastic gradient descent (`SgdNoise`)

**On screen (from the spec):**
- Random minibatch: unbiased but noisy
- Constant step hovers; decreasing step settles

**Narration draft:**

> TODO

## s07 · Overfitting and underfitting (`Overfitting`)

**On screen (from the spec):**
- Line -> wiggle through every point
- Training vs validation error

**Narration draft:**

> TODO

## s08 · Ridge and Lasso (`RidgeLasso`)

**On screen (from the spec):**
- Penalties lambda ||w||_2^2 and lambda ||w||_1
- Shrinkage vs sparsity

**Narration draft:**

> TODO

## s09 · Regularization is a constraint (`ConstraintInDisguise`)

**On screen (from the spec):**
- Penalty = constraint with multiplier lambda
- Diamond corners give exact zeros

**Narration draft:**

> TODO

## s10 · Recap and closing (`RecapClosing`)

**On screen (from the spec):**
- Error is honest feedback; regularization is humility
- Closing line

**Narration draft:**

> TODO
