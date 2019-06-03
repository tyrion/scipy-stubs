# Stubs for scipy.spatial._spherical_voronoi (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class SphericalVoronoi:
    points: Any = ...
    center: Any = ...
    radius: Any = ...
    vertices: Any = ...
    regions: Any = ...
    _tri: Any = ...
    def __init__(self, points: Any, radius: Optional[Any] = ..., center: Optional[Any] = ..., threshold: float = ...) -> None: ...
    def _calc_vertices_regions(self): ...
    def sort_vertices_of_regions(self) -> None: ...
