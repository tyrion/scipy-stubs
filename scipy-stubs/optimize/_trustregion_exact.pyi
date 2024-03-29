# Stubs for scipy.optimize._trustregion_exact (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._trustregion import BaseQuadraticSubproblem
from typing import Any, Optional

def _minimize_trustregion_exact(fun: Any, x0: Any, args: Any = ..., jac: Optional[Any] = ..., hess: Optional[Any] = ..., **trust_region_options: Any): ...
def estimate_smallest_singular_value(U: Any): ...
def singular_leading_submatrix(A: Any, U: Any, k: Any): ...

class IterativeSubproblem(BaseQuadraticSubproblem):
    UPDATE_COEFF: float = ...
    EPS: Any = ...
    previous_tr_radius: int = ...
    lambda_lb: Any = ...
    niter: int = ...
    k_easy: Any = ...
    k_hard: Any = ...
    dimension: Any = ...
    hess_inf: Any = ...
    hess_fro: Any = ...
    CLOSE_TO_ZERO: Any = ...
    def __init__(self, x: Any, fun: Any, jac: Any, hess: Any, hessp: Optional[Any] = ..., k_easy: float = ..., k_hard: float = ...) -> None: ...
    def _initial_values(self, tr_radius: Any): ...
    lambda_current: Any = ...
    def solve(self, tr_radius: Any): ...
