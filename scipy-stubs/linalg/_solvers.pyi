# Stubs for scipy.linalg._solvers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def solve_sylvester(a: Any, b: Any, q: Any): ...
def solve_continuous_lyapunov(a: Any, q: Any): ...
solve_lyapunov = solve_continuous_lyapunov

def solve_discrete_lyapunov(a: Any, q: Any, method: Optional[Any] = ...): ...
def solve_continuous_are(a: Any, b: Any, q: Any, r: Any, e: Optional[Any] = ..., s: Optional[Any] = ..., balanced: bool = ...): ...
def solve_discrete_are(a: Any, b: Any, q: Any, r: Any, e: Optional[Any] = ..., s: Optional[Any] = ..., balanced: bool = ...): ...