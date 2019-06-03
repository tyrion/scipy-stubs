# Stubs for scipy.interpolate.fitpack2 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class UnivariateSpline:
    ext: Any = ...
    _data: Any = ...
    def __init__(self, x: Any, y: Any, w: Optional[Any] = ..., bbox: Any = ..., k: int = ..., s: Optional[Any] = ..., ext: int = ..., check_finite: bool = ...) -> None: ...
    @classmethod
    _eval_args: Any = ...
    def _from_tck(cls, tck: Any, ext: int = ...): ...
    def _reset_class(self) -> None: ...
    _spline_class: Any = ...
    __class__: Any = ...
    def _set_class(self, cls: Any) -> None: ...
    def _reset_nest(self, data: Any, nest: Optional[Any] = ...): ...
    def set_smoothing_factor(self, s: Any): ...
    def __call__(self, x: Any, nu: int = ..., ext: Optional[Any] = ...): ...
    def get_knots(self): ...
    def get_coeffs(self): ...
    def get_residual(self): ...
    def integral(self, a: Any, b: Any): ...
    def derivatives(self, x: Any): ...
    def roots(self): ...
    def derivative(self, n: int = ...): ...
    def antiderivative(self, n: int = ...): ...

class InterpolatedUnivariateSpline(UnivariateSpline):
    _data: Any = ...
    ext: Any = ...
    def __init__(self, x: Any, y: Any, w: Optional[Any] = ..., bbox: Any = ..., k: int = ..., ext: int = ..., check_finite: bool = ...) -> None: ...

class LSQUnivariateSpline(UnivariateSpline):
    _data: Any = ...
    ext: Any = ...
    def __init__(self, x: Any, y: Any, t: Any, w: Optional[Any] = ..., bbox: Any = ..., k: int = ..., ext: int = ..., check_finite: bool = ...) -> None: ...

class _BivariateSplineBase:
    def get_residual(self): ...
    def get_knots(self): ...
    def get_coeffs(self): ...
    def __call__(self, x: Any, y: Any, dx: int = ..., dy: int = ..., grid: bool = ...): ...

class BivariateSpline(_BivariateSplineBase):
    @classmethod
    tck: Any = ...
    degrees: Any = ...
    def _from_tck(cls, tck: Any): ...
    def ev(self, xi: Any, yi: Any, dx: int = ..., dy: int = ...): ...
    def integral(self, xa: Any, xb: Any, ya: Any, yb: Any): ...

class SmoothBivariateSpline(BivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, x: Any, y: Any, z: Any, w: Optional[Any] = ..., bbox: Any = ..., kx: int = ..., ky: int = ..., s: Optional[Any] = ..., eps: Optional[Any] = ...) -> None: ...

class LSQBivariateSpline(BivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, x: Any, y: Any, z: Any, tx: Any, ty: Any, w: Optional[Any] = ..., bbox: Any = ..., kx: int = ..., ky: int = ..., eps: Optional[Any] = ...) -> None: ...

class RectBivariateSpline(BivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, x: Any, y: Any, z: Any, bbox: Any = ..., kx: int = ..., ky: int = ..., s: int = ...) -> None: ...

class SphereBivariateSpline(_BivariateSplineBase):
    def __call__(self, theta: Any, phi: Any, dtheta: int = ..., dphi: int = ..., grid: bool = ...): ...
    def ev(self, theta: Any, phi: Any, dtheta: int = ..., dphi: int = ...): ...

class SmoothSphereBivariateSpline(SphereBivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, theta: Any, phi: Any, r: Any, w: Optional[Any] = ..., s: float = ..., eps: float = ...) -> None: ...

class LSQSphereBivariateSpline(SphereBivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, theta: Any, phi: Any, r: Any, tt: Any, tp: Any, w: Optional[Any] = ..., eps: float = ...) -> None: ...

class RectSphereBivariateSpline(SphereBivariateSpline):
    fp: Any = ...
    tck: Any = ...
    degrees: Any = ...
    def __init__(self, u: Any, v: Any, r: Any, s: float = ..., pole_continuity: bool = ..., pole_values: Optional[Any] = ..., pole_exact: bool = ..., pole_flat: bool = ...) -> None: ...
