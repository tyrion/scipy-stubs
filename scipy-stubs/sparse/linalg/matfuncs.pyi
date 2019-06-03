# Stubs for scipy.sparse.linalg.matfuncs (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from scipy.sparse.linalg.interface import LinearOperator
from typing import Any, Optional

def inv(A: Any): ...

class MatrixPowerOperator(LinearOperator):
    _A: Any = ...
    _p: Any = ...
    _structure: Any = ...
    dtype: Any = ...
    ndim: Any = ...
    shape: Any = ...
    def __init__(self, A: Any, p: Any, structure: Optional[Any] = ...) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, X: Any): ...
    @property
    def T(self): ...

class ProductOperator(LinearOperator):
    _structure: Any = ...
    shape: Any = ...
    ndim: Any = ...
    dtype: Any = ...
    _operator_sequence: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, X: Any): ...
    @property
    def T(self): ...

class _ExpmPadeHelper:
    A: Any = ...
    _A2: Any = ...
    _A4: Any = ...
    _A6: Any = ...
    _A8: Any = ...
    _A10: Any = ...
    _d4_exact: Any = ...
    _d6_exact: Any = ...
    _d8_exact: Any = ...
    _d10_exact: Any = ...
    _d4_approx: Any = ...
    _d6_approx: Any = ...
    _d8_approx: Any = ...
    _d10_approx: Any = ...
    ident: Any = ...
    structure: Any = ...
    use_exact_onenorm: Any = ...
    def __init__(self, A: Any, structure: Optional[Any] = ..., use_exact_onenorm: bool = ...) -> None: ...
    @property
    def A2(self): ...
    @property
    def A4(self): ...
    @property
    def A6(self): ...
    @property
    def A8(self): ...
    @property
    def A10(self): ...
    @property
    def d4_tight(self): ...
    @property
    def d6_tight(self): ...
    @property
    def d8_tight(self): ...
    @property
    def d10_tight(self): ...
    @property
    def d4_loose(self): ...
    @property
    def d6_loose(self): ...
    @property
    def d8_loose(self): ...
    @property
    def d10_loose(self): ...
    def pade3(self): ...
    def pade5(self): ...
    def pade7(self): ...
    def pade9(self): ...
    def pade13_scaled(self, s: Any): ...

def expm(A: Any): ...