"""Keep the Gradient - Checks of the Precise Statements

Each test checks one mathematical claim from an episode's "Precise statements"
against the numerics the animations are computed from. If a test here fails,
either the code or the claim in the episode README is wrong; fix the one that
is wrong, never relax the test to make it pass.
"""
from __future__ import annotations

import numpy as np

from gradkit.algorithms import consensus as cons
from gradkit.algorithms.control import dlqr, simulate_linear
from gradkit.algorithms.descent import (adam, gradient_descent, heavy_ball, newton,
                                        projected_gradient_descent, sgd)
from gradkit.algorithms.least_squares import gauss_newton, levenberg_marquardt
from gradkit.algorithms.lp import solve_lp_max, vertices_2d
from gradkit.algorithms.quadratic import Quadratic
from gradkit.algorithms.sensitivity import trajectory_sensitivity

BOWL = Quadratic([[10.0, 0.0], [0.0, 1.0]], center=[1.0, -1.0])
X0 = np.array([-2.0, 2.0])


# --- Episode 1 ---------------------------------------------------------------

def test_step_threshold_is_exact_on_quadratics():
    """GD converges iff 0 < alpha < 2 / lambda_max(H)."""
    t = BOWL.step_threshold()
    below = gradient_descent(BOWL.grad, X0, 0.95 * t, 400)
    above = gradient_descent(BOWL.grad, X0, 1.05 * t, 400)
    assert np.allclose(below[-1], BOWL.center, atol=1e-6)
    assert np.linalg.norm(above[-1] - BOWL.center) > 1e3


def test_best_step_rate_matches_condition_number():
    """With alpha = 2/(lmin + lmax) the error factor is (kappa - 1)/(kappa + 1)."""
    k = BOWL.kappa
    assert np.isclose(BOWL.contraction(BOWL.best_step()), (k - 1) / (k + 1))


def test_heavy_ball_converges_on_bowl():
    xs = heavy_ball(BOWL.grad, X0, 0.05, 0.6, 400)
    assert np.allclose(xs[-1], BOWL.center, atol=1e-6)


def test_projected_gd_stays_feasible_and_finds_boundary_optimum():
    """Minimum of the bowl restricted to the box [-1, 0]^2 lies on the boundary."""
    proj = lambda x: np.clip(x, -1.0, 0.0)  # noqa: E731
    xs = projected_gradient_descent(BOWL.grad, proj, X0, 0.05, 500)
    assert np.all((xs >= -1.0) & (xs <= 0.0))
    assert np.allclose(xs[-1], [0.0, -1.0], atol=1e-6)


# --- Episode 5 ---------------------------------------------------------------

def test_newton_solves_a_quadratic_in_one_step():
    xs = newton(BOWL.grad, BOWL.hess, X0, 1)
    assert np.allclose(xs[1], BOWL.center)


def test_sgd_constant_step_hovers_decreasing_step_settles():
    """Constant step: noise floor. Robbins-Monro schedule: much closer."""
    q = Quadratic([[1.0, 0.0], [0.0, 1.0]])
    noisy = lambda x, rng: q.grad(x) + rng.normal(scale=1.0, size=2)  # noqa: E731
    const = sgd(noisy, X0, 0.2, 4000, seed=1)
    decay = sgd(noisy, X0, lambda k: 1.0 / (k + 5), 4000, seed=1)
    err_const = np.mean(np.linalg.norm(const[-500:], axis=1))
    err_decay = np.mean(np.linalg.norm(decay[-500:], axis=1))
    assert err_decay < 0.5 * err_const


def test_gauss_newton_and_lm_fit_an_exponential():
    t = np.linspace(0, 2, 30)
    true = np.array([2.0, -1.3])
    y = true[0] * np.exp(true[1] * t)
    r = lambda th: th[0] * np.exp(th[1] * t) - y  # noqa: E731
    J = lambda th: np.stack([np.exp(th[1] * t), th[0] * t * np.exp(th[1] * t)], axis=1)  # noqa: E731
    assert np.allclose(gauss_newton(r, J, [1.5, -1.0], 20)[-1], true, atol=1e-8)
    thetas, rhos = levenberg_marquardt(r, J, [0.5, 0.5], 100)
    assert np.allclose(thetas[-1], true, atol=1e-6)
    assert len(rhos) == len(thetas)


# --- Episode 6 ---------------------------------------------------------------

def test_adam_reaches_the_minimum_neighbourhood():
    xs = adam(BOWL.grad, X0, 0.05, 3000)
    assert np.linalg.norm(xs[-1] - BOWL.center) < 1e-2


# --- Episode 2 ---------------------------------------------------------------

FACTORY_C = [3.0, 5.0]
FACTORY_A = [[1.0, 0.0], [0.0, 2.0], [3.0, 2.0]]
FACTORY_B = [4.0, 12.0, 18.0]


def test_factory_lp_strong_duality_and_complementary_slackness():
    sol = solve_lp_max(FACTORY_C, FACTORY_A, FACTORY_B)
    assert np.allclose(sol.x, [2.0, 6.0])
    assert np.isclose(sol.value, 36.0)
    y = sol.shadow_prices
    assert np.all(y >= -1e-12)
    assert np.isclose(np.dot(FACTORY_B, y), sol.value)                       # strong duality
    slack = np.asarray(FACTORY_B) - np.asarray(FACTORY_A) @ sol.x
    assert np.allclose(y * slack, 0.0)                                        # complementary slackness
    assert np.isclose(y[0], 0.0)                                              # slack resource is free


def test_shadow_price_is_derivative_of_optimal_value():
    """Episode 4: y_i = d value / d b_i while the binding set is unchanged."""
    base = solve_lp_max(FACTORY_C, FACTORY_A, FACTORY_B)
    h = 1e-4
    for i in range(3):
        b = np.array(FACTORY_B)
        b[i] += h
        fd = (solve_lp_max(FACTORY_C, FACTORY_A, b).value - base.value) / h
        assert np.isclose(fd, base.shadow_prices[i], atol=1e-6)


def test_optimum_is_a_vertex_of_the_polygon():
    A = np.vstack([FACTORY_A, -np.eye(2)])
    b = np.concatenate([FACTORY_B, [0.0, 0.0]])
    V = vertices_2d(A, b)
    assert len(V) == 5
    sol = solve_lp_max(FACTORY_C, FACTORY_A, FACTORY_B)
    assert any(np.allclose(v, sol.x) for v in V)


# --- Episode 7 ---------------------------------------------------------------

def path_graph(n):
    A = np.zeros((n, n))
    for i in range(n - 1):
        A[i, i + 1] = A[i + 1, i] = 1.0
    return A


def test_laplacian_properties_and_connectivity():
    L = cons.laplacian(path_graph(6))
    assert np.allclose(L @ np.ones(6), 0.0)
    assert cons.algebraic_connectivity(L) > 0
    disconnected = cons.laplacian(np.kron(np.eye(2), path_graph(3)))
    assert np.isclose(cons.algebraic_connectivity(disconnected), 0.0)


def test_consensus_reaches_the_average_iff_below_threshold():
    L = cons.laplacian(path_graph(6))
    x0 = np.arange(6.0)
    t = cons.consensus_threshold(L)
    below = cons.consensus(L, x0, 0.95 * t, 3000)
    above = cons.consensus(L, x0, 1.05 * t, 3000)
    assert np.allclose(below[-1], x0.mean(), atol=1e-6)
    assert np.allclose(below.sum(axis=1), x0.sum())          # the average is invariant
    assert np.max(np.abs(above[-1] - x0.mean())) > 1e3


def test_better_connected_graphs_agree_faster():
    path = cons.laplacian(path_graph(8))
    complete = cons.laplacian(np.ones((8, 8)) - np.eye(8))
    assert cons.algebraic_connectivity(complete) > 10 * cons.algebraic_connectivity(path)


def test_containment_rows_are_convex_weights():
    # leaders 0 and 4 at the ends of a path; followers in between
    L = cons.laplacian(path_graph(5))
    H = cons.containment_matrix(L, followers=[1, 2, 3], leaders=[0, 4])
    assert np.all(H >= -1e-12)
    assert np.allclose(H.sum(axis=1), 1.0)
    assert np.allclose(H @ [0.0, 4.0], [1.0, 2.0, 3.0])


# --- Episode 8 ---------------------------------------------------------------

def test_dgd_stalls_gradient_tracking_is_exact():
    """f_i(x) = 1/2 (x - a_i)^2: optimum is mean(a); DGD is biased, GT is exact."""
    a = np.array([[-3.0], [0.0], [1.0], [6.0]])
    grads = [lambda x, ai=ai: x - ai for ai in a]
    L = cons.laplacian(path_graph(4))
    W = np.eye(4) - 0.3 * L
    x0 = np.zeros((4, 1))
    dg = cons.dgd(W, grads, x0, 0.1, 3000)[-1]
    gt = cons.gradient_tracking(W, grads, x0, 0.1, 3000)[-1]
    assert np.allclose(gt, a.mean(), atol=1e-8)
    assert np.max(np.abs(dg - a.mean())) > 1e-2


# --- Episode 9 ---------------------------------------------------------------

def test_lqr_stabilizes_a_double_integrator():
    dt = 0.1
    A_d = [[1.0, dt], [0.0, 1.0]]
    B_d = [[0.5 * dt ** 2], [dt]]
    K, P = dlqr(A_d, B_d, np.eye(2), [[1.0]])
    closed = np.asarray(A_d) - np.asarray(B_d) @ K
    assert np.max(np.abs(np.linalg.eigvals(closed))) < 1.0
    xs, _ = simulate_linear(A_d, B_d, K, [1.0, 0.0], 300)
    assert np.linalg.norm(xs[-1]) < 1e-6


# --- Episode 4 ---------------------------------------------------------------

def test_trajectory_sensitivity_matches_the_exact_solution():
    """x' = -p x: x = x0 e^{-pt}, dx/dp = -t x0 e^{-pt}."""
    p, x0 = 0.7, 2.0
    t, X, S = trajectory_sensitivity(lambda x: -p * x, lambda x: np.array([[-p]]),
                                     lambda x: -x, [x0], [[0.0]], 3.0, 0.01)
    assert np.allclose(X[:, 0], x0 * np.exp(-p * t), atol=1e-8)
    assert np.allclose(S[:, 0, 0], -t * x0 * np.exp(-p * t), atol=1e-8)
