# Stubs for scipy.interpolate.polyint (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class _Interpolator1D:
    __slots__: Any = ...
    _y_axis: Any = ...
    _y_extra_shape: Any = ...
    dtype: Any = ...
    def __init__(self, xi: Optional[Any] = ..., yi: Optional[Any] = ..., axis: Optional[Any] = ...) -> None: ...
    def __call__(self, x: Any): ...
    def _evaluate(self, x: Any) -> None: ...
    def _prepare_x(self, x: Any): ...
    def _finish_y(self, y: Any, x_shape: Any): ...
    def _reshape_yi(self, yi: Any, check: bool = ...): ...
    def _set_yi(self, yi: Any, xi: Optional[Any] = ..., axis: Optional[Any] = ...) -> None: ...
    def _set_dtype(self, dtype: Any, union: bool = ...) -> None: ...

class _Interpolator1DWithDerivatives(_Interpolator1D):
    def derivatives(self, x: Any, der: Optional[Any] = ...): ...
    def derivative(self, x: Any, der: int = ...): ...

class KroghInterpolator(_Interpolator1DWithDerivatives):
    xi: Any = ...
    yi: Any = ...
    c: Any = ...
    def __init__(self, xi: Any, yi: Any, axis: int = ...) -> None: ...
    def _evaluate(self, x: Any): ...
    def _evaluate_derivatives(self, x: Any, der: Optional[Any] = ...): ...

def krogh_interpolate(xi: Any, yi: Any, x: Any, der: int = ..., axis: int = ...): ...
def approximate_taylor_polynomial(f: Any, x: Any, degree: Any, scale: Any, order: Optional[Any] = ...): ...

class BarycentricInterpolator(_Interpolator1D):
    xi: Any = ...
    n: Any = ...
    wi: Any = ...
    def __init__(self, xi: Any, yi: Optional[Any] = ..., axis: int = ...) -> None: ...
    yi: Any = ...
    def set_yi(self, yi: Any, axis: Optional[Any] = ...): ...
    def add_xi(self, xi: Any, yi: Optional[Any] = ...) -> None: ...
    def __call__(self, x: Any): ...
    def _evaluate(self, x: Any): ...

def barycentric_interpolate(xi: Any, yi: Any, x: Any, axis: int = ...): ...
