"""Keep the Gradient - Shared Scene Library

Everything that more than one episode uses lives here, so no scene file ever
carries a private copy of a helper:

- ``gradkit.style``       colours by role, sizes, timing (the visual language)
- ``gradkit.tex``         the LaTeX template with the series' math macros
- ``gradkit.scenes``      base scenes, the title card and the placeholder card
- ``gradkit.mobjects``    the recurring objects: ball, paths, walls, forces, price tags
- ``gradkit.algorithms``  the numerics every animation is computed from

Importing ``gradkit.scenes`` applies the style globally, so a scene file only
needs ``from gradkit.scenes import SeriesScene``.
"""
