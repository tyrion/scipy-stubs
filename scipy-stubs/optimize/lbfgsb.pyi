# Stubs for scipy.optimize.lbfgsb (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from scipy.sparse.linalg import LinearOperator
from typing import Any, Optional

def fmin_l_bfgs_b(func: Any, x0: Any, fprime: Optional[Any] = ..., args: Any = ..., approx_grad: int = ..., bounds: Optional[Any] = ..., m: int = ..., factr: float = ..., pgtol: float = ..., epsilon: float = ..., iprint: int = ..., maxfun: int = ..., maxiter: int = ..., disp: Optional[Any] = ..., callback: Optional[Any] = ..., maxls: int = ...): ...

class LbfgsInvHessProduct(LinearOperator):
    sk: Any = ...
    yk: Any = ...
    n_corrs: Any = ...
    rho: Any = ...
    def __init__(self, sk: Any, yk: Any) -> None: ...
    def _matvec(self, x: Any): ...
    def todense(self): ...