# Stubs for scipy.optimize._linprog_ip (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimize import OptimizeResult, OptimizeWarning, _check_unknown_options
from typing import Any, Optional

def _clean_inputs(c: Any, A_ub: Optional[Any] = ..., b_ub: Optional[Any] = ..., A_eq: Optional[Any] = ..., b_eq: Optional[Any] = ..., bounds: Optional[Any] = ...): ...
def _presolve(c: Any, A_ub: Any, b_ub: Any, A_eq: Any, b_eq: Any, bounds: Any, rr: Any): ...
def _get_Abc(c: Any, c0: int = ..., A_ub: Optional[Any] = ..., b_ub: Optional[Any] = ..., A_eq: Optional[Any] = ..., b_eq: Optional[Any] = ..., bounds: Optional[Any] = ..., undo: Any = ...): ...
def _postprocess(x: Any, c: Any, A_ub: Optional[Any] = ..., b_ub: Optional[Any] = ..., A_eq: Optional[Any] = ..., b_eq: Optional[Any] = ..., bounds: Optional[Any] = ..., complete: bool = ..., undo: Any = ..., status: int = ..., message: str = ..., tol: float = ...): ...
def _get_solver(sparse: bool = ..., lstsq: bool = ..., sym_pos: bool = ..., cholesky: bool = ...): ...
def _get_delta(A: Any, b: Any, c: Any, x: Any, y: Any, z: Any, tau: Any, kappa: Any, gamma: Any, eta: Any, sparse: bool = ..., lstsq: bool = ..., sym_pos: bool = ..., cholesky: bool = ..., pc: bool = ..., ip: bool = ..., permc_spec: str = ...): ...
def _sym_solve(Dinv: Any, M: Any, A: Any, r1: Any, r2: Any, solve: Any, splu: bool = ...): ...
def _get_step(x: Any, d_x: Any, z: Any, d_z: Any, tau: Any, d_tau: Any, kappa: Any, d_kappa: Any, alpha0: Any): ...
def _get_message(status: Any): ...
def _do_step(x: Any, y: Any, z: Any, tau: Any, kappa: Any, d_x: Any, d_y: Any, d_z: Any, d_tau: Any, d_kappa: Any, alpha: Any): ...
def _get_blind_start(shape: Any): ...
def _indicators(A: Any, b: Any, c: Any, c0: Any, x: Any, y: Any, z: Any, tau: Any, kappa: Any): ...
def _display_iter(rho_p: Any, rho_d: Any, rho_g: Any, alpha: Any, rho_mu: Any, obj: Any, header: bool = ...) -> None: ...
def _ip_hsd(A: Any, b: Any, c: Any, c0: Any, alpha0: Any, beta: Any, maxiter: Any, disp: Any, tol: Any, sparse: Any, lstsq: Any, sym_pos: Any, cholesky: Any, pc: Any, ip: Any, permc_spec: Any): ...
def _linprog_ip(c: Any, A_ub: Optional[Any] = ..., b_ub: Optional[Any] = ..., A_eq: Optional[Any] = ..., b_eq: Optional[Any] = ..., bounds: Optional[Any] = ..., callback: Optional[Any] = ..., alpha0: float = ..., beta: float = ..., maxiter: int = ..., disp: bool = ..., tol: float = ..., sparse: bool = ..., lstsq: bool = ..., sym_pos: bool = ..., cholesky: Optional[Any] = ..., pc: bool = ..., ip: bool = ..., presolve: bool = ..., permc_spec: str = ..., rr: bool = ..., _sparse_presolve: bool = ..., **unknown_options: Any): ...
