# Stubs for scipy.sparse.csgraph._laplacian (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def laplacian(csgraph: Any, normed: bool = ..., return_diag: bool = ..., use_out_degree: bool = ...): ...
def _setdiag_dense(A: Any, d: Any) -> None: ...
def _laplacian_sparse(graph: Any, normed: bool = ..., axis: int = ...): ...
def _laplacian_dense(graph: Any, normed: bool = ..., axis: int = ...): ...
