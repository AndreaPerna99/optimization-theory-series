"""Keep the Gradient - Nonlinear Least Squares (Episode 5)

Minimize 1/2 ||r(theta)||^2 with residual r and Jacobian J. Gauss-Newton
solves (J^T J) Delta = -J^T r; Levenberg-Marquardt adds damping rho:
(J^T J + rho I) Delta = -J^T r, a short gradient-like step for large rho and
a Gauss-Newton step for small rho. Camera calibration refines its parameters
this way (Zhang's method: closed-form initialization, then LM).
"""
from __future__ import annotations

from collections.abc import Callable

import numpy as np

Residual = Callable[[np.ndarray], np.ndarray]


def gauss_newton(residual: Residual, jacobian: Residual, theta0, steps: int) -> np.ndarray:
    """Undamped Gauss-Newton iterations.

        Parameters
        ----------
        residual : callable
            theta -> residual vector r(theta).
        jacobian : callable
            theta -> Jacobian of r, shape (m, n).
        theta0 : array-like
            Initial parameters.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Parameter iterates, shape (steps + 1, n).
    """
    th = [np.asarray(theta0, dtype=float)]
    for _ in range(steps):
        r, J = residual(th[-1]), jacobian(th[-1])
        th.append(th[-1] + np.linalg.lstsq(J, -r, rcond=None)[0])
    return np.array(th)


def levenberg_marquardt(residual: Residual, jacobian: Residual, theta0, steps: int,
                        rho: float = 1e-2, up: float = 10.0, down: float = 0.1
                        ) -> tuple[np.ndarray, np.ndarray]:
    """Levenberg-Marquardt with the classic accept/reject damping update.

        Parameters
        ----------
        residual : callable
            theta -> residual vector r(theta).
        jacobian : callable
            theta -> Jacobian of r, shape (m, n).
        theta0 : array-like
            Initial parameters.
        steps : int
            Number of iterations (accepted or rejected).
        rho : float
            Initial damping.
        up, down : float
            Damping multipliers after a rejected / accepted step.

        Returns
        -------
        thetas : numpy.ndarray
            Accepted parameter iterates, shape (k + 1, n).
        rhos : numpy.ndarray
            Damping used at each accepted iterate, shape (k + 1,).
    """
    th = np.asarray(theta0, dtype=float)
    thetas, rhos = [th], [rho]
    cost = 0.5 * float(residual(th) @ residual(th))
    for _ in range(steps):
        r, J = residual(th), jacobian(th)
        delta = np.linalg.solve(J.T @ J + rho * np.eye(len(th)), -J.T @ r)
        cand = th + delta
        r_new = residual(cand)
        new_cost = 0.5 * float(r_new @ r_new)
        if new_cost < cost:
            th, cost, rho = cand, new_cost, rho * down
            thetas.append(th)
            rhos.append(rho)
        else:
            rho *= up
    return np.array(thetas), np.array(rhos)
