"""Keep the Gradient - Tabular Reinforcement Learning (Episode 10) (specified, not yet implemented)

Grid-world Q-learning: Q(s,a) <- Q(s,a) + alpha [r + gamma max_a' Q(s',a') - Q(s,a)] with epsilon-greedy exploration and a fixed seed. Return the Q-table after every episode so the scenes can show values spreading back from the goal.
"""
from __future__ import annotations


def q_learning(grid, alpha, gamma, epsilon, episodes, seed, *args, **kwargs):
    """See the module docstring for the specification."""
    raise NotImplementedError("q_learning: see gradkit/algorithms/rl.py for the specification")
