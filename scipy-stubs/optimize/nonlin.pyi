# Stubs for scipy.optimize.nonlin (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class NoConvergence(Exception): ...

class TerminationCondition:
    x_tol: Any = ...
    x_rtol: Any = ...
    f_tol: Any = ...
    f_rtol: Any = ...
    norm: Any = ...
    iter: Any = ...
    f0_norm: Any = ...
    iteration: int = ...
    def __init__(self, f_tol: Optional[Any] = ..., f_rtol: Optional[Any] = ..., x_tol: Optional[Any] = ..., x_rtol: Optional[Any] = ..., iter: Optional[Any] = ..., norm: Any = ...) -> None: ...
    def check(self, f: Any, x: Any, dx: Any): ...

class Jacobian:
    __array__: Any = ...
    def __init__(self, **kw: Any) -> None: ...
    def aspreconditioner(self): ...
    def solve(self, v: Any, tol: int = ...) -> None: ...
    def update(self, x: Any, F: Any) -> None: ...
    func: Any = ...
    shape: Any = ...
    dtype: Any = ...
    def setup(self, x: Any, F: Any, func: Any) -> None: ...

class InverseJacobian:
    jacobian: Any = ...
    matvec: Any = ...
    update: Any = ...
    setup: Any = ...
    rmatvec: Any = ...
    def __init__(self, jacobian: Any) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...

class GenericBroyden(Jacobian):
    last_f: Any = ...
    last_x: Any = ...
    alpha: Any = ...
    def setup(self, x0: Any, f0: Any, func: Any) -> None: ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...
    def update(self, x: Any, f: Any) -> None: ...

class LowRankMatrix:
    alpha: Any = ...
    cs: Any = ...
    ds: Any = ...
    n: Any = ...
    dtype: Any = ...
    collapsed: Any = ...
    def __init__(self, alpha: Any, n: Any, dtype: Any) -> None: ...
    @staticmethod
    def _matvec(v: Any, alpha: Any, cs: Any, ds: Any): ...
    @staticmethod
    def _solve(v: Any, alpha: Any, cs: Any, ds: Any): ...
    def matvec(self, v: Any): ...
    def rmatvec(self, v: Any): ...
    def solve(self, v: Any, tol: int = ...): ...
    def rsolve(self, v: Any, tol: int = ...): ...
    def append(self, c: Any, d: Any): ...
    def __array__(self): ...
    def collapse(self) -> None: ...
    def restart_reduce(self, rank: Any): ...
    def simple_reduce(self, rank: Any): ...
    def svd_reduce(self, max_rank: Any, to_retain: Optional[Any] = ...): ...

class BroydenFirst(GenericBroyden):
    alpha: Any = ...
    Gm: Any = ...
    max_rank: Any = ...
    _reduce: Any = ...
    def __init__(self, alpha: Optional[Any] = ..., reduction_method: str = ..., max_rank: Optional[Any] = ...) -> None: ...
    def setup(self, x: Any, F: Any, func: Any) -> None: ...
    def todense(self): ...
    def solve(self, f: Any, tol: int = ...): ...
    def matvec(self, f: Any): ...
    def rsolve(self, f: Any, tol: int = ...): ...
    def rmatvec(self, f: Any): ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...

class BroydenSecond(BroydenFirst):
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...

class Anderson(GenericBroyden):
    alpha: Any = ...
    M: Any = ...
    dx: Any = ...
    df: Any = ...
    gamma: Any = ...
    w0: Any = ...
    def __init__(self, alpha: Optional[Any] = ..., w0: float = ..., M: int = ...) -> None: ...
    def solve(self, f: Any, tol: int = ...): ...
    def matvec(self, f: Any): ...
    a: Any = ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any): ...

class DiagBroyden(GenericBroyden):
    alpha: Any = ...
    def __init__(self, alpha: Optional[Any] = ...) -> None: ...
    d: Any = ...
    def setup(self, x: Any, F: Any, func: Any) -> None: ...
    def solve(self, f: Any, tol: int = ...): ...
    def matvec(self, f: Any): ...
    def rsolve(self, f: Any, tol: int = ...): ...
    def rmatvec(self, f: Any): ...
    def todense(self): ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...

class LinearMixing(GenericBroyden):
    alpha: Any = ...
    def __init__(self, alpha: Optional[Any] = ...) -> None: ...
    def solve(self, f: Any, tol: int = ...): ...
    def matvec(self, f: Any): ...
    def rsolve(self, f: Any, tol: int = ...): ...
    def rmatvec(self, f: Any): ...
    def todense(self): ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...

class ExcitingMixing(GenericBroyden):
    alpha: Any = ...
    alphamax: Any = ...
    beta: Any = ...
    def __init__(self, alpha: Optional[Any] = ..., alphamax: float = ...) -> None: ...
    def setup(self, x: Any, F: Any, func: Any) -> None: ...
    def solve(self, f: Any, tol: int = ...): ...
    def matvec(self, f: Any): ...
    def rsolve(self, f: Any, tol: int = ...): ...
    def rmatvec(self, f: Any): ...
    def todense(self): ...
    def _update(self, x: Any, f: Any, dx: Any, df: Any, dx_norm: Any, df_norm: Any) -> None: ...

class KrylovJacobian(Jacobian):
    preconditioner: Any = ...
    rdiff: Any = ...
    method: Any = ...
    method_kw: Any = ...
    def __init__(self, rdiff: Optional[Any] = ..., method: str = ..., inner_maxiter: int = ..., inner_M: Optional[Any] = ..., outer_k: int = ..., **kw: Any) -> None: ...
    omega: Any = ...
    def _update_diff_step(self) -> None: ...
    def matvec(self, v: Any): ...
    def solve(self, rhs: Any, tol: int = ...): ...
    x0: Any = ...
    f0: Any = ...
    def update(self, x: Any, f: Any) -> None: ...
    op: Any = ...
    def setup(self, x: Any, f: Any, func: Any) -> None: ...

broyden1: Any
broyden2: Any
anderson: Any
linearmixing: Any
diagbroyden: Any
excitingmixing: Any
newton_krylov: Any
