"""Keep the Gradient - Agent Graphs (specified, not yet implemented)

Agents are dots joined by communication edges. Needed from Episode 7 on.
"""
from __future__ import annotations

from manim import VGroup


class AgentGraph(VGroup):
    """A communication graph whose node colours show the agents' values.

    Specification
    -------------
    - inputs: adjacency matrix (the same one passed to
      ``gradkit.algorithms.consensus.laplacian``), node positions, optional
      set of leader indices;
    - nodes in ``style.AGENT`` (leaders in ``style.LEADER``), edges in ``style.EDGE``;
    - ``set_values(x)`` recolours or labels the nodes from a value vector, so a
      consensus run from ``algorithms.consensus.consensus`` can be animated
      frame by frame with an updater;
    - optional numeric labels on the nodes.
    """

    def __init__(self, adjacency, positions, leaders=()) -> None:
        raise NotImplementedError("AgentGraph: implement before Episode 7 (see class docstring)")
