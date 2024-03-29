# Stubs for scipy.integrate.odepack (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ODEintWarning(Warning): ...

def odeint(func: Any, y0: Any, t: Any, args: Any = ..., Dfun: Optional[Any] = ..., col_deriv: int = ..., full_output: int = ..., ml: Optional[Any] = ..., mu: Optional[Any] = ..., rtol: Optional[Any] = ..., atol: Optional[Any] = ..., tcrit: Optional[Any] = ..., h0: float = ..., hmax: float = ..., hmin: float = ..., ixpr: int = ..., mxstep: int = ..., mxhnil: int = ..., mxordn: int = ..., mxords: int = ..., printmessg: int = ..., tfirst: bool = ...): ...
