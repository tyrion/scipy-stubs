# Stubs for scipy.optimize._linprog (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def linprog_verbose_callback(xk: Any, **kwargs: Any): ...
def linprog_terse_callback(xk: Any, **kwargs: Any) -> None: ...
def linprog(c: Any, A_ub: Optional[Any] = ..., b_ub: Optional[Any] = ..., A_eq: Optional[Any] = ..., b_eq: Optional[Any] = ..., bounds: Optional[Any] = ..., method: str = ..., callback: Optional[Any] = ..., options: Optional[Any] = ...): ...
