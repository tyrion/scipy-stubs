# Stubs for scipy.interpolate.ndgriddata (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .interpnd import CloughTocher2DInterpolator as CloughTocher2DInterpolator, LinearNDInterpolator as LinearNDInterpolator, NDInterpolatorBase
from typing import Any, Optional

class NearestNDInterpolator(NDInterpolatorBase):
    tree: Any = ...
    values: Any = ...
    def __init__(self, x: Any, y: Any, rescale: bool = ..., tree_options: Optional[Any] = ...) -> None: ...
    def __call__(self, *args: Any): ...

def griddata(points: Any, values: Any, xi: Any, method: str = ..., fill_value: Any = ..., rescale: bool = ...): ...
