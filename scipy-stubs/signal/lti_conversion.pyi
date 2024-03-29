# Stubs for scipy.signal.lti_conversion (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def tf2ss(num: Any, den: Any): ...
def abcd_normalize(A: Optional[Any] = ..., B: Optional[Any] = ..., C: Optional[Any] = ..., D: Optional[Any] = ...): ...
def ss2tf(A: Any, B: Any, C: Any, D: Any, input: int = ...): ...
def zpk2ss(z: Any, p: Any, k: Any): ...
def ss2zpk(A: Any, B: Any, C: Any, D: Any, input: int = ...): ...
def cont2discrete(system: Any, dt: Any, method: str = ..., alpha: Optional[Any] = ...): ...
