"""Keep the Gradient - Recurring Objects

The objects of the visual language in SERIES.md. Each one has a fixed meaning
and colour across the series; build new pictures from these rather than from
raw manim shapes, so a viewer recognises an idea from one episode to the next.

Implemented: Ball, IteratePath, GhostPath, FeasibleRegion, Wall, ForceArrow,
PriceTag. Specified but not yet implemented (they raise NotImplementedError
with their specification): ContourMap, Landscape3D, AgentGraph.
"""
from gradkit.mobjects.constraints import FeasibleRegion, ForceArrow, Wall
from gradkit.mobjects.graphs import AgentGraph
from gradkit.mobjects.iterates import Ball, GhostPath, IteratePath
from gradkit.mobjects.labels import PriceTag
from gradkit.mobjects.landscape import ContourMap, Landscape3D

__all__ = ["AgentGraph", "Ball", "ContourMap", "FeasibleRegion", "ForceArrow",
           "GhostPath", "IteratePath", "Landscape3D", "PriceTag", "Wall"]
