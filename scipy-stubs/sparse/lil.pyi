# Stubs for scipy.sparse.lil (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import spmatrix
from .sputils import IndexMixin
from typing import Any, Optional

class lil_matrix(spmatrix, IndexMixin):
    format: str = ...
    dtype: Any = ...
    _shape: Any = ...
    rows: Any = ...
    data: Any = ...
    def __init__(self, arg1: Any, shape: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> None: ...
    def __iadd__(self, other: Any): ...
    def __isub__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def __itruediv__(self, other: Any): ...
    def getnnz(self, axis: Optional[Any] = ...): ...
    def count_nonzero(self): ...
    def __str__(self): ...
    def getrowview(self, i: Any): ...
    def getrow(self, i: Any): ...
    def _check_row_bounds(self, i: Any): ...
    def _check_col_bounds(self, j: Any): ...
    def __getitem__(self, index: Any): ...
    def _get_row_ranges(self, rows: Any, col_slice: Any): ...
    def __setitem__(self, index: Any, x: Any): ...
    def _mul_scalar(self, other: Any): ...
    def __truediv__(self, other: Any): ...
    def copy(self): ...
    def reshape(self, *args: Any, **kwargs: Any): ...
    def resize(self, *shape: Any) -> None: ...
    def toarray(self, order: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def transpose(self, axes: Optional[Any] = ..., copy: bool = ...): ...
    def tolil(self, copy: bool = ...): ...
    def tocsr(self, copy: bool = ...): ...

def isspmatrix_lil(x: Any): ...
