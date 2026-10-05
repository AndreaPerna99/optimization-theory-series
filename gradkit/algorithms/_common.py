"""Keep the Gradient - Shared Helpers for the Numerics"""
from __future__ import annotations

from collections.abc import Callable

StepSize = float | Callable[[int], float]


def step_at(alpha: StepSize, k: int) -> float:
    """Return the step size used at iteration k.

        Parameters
        ----------
        alpha : float or callable
            A constant step, or a schedule k -> alpha_k.
        k : int
            Iteration index, starting at 0.

        Returns
        -------
        float
            The step size alpha_k.
    """
    return float(alpha(k)) if callable(alpha) else float(alpha)
