# Stubs for scipy.sparse.linalg._expm_multiply (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def expm_multiply(A: Any, B: Any, start: Optional[Any] = ..., stop: Optional[Any] = ..., num: Optional[Any] = ..., endpoint: Optional[Any] = ...): ...

class LazyOperatorNormInfo:
    _A: Any = ...
    _A_1_norm: Any = ...
    _ell: Any = ...
    _d: Any = ...
    _scale: Any = ...
    def __init__(self, A: Any, A_1_norm: Optional[Any] = ..., ell: int = ..., scale: int = ...) -> None: ...
    def set_scale(self, scale: Any) -> None: ...
    def onenorm(self): ...
    def d(self, p: Any): ...
    def alpha(self, p: Any): ...