"""Keep the Gradient - Ant Colony Optimization (Episode 12) (specified, not yet implemented)

Ant system on a small graph: an ant picks edge (i, j) with probability proportional to tau_ij^a eta_ij^b; after each round tau <- (1 - rho) tau + delta_tau. Include the double-bridge set-up and a moving food source for the evaporation scene.
"""
from __future__ import annotations


def ant_system(graph, a, b, rho, ants, rounds, seed, *args, **kwargs):
    """See the module docstring for the specification."""
    raise NotImplementedError("ant_system: see gradkit/algorithms/aco.py for the specification")
