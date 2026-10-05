"""Keep the Gradient - Numerics Behind the Animations

Every iterate, trajectory and value shown on screen is computed here, never
placed by hand, so the picture is correct by construction. Each function cites
the episode whose "Precise statements" it implements, and tests/ checks the
statements themselves (thresholds, convergence, duality) against this code.

Implemented: quadratic, descent, least_squares, lp, consensus, control,
sensitivity. Specified stubs (raise NotImplementedError): svm, coverage, rl,
pareto, aco.

Conventions: iterates are returned as arrays of shape (steps + 1, n) with the
starting point first; a step size may be a float or a callable k -> alpha_k.
"""
