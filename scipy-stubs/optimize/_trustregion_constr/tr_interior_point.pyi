# Stubs for scipy.optimize._trustregion_constr.tr_interior_point (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BarrierSubproblem:
    n_vars: Any = ...
    x0: Any = ...
    s0: Any = ...
    fun: Any = ...
    grad: Any = ...
    lagr_hess: Any = ...
    constr: Any = ...
    jac: Any = ...
    barrier_parameter: Any = ...
    tolerance: Any = ...
    n_eq: Any = ...
    n_ineq: Any = ...
    enforce_feasibility: Any = ...
    global_stop_criteria: Any = ...
    xtol: Any = ...
    fun0: Any = ...
    grad0: Any = ...
    constr0: Any = ...
    jac0: Any = ...
    terminate: bool = ...
    def __init__(self, x0: Any, s0: Any, fun: Any, grad: Any, lagr_hess: Any, n_vars: Any, n_ineq: Any, n_eq: Any, constr: Any, jac: Any, barrier_parameter: Any, tolerance: Any, enforce_feasibility: Any, global_stop_criteria: Any, xtol: Any, fun0: Any, grad0: Any, constr_ineq0: Any, jac_ineq0: Any, constr_eq0: Any, jac_eq0: Any) -> None: ...
    def update(self, barrier_parameter: Any, tolerance: Any) -> None: ...
    def get_slack(self, z: Any): ...
    def get_variables(self, z: Any): ...
    def function_and_constraints(self, z: Any): ...
    def _compute_function(self, f: Any, c_ineq: Any, s: Any): ...
    def _compute_constr(self, c_ineq: Any, c_eq: Any, s: Any): ...
    def scaling(self, z: Any): ...
    def gradient_and_jacobian(self, z: Any): ...
    def _compute_gradient(self, g: Any): ...
    def _compute_jacobian(self, J_eq: Any, J_ineq: Any, s: Any): ...
    def _assemble_sparse_jacobian(self, J_eq: Any, J_ineq: Any, s: Any): ...
    def lagrangian_hessian_x(self, z: Any, v: Any): ...
    def lagrangian_hessian_s(self, z: Any, v: Any): ...
    def lagrangian_hessian(self, z: Any, v: Any): ...
    def stop_criteria(self, state: Any, z: Any, last_iteration_failed: Any, optimality: Any, constr_violation: Any, trust_radius: Any, penalty: Any, cg_info: Any): ...

def tr_interior_point(fun: Any, grad: Any, lagr_hess: Any, n_vars: Any, n_ineq: Any, n_eq: Any, constr: Any, jac: Any, x0: Any, fun0: Any, grad0: Any, constr_ineq0: Any, jac_ineq0: Any, constr_eq0: Any, jac_eq0: Any, stop_criteria: Any, enforce_feasibility: Any, xtol: Any, state: Any, initial_barrier_parameter: Any, initial_tolerance: Any, initial_penalty: Any, initial_trust_radius: Any, factorization_method: Any): ...
