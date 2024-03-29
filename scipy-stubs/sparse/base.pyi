# Stubs for scipy.sparse.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .csr import csr_matrix
from .csc import csc_matrix
from .coo import coo_matrix
from .dok import dok_matrix
from .dia import dia_matrix
from .lil import lil_matrix

class SparseWarning(Warning): ...
class SparseFormatWarning(SparseWarning): ...
class SparseEfficiencyWarning(SparseWarning): ...

class spmatrix:
    __array_priority__: float = ...
    ndim: int = ...
    _shape: Any = ...
    maxprint: Any = ...
    def __init__(self, maxprint: Any = ...) -> None: ...
    __dict__: Any = ...
    def set_shape(self, shape: Any) -> None: ...
    def get_shape(self): ...
    shape: Any = ...
    def reshape(self, *args: Any, **kwargs: Any): ...
    def resize(self, shape: Any) -> None: ...
    def astype(self, dtype: Any, casting: str = ..., copy: bool = ...): ...
    def asfptype(self): ...
    #def __iter__(self) -> None: ...
    def getmaxprint(self): ...
    def count_nonzero(self) -> None: ...
    def getnnz(self, axis: Optional[Any] = ...) -> None: ...
    @property
    def nnz(self): ...
    def getformat(self): ...
    def __repr__(self): ...
    def __str__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __len__(self) -> int: ...
    def asformat(self, format: Any, copy: bool = ...): ...
    def multiply(self, other: Any): ...
    def maximum(self, other: Any): ...
    def minimum(self, other: Any): ...
    def dot(self, other: Any): ...
    def power(self, n: Any, dtype: Optional[Any] = ...): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __abs__(self): ...
    def _add_sparse(self, other: Any): ...
    def _add_dense(self, other: Any): ...
    def _sub_sparse(self, other: Any): ...
    def _sub_dense(self, other: Any): ...
    def _rsub_dense(self, other: Any): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def _mul_scalar(self, other: Any): ...
    def _mul_vector(self, other: Any): ...
    def _mul_multivector(self, other: Any): ...
    def _mul_sparse_matrix(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    def _divide(self, other: Any, true_divide: bool = ..., rdivide: bool = ...): ...
    def __truediv__(self, other: Any): ...
    def __div__(self, other: Any): ...
    def __rtruediv__(self, other: Any): ...
    def __rdiv__(self, other: Any): ...
    def __neg__(self): ...
    def __iadd__(self, other: Any): ...
    def __isub__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def __idiv__(self, other: Any): ...
    def __itruediv__(self, other: Any): ...
    def __pow__(self, other: Any): ...
    def __getattr__(self, attr: Any): ...
    def transpose(self, axes: Optional[Any] = ..., copy: bool = ...): ...
    def conj(self, copy: bool = ...): ...
    def conjugate(self, copy: bool = ...): ...
    def getH(self): ...
    def _real(self): ...
    def _imag(self): ...
    def nonzero(self): ...
    def getcol(self, j: Any): ...
    def getrow(self, i: Any): ...
    def todense(self, order: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def toarray(self, order: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def tocsr(self, copy: bool = ...) -> csr_matrix: ...
    def todok(self, copy: bool = ...) -> dok_matrix: ...
    def tocoo(self, copy: bool = ...) -> coo_matrix: ...
    def tolil(self, copy: bool = ...) -> lil_matrix: ...
    def todia(self, copy: bool = ...) -> dia_matrix: ...
    def tobsr(self, blocksize: Optional[Any] = ..., copy: bool = ...): ...
    def tocsc(self, copy: bool = ...) -> csc_matrix: ...
    def copy(self): ...
    def sum(self, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def mean(self, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def diagonal(self, k: int = ...): ...
    def setdiag(self, values: Any, k: int = ...) -> None: ...
    def _setdiag(self, values: Any, k: Any): ...
    def _process_toarray_args(self, order: Any, out: Any): ...

def isspmatrix(x: Any): ...
issparse = isspmatrix
