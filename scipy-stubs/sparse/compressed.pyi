# Stubs for scipy.sparse.compressed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.
# NOTE: Manually edited

from .base import SparseEfficiencyWarning, isspmatrix, spmatrix
from .data import _data_matrix, _minmax_mixin
from .dia import dia_matrix
from .sputils import IndexMixin, get_sum_dtype, getdtype, isdense, isscalarlike, isshape, upcast
from typing import Any, Optional

class _cs_matrix(_data_matrix, _minmax_mixin, IndexMixin):
    data: Any = ...
    indices: Any = ...
    indptr: Any = ...
    def __init__(self, arg1: Any, shape: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ...) -> None: ...
    def getnnz(self, axis: Optional[Any] = ...): ...
    def check_format(self, full_check: bool = ...) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def multiply(self, other: Any): ...
    def diagonal(self, k: int = ...): ...
    def maximum(self, other: Any): ...
    def minimum(self, other: Any): ...
    def sum(self, axis: Optional[Any] = ..., dtype: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def __setitem__(self, index: Any, x: Any) -> None: ...
    def tocoo(self, copy: bool = ...): ...
    def toarray(self, order: Optional[Any] = ..., out: Optional[Any] = ...): ...
    def eliminate_zeros(self) -> None: ...
    has_canonical_format: Any = ...
    def sum_duplicates(self) -> None: ...
    has_sorted_indices: Any = ...
    def sorted_indices(self): ...
    def sort_indices(self) -> None: ...
    def prune(self) -> None: ...
    def resize(self, *shape: Any) -> None: ...
