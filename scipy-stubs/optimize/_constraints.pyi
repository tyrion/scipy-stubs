# Stubs for scipy.optimize._constraints (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._differentiable_functions import IdentityVectorFunction, LinearVectorFunction, VectorFunction
from ._hessian_update_strategy import BFGS
from typing import Any, Optional

class NonlinearConstraint:
    fun: Any = ...
    lb: Any = ...
    ub: Any = ...
    finite_diff_rel_step: Any = ...
    finite_diff_jac_sparsity: Any = ...
    jac: Any = ...
    hess: Any = ...
    keep_feasible: Any = ...
    def __init__(self, fun: Any, lb: Any, ub: Any, jac: str = ..., hess: Any = ..., keep_feasible: bool = ..., finite_diff_rel_step: Optional[Any] = ..., finite_diff_jac_sparsity: Optional[Any] = ...) -> None: ...

class LinearConstraint:
    A: Any = ...
    lb: Any = ...
    ub: Any = ...
    keep_feasible: Any = ...
    def __init__(self, A: Any, lb: Any, ub: Any, keep_feasible: bool = ...) -> None: ...

class Bounds:
    lb: Any = ...
    ub: Any = ...
    keep_feasible: Any = ...
    def __init__(self, lb: Any, ub: Any, keep_feasible: bool = ...) -> None: ...

class PreparedConstraint:
    fun: Any = ...
    bounds: Any = ...
    keep_feasible: Any = ...
    def __init__(self, constraint: Any, x0: Any, sparse_jacobian: Optional[Any] = ..., finite_diff_bounds: Any = ...) -> None: ...

def new_bounds_to_old(lb: Any, ub: Any, n: Any): ...
def old_bound_to_new(bounds: Any): ...
def strict_bounds(lb: Any, ub: Any, keep_feasible: Any, n_vars: Any): ...
