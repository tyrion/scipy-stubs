# Stubs for scipy.sparse.linalg.interface (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class LinearOperator:
    def __new__(cls, *args: Any, **kwargs: Any): ...
    dtype: Any = ...
    shape: Any = ...
    def __init__(self, dtype: Any, shape: Any) -> None: ...
    def _init_dtype(self) -> None: ...
    def _matmat(self, X: Any): ...
    def _matvec(self, x: Any): ...
    def matvec(self, x: Any): ...
    def rmatvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def matmat(self, X: Any): ...
    def __call__(self, x: Any): ...
    def __mul__(self, x: Any): ...
    def dot(self, x: Any): ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    def __rmul__(self, x: Any): ...
    def __pow__(self, p: Any): ...
    def __add__(self, x: Any): ...
    def __neg__(self): ...
    def __sub__(self, x: Any): ...
    def __repr__(self): ...
    def adjoint(self): ...
    H: Any = ...
    def transpose(self): ...
    T: Any = ...
    def _adjoint(self): ...

class _CustomLinearOperator(LinearOperator):
    args: Any = ...
    __matvec_impl: Any = ...
    __rmatvec_impl: Any = ...
    __matmat_impl: Any = ...
    def __init__(self, shape: Any, matvec: Any, rmatvec: Optional[Any] = ..., matmat: Optional[Any] = ..., dtype: Optional[Any] = ...) -> None: ...
    def _matmat(self, X: Any): ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _adjoint(self): ...

class _SumLinearOperator(LinearOperator):
    args: Any = ...
    def __init__(self, A: Any, B: Any) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, x: Any): ...
    def _adjoint(self): ...

class _ProductLinearOperator(LinearOperator):
    args: Any = ...
    def __init__(self, A: Any, B: Any) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, x: Any): ...
    def _adjoint(self): ...

class _ScaledLinearOperator(LinearOperator):
    args: Any = ...
    def __init__(self, A: Any, alpha: Any) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, x: Any): ...
    def _adjoint(self): ...

class _PowerLinearOperator(LinearOperator):
    args: Any = ...
    def __init__(self, A: Any, p: Any) -> None: ...
    def _power(self, fun: Any, x: Any): ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, x: Any): ...
    def _adjoint(self): ...

class MatrixLinearOperator(LinearOperator):
    A: Any = ...
    __adj: Any = ...
    args: Any = ...
    def __init__(self, A: Any) -> None: ...
    def _matmat(self, X: Any): ...
    def _adjoint(self): ...

class _AdjointMatrixOperator(MatrixLinearOperator):
    A: Any = ...
    __adjoint: Any = ...
    args: Any = ...
    shape: Any = ...
    def __init__(self, adjoint: Any) -> None: ...
    @property
    def dtype(self): ...
    def _adjoint(self): ...

class IdentityOperator(LinearOperator):
    def __init__(self, shape: Any, dtype: Optional[Any] = ...) -> None: ...
    def _matvec(self, x: Any): ...
    def _rmatvec(self, x: Any): ...
    def _matmat(self, x: Any): ...
    def _adjoint(self): ...

def aslinearoperator(A: Any): ...
