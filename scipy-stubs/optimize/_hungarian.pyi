# Stubs for scipy.optimize._hungarian (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def linear_sum_assignment(cost_matrix: Any): ...

class _Hungary:
    C: Any = ...
    row_uncovered: Any = ...
    col_uncovered: Any = ...
    Z0_r: int = ...
    Z0_c: int = ...
    path: Any = ...
    marked: Any = ...
    def __init__(self, cost_matrix: Any) -> None: ...
    def _clear_covers(self) -> None: ...

def _step1(state: Any): ...
def _step3(state: Any): ...
def _step4(state: Any): ...
def _step5(state: Any): ...
def _step6(state: Any): ...
