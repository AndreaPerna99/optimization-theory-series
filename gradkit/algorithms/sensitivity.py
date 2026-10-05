"""Keep the Gradient - Trajectory Sensitivity (Episode 4)

For x' = F(x, p), the sensitivity S = dx/dp obeys S' = (dF/dx) S + dF/dp.
To first order x(t; p + dp) ~ x(t; p) + S(t) dp, valid for small dp only.
"""
from __future__ import annotations

from collections.abc import Callable

import numpy as np

Field = Callable[[np.ndarray], np.ndarray]


def trajectory_sensitivity(F: Field, dF_dx: Field, dF_dp: Field, x0, S0, t_final: float,
                           dt: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Integrate the state and its parameter sensitivity together (RK4).

        Parameters
        ----------
        F : callable
            x -> x' at the nominal parameter (time-invariant).
        dF_dx : callable
            x -> Jacobian dF/dx, shape (n, n).
        dF_dp : callable
            x -> Jacobian dF/dp, shape (n, m).
        x0 : array-like, shape (n,)
            Initial state.
        S0 : array-like, shape (n, m)
            Initial sensitivity dx(0)/dp (zero if x0 does not depend on p).
        t_final : float
            Final time.
        dt : float
            Integration step.

        Returns
        -------
        t : numpy.ndarray
            Times, shape (N,).
        X : numpy.ndarray
            States, shape (N, n).
        S : numpy.ndarray
            Sensitivities, shape (N, n, m).
    """
    x = np.asarray(x0, dtype=float)
    S = np.asarray(S0, dtype=float).reshape(len(x), -1)

    def rhs(x, S):
        return F(x), dF_dx(x) @ S + np.asarray(dF_dp(x)).reshape(len(x), -1)

    n_steps = int(round(t_final / dt))
    ts, Xs, Ss = [0.0], [x], [S]
    for k in range(n_steps):
        k1 = rhs(x, S)
        k2 = rhs(x + dt / 2 * k1[0], S + dt / 2 * k1[1])
        k3 = rhs(x + dt / 2 * k2[0], S + dt / 2 * k2[1])
        k4 = rhs(x + dt * k3[0], S + dt * k3[1])
        x = x + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        S = S + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        ts.append((k + 1) * dt)
        Xs.append(x)
        Ss.append(S)
    return np.array(ts), np.array(Xs), np.array(Ss)
