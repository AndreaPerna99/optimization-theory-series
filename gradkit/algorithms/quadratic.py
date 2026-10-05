"""Keep the Gradient - Quadratic Objectives (Episodes 1, 6, 7)

f(x) = 1/2 (x - c)^T H (x - c) with H symmetric positive definite: the model
problem for the step-size threshold, the condition number and the zigzag.
"""
from __future__ import annotations

import numpy as np


class Quadratic:
    """A positive definite quadratic bowl with its spectral facts."""

    def __init__(self, H, center=None) -> None:
        """Create the quadratic.

            Parameters
            ----------
            H : array-like, shape (n, n)
                Symmetric positive definite Hessian.
            center : array-like, shape (n,), optional
                The minimizer c. Defaults to the origin.

            Returns
            -------
            None
        """
        self.H = np.asarray(H, dtype=float)
        if not np.allclose(self.H, self.H.T):
            raise ValueError("H must be symmetric")
        self.eigenvalues = np.linalg.eigvalsh(self.H)
        if self.eigenvalues[0] <= 0:
            raise ValueError("H must be positive definite")
        self.center = np.zeros(len(self.H)) if center is None else np.asarray(center, dtype=float)

    def f(self, x) -> float:
        """Objective value."""
        d = np.asarray(x, dtype=float) - self.center
        return 0.5 * float(d @ self.H @ d)

    def grad(self, x) -> np.ndarray:
        """Gradient H (x - c)."""
        return self.H @ (np.asarray(x, dtype=float) - self.center)

    def hess(self, x=None) -> np.ndarray:
        """Hessian H (constant)."""
        return self.H

    @property
    def kappa(self) -> float:
        """Condition number lambda_max(H) / lambda_min(H)."""
        return float(self.eigenvalues[-1] / self.eigenvalues[0])

    def step_threshold(self) -> float:
        """Gradient descent converges iff 0 < alpha < 2 / lambda_max(H) (Episode 1)."""
        return 2.0 / float(self.eigenvalues[-1])

    def best_step(self) -> float:
        """The constant step 2 / (lambda_min(H) + lambda_max(H))."""
        return 2.0 / float(self.eigenvalues[0] + self.eigenvalues[-1])

    def contraction(self, alpha: float) -> float:
        """Per-step error factor max_i |1 - alpha lambda_i(H)|; < 1 means convergence."""
        return float(np.max(np.abs(1.0 - alpha * self.eigenvalues)))
