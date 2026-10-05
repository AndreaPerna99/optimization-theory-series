"""Keep the Gradient - Optimal Control (Episode 9)

Discrete-time LQR: x_{t+1} = A_d x_t + B_d u_t, cost sum x^T Q x + u^T R u,
optimal control u_t = -K x_t with K from the discrete algebraic Riccati
equation. MPC (receding horizon) is to be added for the quadrotor scenes.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import solve_discrete_are


def dlqr(A_d, B_d, Q, R) -> tuple[np.ndarray, np.ndarray]:
    """Infinite-horizon discrete LQR gain.

        Parameters
        ----------
        A_d, B_d : array-like
            Discrete-time dynamics matrices.
        Q : array-like
            State weight, positive semidefinite.
        R : array-like
            Input weight, positive definite.

        Returns
        -------
        K : numpy.ndarray
            Feedback gain, u = -K x.
        P : numpy.ndarray
            Riccati solution; x^T P x is the optimal cost-to-go.
    """
    A_d, B_d, Q, R = (np.atleast_2d(np.asarray(v, dtype=float)) for v in (A_d, B_d, Q, R))
    P = solve_discrete_are(A_d, B_d, Q, R)
    K = np.linalg.solve(R + B_d.T @ P @ B_d, B_d.T @ P @ A_d)
    return K, P


def simulate_linear(A_d, B_d, K, x0, steps: int) -> tuple[np.ndarray, np.ndarray]:
    """Closed loop x_{t+1} = (A_d - B_d K) x_t.

        Parameters
        ----------
        A_d, B_d : array-like
            Discrete-time dynamics matrices.
        K : array-like
            Feedback gain.
        x0 : array-like
            Initial state.
        steps : int
            Number of steps.

        Returns
        -------
        xs : numpy.ndarray
            States, shape (steps + 1, n).
        us : numpy.ndarray
            Inputs, shape (steps, m).
    """
    A_d, B_d, K = (np.atleast_2d(np.asarray(v, dtype=float)) for v in (A_d, B_d, K))
    xs, us = [np.asarray(x0, dtype=float)], []
    for _ in range(steps):
        u = -K @ xs[-1]
        us.append(u)
        xs.append(A_d @ xs[-1] + B_d @ u)
    return np.array(xs), np.array(us)


def mpc_step(*args, **kwargs):
    """One receding-horizon step: solve the finite-horizon constrained problem
    from the current state and return only the first input (Episode 9).

    Specification: linear dynamics, quadratic cost, box input constraints,
    solved as a QP; return the first input AND the full predicted trajectory,
    which the scenes draw as a ``GhostPath``.
    """
    raise NotImplementedError("mpc_step: implement before Episode 9")
