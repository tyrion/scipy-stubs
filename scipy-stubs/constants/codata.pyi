# Stubs for scipy.constants.codata (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

physical_constants: Any
_current_constants = _physical_constants_2014

class ConstantWarning(DeprecationWarning): ...

def value(key: Any): ...
def unit(key: Any): ...
def precision(key: Any): ...
def find(sub: Optional[Any] = ..., disp: bool = ...): ...
