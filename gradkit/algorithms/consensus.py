"""Keep the Gradient - Graphs, Consensus and Distributed Optimization (Episodes 7, 8)

Consensus x_{k+1} = (I - eps L) x_k is gradient descent with step eps on the
disagreement 1/2 x^T L x, whose Hessian is the Laplacian L: it converges to
the average iff 0 < eps < 2 / lambda_n(L) on a connected undirected graph.
"""
from __future__ import annotations

from collections.abc import Callable, Sequence

import numpy as np

from gradkit.algorithms._common import StepSize, step_at


def laplacian(adjacency) -> np.ndarray:
    """L = D - A_G for an undirected (symmetric) adjacency matrix.

        Parameters
        ----------
        adjacency : array-like, shape (n, n)
            Symmetric nonnegative adjacency (edge weights), zero diagonal.

        Returns
        -------
        numpy.ndarray
            The Laplacian, shape (n, n).
    """
    A = np.asarray(adjacency, dtype=float)
    if not np.allclose(A, A.T):
        raise ValueError("adjacency must be symmetric (undirected graph)")
    return np.diag(A.sum(axis=1)) - A


def laplacian_spectrum(L) -> np.ndarray:
    """Eigenvalues 0 = lambda_1 <= ... <= lambda_n of a Laplacian."""
    return np.linalg.eigvalsh(np.asarray(L, dtype=float))


def algebraic_connectivity(L) -> float:
    """lambda_2(L): positive iff the graph is connected; sets the speed of agreement."""
    return float(laplacian_spectrum(L)[1])


def consensus_threshold(L) -> float:
    """Consensus converges iff 0 < eps < 2 / lambda_n(L) (connected graph)."""
    return 2.0 / float(laplacian_spectrum(L)[-1])


def consensus(L, x0, eps: float, steps: int) -> np.ndarray:
    """Average consensus x_{k+1} = (I - eps L) x_k.

        Parameters
        ----------
        L : array-like, shape (n, n)
            Graph Laplacian.
        x0 : array-like, shape (n,) or (n, d)
            Initial values, one row per agent.
        eps : float
            Consensus gain.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Values over time, shape (steps + 1, *x0.shape).
    """
    L = np.asarray(L, dtype=float)
    P = np.eye(len(L)) - eps * L
    xs = [np.asarray(x0, dtype=float)]
    for _ in range(steps):
        xs.append(P @ xs[-1])
    return np.array(xs)


def containment_matrix(L, followers: Sequence[int], leaders: Sequence[int]) -> np.ndarray:
    """H = -L_FF^{-1} L_FL: followers converge to x_F = H x_L.

    Rows of H are nonnegative and sum to 1 when every follower is reachable
    from some leader, so each follower ends in the leaders' convex hull.

        Parameters
        ----------
        L : array-like, shape (n, n)
            Laplacian of the whole graph.
        followers, leaders : sequence of int
            Index sets partitioning the agents.

        Returns
        -------
        numpy.ndarray
            H, shape (len(followers), len(leaders)).
    """
    L = np.asarray(L, dtype=float)
    F, Ld = list(followers), list(leaders)
    return -np.linalg.solve(L[np.ix_(F, F)], L[np.ix_(F, Ld)])


def dgd(W, grads: Sequence[Callable[[np.ndarray], np.ndarray]], x0, alpha: StepSize,
        steps: int) -> np.ndarray:
    """Distributed gradient descent x_i <- sum_j W_ij x_j - alpha grad f_i(x_i).

    With a constant step it only reaches a neighbourhood of the optimum whose
    size scales with alpha (Episode 8).

        Parameters
        ----------
        W : array-like, shape (n, n)
            Doubly stochastic mixing matrix, nonzero only between neighbours.
        grads : sequence of callable
            Local gradients, one per agent.
        x0 : array-like, shape (n, d)
            Initial local estimates.
        alpha : float or callable
            Step size or schedule.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Local estimates over time, shape (steps + 1, n, d).
    """
    W = np.asarray(W, dtype=float)
    xs = [np.asarray(x0, dtype=float)]
    for k in range(steps):
        x = xs[-1]
        G = np.array([g(xi) for g, xi in zip(grads, x)])
        xs.append(W @ x - step_at(alpha, k) * G)
    return np.array(xs)


def gradient_tracking(W, grads: Sequence[Callable[[np.ndarray], np.ndarray]], x0,
                      alpha: float, steps: int) -> np.ndarray:
    """Gradient tracking: each agent also runs consensus on the gradients.

    x^{k+1} = W x^k - alpha s^k,  s^{k+1} = W s^k + G(x^{k+1}) - G(x^k),
    s^0 = G(x^0). Converges exactly with a constant step (smooth, strongly
    convex f_i, connected graph, small alpha) (Episode 8).

        Parameters
        ----------
        W : array-like, shape (n, n)
            Doubly stochastic mixing matrix.
        grads : sequence of callable
            Local gradients, one per agent.
        x0 : array-like, shape (n, d)
            Initial local estimates.
        alpha : float
            Constant step size.
        steps : int
            Number of iterations.

        Returns
        -------
        numpy.ndarray
            Local estimates over time, shape (steps + 1, n, d).
    """
    W = np.asarray(W, dtype=float)

    def G(x):
        return np.array([g(xi) for g, xi in zip(grads, x)])

    xs = [np.asarray(x0, dtype=float)]
    s = G(xs[0])
    for _ in range(steps):
        x = xs[-1]
        x_new = W @ x - alpha * s
        s = W @ s + G(x_new) - G(x)
        xs.append(x_new)
    return np.array(xs)
