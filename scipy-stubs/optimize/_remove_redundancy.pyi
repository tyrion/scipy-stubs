# Stubs for scipy.optimize._remove_redundancy (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def _row_count(A: Any): ...
def _get_densest(A: Any, eligibleRows: Any): ...
def _remove_zero_rows(A: Any, b: Any): ...
def bg_update_dense(plu: Any, perm_r: Any, v: Any, j: Any): ...
def _remove_redundancy_dense(A: Any, rhs: Any): ...
def _remove_redundancy_sparse(A: Any, rhs: Any): ...
def _remove_redundancy(A: Any, b: Any): ...