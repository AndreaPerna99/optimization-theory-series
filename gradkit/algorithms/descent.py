"""Keep the Gradient - Descent Methods (Episodes 1, 5, 6)

Gradient descent, heavy-ball momentum, projected gradient descent, Newton,
SGD, RMSprop and Adam, written exactly as in the episodes' precise statements.
"""
from __future__ import annotations

from collections.abc import Callable

import numpy as np

from gradkit.algorithms._common import StepSize, step_at

Grad = Callable[[np.ndarray], np.ndarray]


def gradient_descent(grad: Grad, x0, alpha: StepSize, steps: int) -> np.ndarray:
    """x_{k+1} = x_k - alpha_k grad f(x_k)  (Episode 1).

        Parameters
        ----------
        grad : callable
            Gradient of the objective.
        x0 : array-like
            Starting point.
        alpha : float or callable
            Step size or schedule.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [np.asarray(x0, dtype=float)]
    for k in range(steps):
        xs.append(xs[-1] - step_at(alpha, k) * grad(xs[-1]))
    return np.array(xs)


def heavy_ball(grad: Grad, x0, alpha: StepSize, beta: float, steps: int) -> np.ndarray:
    """x_{k+1} = x_k - alpha grad f(x_k) + beta (x_k - x_{k-1})  (Episode 1).

        Parameters
        ----------
        grad : callable
            Gradient of the objective.
        x0 : array-like
            Starting point; the method starts at rest (x_{-1} = x_0).
        alpha : float or callable
            Step size or schedule.
        beta : float
            Momentum coefficient, 0 <= beta < 1.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [np.asarray(x0, dtype=float)]
    prev = xs[0]
    for k in range(steps):
        x = xs[-1]
        xs.append(x - step_at(alpha, k) * grad(x) + beta * (x - prev))
        prev = x
    return np.array(xs)


def projected_gradient_descent(grad: Grad, project: Callable[[np.ndarray], np.ndarray],
                               x0, alpha: StepSize, steps: int) -> np.ndarray:
    """x_{k+1} = Pi_C(x_k - alpha grad f(x_k))  (Episode 1).

        Parameters
        ----------
        grad : callable
            Gradient of the objective.
        project : callable
            Euclidean projection onto the convex feasible set C.
        x0 : array-like
            Starting point (projected before the first step).
        alpha : float or callable
            Step size or schedule.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [project(np.asarray(x0, dtype=float))]
    for k in range(steps):
        xs.append(project(xs[-1] - step_at(alpha, k) * grad(xs[-1])))
    return np.array(xs)


def newton(grad: Grad, hess: Callable[[np.ndarray], np.ndarray], x0, steps: int) -> np.ndarray:
    """x_{k+1} = x_k - [hess f(x_k)]^{-1} grad f(x_k)  (Episode 5).

        Parameters
        ----------
        grad, hess : callable
            Gradient and Hessian of the objective.
        x0 : array-like
            Starting point.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [np.asarray(x0, dtype=float)]
    for _ in range(steps):
        x = xs[-1]
        xs.append(x - np.linalg.solve(hess(x), grad(x)))
    return np.array(xs)


def sgd(sample_grad: Callable[[np.ndarray, np.random.Generator], np.ndarray],
        x0, alpha: StepSize, steps: int, seed: int = 0) -> np.ndarray:
    """Stochastic gradient descent with an unbiased noisy gradient  (Episode 5).

        Parameters
        ----------
        sample_grad : callable
            (x, rng) -> a random gradient estimate whose mean is grad f(x),
            e.g. the gradient on a random minibatch.
        x0 : array-like
            Starting point.
        alpha : float or callable
            Step size or schedule. A constant step hovers in a noise region;
            a schedule with sum alpha_k = inf and sum alpha_k^2 < inf settles.
        steps : int
            Number of iterations.
        seed : int
            Seed, so every render of a scene shows the same path.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    rng = np.random.default_rng(seed)
    xs = [np.asarray(x0, dtype=float)]
    for k in range(steps):
        xs.append(xs[-1] - step_at(alpha, k) * sample_grad(xs[-1], rng))
    return np.array(xs)


def rmsprop(grad: Grad, x0, alpha: StepSize, steps: int, beta2: float = 0.9,
            eps: float = 1e-8) -> np.ndarray:
    """Per-coordinate step scaled by a running RMS of the gradient  (Episode 6).

        Parameters
        ----------
        grad : callable
            Gradient (or stochastic gradient) of the objective.
        x0 : array-like
            Starting point.
        alpha : float or callable
            Step size or schedule.
        steps : int
            Number of iterations.
        beta2 : float
            Decay of the squared-gradient average.
        eps : float
            Small constant against division by zero.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [np.asarray(x0, dtype=float)]
    v = np.zeros_like(xs[0])
    for k in range(steps):
        g = grad(xs[-1])
        v = beta2 * v + (1 - beta2) * g ** 2
        xs.append(xs[-1] - step_at(alpha, k) * g / (np.sqrt(v) + eps))
    return np.array(xs)


def adam(grad: Grad, x0, alpha: StepSize, steps: int, beta1: float = 0.9,
         beta2: float = 0.999, eps: float = 1e-8) -> np.ndarray:
    """Momentum plus per-coordinate scaling, with bias correction  (Episode 6).

        Parameters
        ----------
        grad : callable
            Gradient (or stochastic gradient) of the objective.
        x0 : array-like
            Starting point.
        alpha : float or callable
            Step size or schedule.
        steps : int
            Number of iterations.
        beta1, beta2 : float
            Decays of the gradient and squared-gradient averages.
        eps : float
            Small constant against division by zero.

        Returns
        -------
        numpy.ndarray
            Iterates, shape (steps + 1, n).
    """
    xs = [np.asarray(x0, dtype=float)]
    m = np.zeros_like(xs[0])
    v = np.zeros_like(xs[0])
    for k in range(steps):
        g = grad(xs[-1])
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g ** 2
        m_hat = m / (1 - beta1 ** (k + 1))
        v_hat = v / (1 - beta2 ** (k + 1))
        xs.append(xs[-1] - step_at(alpha, k) * m_hat / (np.sqrt(v_hat) + eps))
    return np.array(xs)
