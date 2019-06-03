# Stubs for scipy.optimize.linesearch (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class LineSearchWarning(RuntimeWarning): ...

def line_search_wolfe1(f: Any, fprime: Any, xk: Any, pk: Any, gfk: Optional[Any] = ..., old_fval: Optional[Any] = ..., old_old_fval: Optional[Any] = ..., args: Any = ..., c1: float = ..., c2: float = ..., amax: int = ..., amin: float = ..., xtol: float = ...): ...
def scalar_search_wolfe1(phi: Any, derphi: Any, phi0: Optional[Any] = ..., old_phi0: Optional[Any] = ..., derphi0: Optional[Any] = ..., c1: float = ..., c2: float = ..., amax: int = ..., amin: float = ..., xtol: float = ...): ...
line_search = line_search_wolfe1

def line_search_wolfe2(f: Any, myfprime: Any, xk: Any, pk: Any, gfk: Optional[Any] = ..., old_fval: Optional[Any] = ..., old_old_fval: Optional[Any] = ..., args: Any = ..., c1: float = ..., c2: float = ..., amax: Optional[Any] = ..., extra_condition: Optional[Any] = ..., maxiter: int = ...): ...
def scalar_search_wolfe2(phi: Any, derphi: Optional[Any] = ..., phi0: Optional[Any] = ..., old_phi0: Optional[Any] = ..., derphi0: Optional[Any] = ..., c1: float = ..., c2: float = ..., amax: Optional[Any] = ..., extra_condition: Optional[Any] = ..., maxiter: int = ...): ...
def line_search_armijo(f: Any, xk: Any, pk: Any, gfk: Any, old_fval: Any, args: Any = ..., c1: float = ..., alpha0: int = ...): ...
