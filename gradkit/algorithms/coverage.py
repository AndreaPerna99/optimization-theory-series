"""Keep the Gradient - Voronoi Coverage (Episode 8) (specified, not yet implemented)

Lloyd's algorithm for min integral of min_i ||q - p_i||^2 phi(q) dq on a grid: each step moves every robot to the centroid of its Voronoi cell weighted by the survivor density phi. Return the robot positions per step and the cell assignment. Use only if it matches the SAR project [CONFIRM].
"""
from __future__ import annotations


def lloyd_coverage(positions, density, grid, steps, *args, **kwargs):
    """See the module docstring for the specification."""
    raise NotImplementedError("lloyd_coverage: see gradkit/algorithms/coverage.py for the specification")
