# Stubs for scipy.sparse.csc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .compressed import _cs_matrix
from .sputils import IndexMixin
from typing import Any, Optional

class csc_matrix(_cs_matrix, IndexMixin):
    format: str = ...
    def transpose(self, axes: Optional[Any] = ..., copy: bool = ...): ...
    def __iter__(self) -> None: ...
    def tocsc(self, copy: bool = ...): ...
    def tocsr(self, copy: bool = ...): ...
    def __getitem__(self, key: Any): ...
    def nonzero(self): ...
    def getrow(self, i: Any): ...
    def getcol(self, i: Any): ...
    def _swap(self, x: Any): ...

def isspmatrix_csc(x: Any): ...
