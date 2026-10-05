"""Keep the Gradient - Linear Programs (Episodes 2, 3, 4)

The factory LP: maximize c^T x subject to A x <= b, x >= 0. Its dual is
minimize b^T mu subject to A^T mu >= c, mu >= 0; at the optimum the values are
equal (strong duality) and mu_i is the shadow price of resource i.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

import numpy as np
from scipy.optimize import linprog


@dataclass(frozen=True)
class LPSolution:
    """Primal optimum, optimal value and shadow prices of a maximization LP."""

    x: np.ndarray
    value: float
    shadow_prices: np.ndarray


def solve_lp_max(c, A, b) -> LPSolution:
    """Solve maximize c^T x subject to A x <= b, x >= 0.

        Parameters
        ----------
        c : array-like, shape (n,)
            Profit per unit of each product.
        A : array-like, shape (m, n)
            Resource use per unit of each product.
        b : array-like, shape (m,)
            Resource availability.

        Returns
        -------
        LPSolution
            Optimal x, optimal value c^T x and the dual variables mu (shadow
            prices, mu_i = d value / d b_i while the binding set is unchanged).
    """
    c, A, b = (np.asarray(v, dtype=float) for v in (c, A, b))
    res = linprog(-c, A_ub=A, b_ub=b, bounds=[(0, None)] * len(c), method="highs")
    if res.status != 0:
        raise ValueError(f"LP not solved: {res.message}")
    # HiGHS reports d(min objective)/d b_ub; the maximized profit is its negative
    return LPSolution(x=res.x, value=float(-res.fun), shadow_prices=-res.ineqlin.marginals)


def vertices_2d(A, b, tol: float = 1e-9) -> np.ndarray:
    """Vertices of the 2D polygon {x : A x <= b}, ordered counter-clockwise.

        Parameters
        ----------
        A : array-like, shape (m, 2)
            Constraint normals. Include -I rows for x >= 0 if needed.
        b : array-like, shape (m,)
            Right-hand sides.
        tol : float
            Feasibility and de-duplication tolerance.

        Returns
        -------
        numpy.ndarray
            Vertices, shape (k, 2), ready for ``FeasibleRegion``.
    """
    A, b = np.asarray(A, dtype=float), np.asarray(b, dtype=float)
    pts = []
    for i, j in combinations(range(len(A)), 2):
        M = A[[i, j]]
        if abs(np.linalg.det(M)) < tol:
            continue
        p = np.linalg.solve(M, b[[i, j]])
        if np.all(A @ p <= b + tol) and not any(np.allclose(p, q, atol=1e-7) for q in pts):
            pts.append(p)
    if not pts:
        return np.zeros((0, 2))
    pts = np.array(pts)
    center = pts.mean(axis=0)
    order = np.argsort(np.arctan2(pts[:, 1] - center[1], pts[:, 0] - center[0]))
    return pts[order]
