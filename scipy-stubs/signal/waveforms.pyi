# Stubs for scipy.signal.waveforms (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def sawtooth(t: Any, width: int = ...): ...
def square(t: Any, duty: float = ...): ...
def gausspulse(t: Any, fc: int = ..., bw: float = ..., bwr: int = ..., tpr: int = ..., retquad: bool = ..., retenv: bool = ...): ...
def chirp(t: Any, f0: Any, t1: Any, f1: Any, method: str = ..., phi: int = ..., vertex_zero: bool = ...): ...
def sweep_poly(t: Any, poly: Any, phi: int = ...): ...
def unit_impulse(shape: Any, idx: Optional[Any] = ..., dtype: Any = ...): ...
