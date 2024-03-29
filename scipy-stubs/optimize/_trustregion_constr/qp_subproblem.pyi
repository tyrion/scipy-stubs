# Stubs for scipy.optimize._trustregion_constr.qp_subproblem (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def eqp_kktfact(H: Any, c: Any, A: Any, b: Any): ...
def sphere_intersections(z: Any, d: Any, trust_radius: Any, entire_line: bool = ...): ...
def box_intersections(z: Any, d: Any, lb: Any, ub: Any, entire_line: bool = ...): ...
def box_sphere_intersections(z: Any, d: Any, lb: Any, ub: Any, trust_radius: Any, entire_line: bool = ..., extra_info: bool = ...): ...
def inside_box_boundaries(x: Any, lb: Any, ub: Any): ...
def modified_dogleg(A: Any, Y: Any, b: Any, trust_radius: Any, lb: Any, ub: Any): ...
def projected_cg(H: Any, c: Any, Z: Any, Y: Any, b: Any, trust_radius: Any = ..., lb: Optional[Any] = ..., ub: Optional[Any] = ..., tol: Optional[Any] = ..., max_iter: Optional[Any] = ..., max_infeasible_iter: Optional[Any] = ..., return_all: bool = ...): ...
