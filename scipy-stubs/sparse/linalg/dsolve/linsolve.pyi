# Stubs for scipy.sparse.linalg.dsolve.linsolve (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class MatrixRankWarning(UserWarning): ...

def use_solver(**kwargs: Any) -> None: ...
def spsolve(A: Any, b: Any, permc_spec: Optional[Any] = ..., use_umfpack: bool = ...): ...
def splu(A: Any, permc_spec: Optional[Any] = ..., diag_pivot_thresh: Optional[Any] = ..., relax: Optional[Any] = ..., panel_size: Optional[Any] = ..., options: Any = ...): ...
def spilu(A: Any, drop_tol: Optional[Any] = ..., fill_factor: Optional[Any] = ..., drop_rule: Optional[Any] = ..., permc_spec: Optional[Any] = ..., diag_pivot_thresh: Optional[Any] = ..., relax: Optional[Any] = ..., panel_size: Optional[Any] = ..., options: Optional[Any] = ...): ...
def factorized(A: Any): ...
def spsolve_triangular(A: Any, b: Any, lower: bool = ..., overwrite_A: bool = ..., overwrite_b: bool = ...): ...
