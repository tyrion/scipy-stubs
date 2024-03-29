# Stubs for scipy.optimize._lsq.least_squares (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .common import EPS, in_bounds, make_strictly_feasible
from .dogbox import dogbox
from .trf import trf
from typing import Any, Optional

TERMINATION_MESSAGES: Any
FROM_MINPACK_TO_COMMON: Any

def call_minpack(fun: Any, x0: Any, jac: Any, ftol: Any, xtol: Any, gtol: Any, max_nfev: Any, x_scale: Any, diff_step: Any): ...
def prepare_bounds(bounds: Any, n: Any): ...
def check_tolerance(ftol: Any, xtol: Any, gtol: Any): ...
def check_x_scale(x_scale: Any, x0: Any): ...
def check_jac_sparsity(jac_sparsity: Any, m: Any, n: Any): ...
def huber(z: Any, rho: Any, cost_only: Any): ...
def soft_l1(z: Any, rho: Any, cost_only: Any): ...
def cauchy(z: Any, rho: Any, cost_only: Any): ...
def arctan(z: Any, rho: Any, cost_only: Any): ...

IMPLEMENTED_LOSSES: Any

def construct_loss_function(m: Any, loss: Any, f_scale: Any): ...
def least_squares(fun: Any, x0: Any, jac: str = ..., bounds: Any = ..., method: str = ..., ftol: float = ..., xtol: float = ..., gtol: float = ..., x_scale: float = ..., loss: str = ..., f_scale: float = ..., diff_step: Optional[Any] = ..., tr_solver: Optional[Any] = ..., tr_options: Any = ..., jac_sparsity: Optional[Any] = ..., max_nfev: Optional[Any] = ..., verbose: int = ..., args: Any = ..., kwargs: Any = ...): ...
