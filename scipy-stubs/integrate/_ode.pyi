# Stubs for scipy.integrate._ode (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ode:
    stiff: int = ...
    f: Any = ...
    jac: Any = ...
    f_params: Any = ...
    jac_params: Any = ...
    _y: Any = ...
    def __init__(self, f: Any, jac: Optional[Any] = ...) -> None: ...
    @property
    def y(self): ...
    t: Any = ...
    def set_initial_value(self, y: Any, t: float = ...): ...
    _integrator: Any = ...
    def set_integrator(self, name: Any, **integrator_params: Any): ...
    def integrate(self, t: Any, step: bool = ..., relax: bool = ...): ...
    def successful(self): ...
    def get_return_code(self): ...
    def set_f_params(self, *args: Any): ...
    def set_jac_params(self, *args: Any): ...
    def set_solout(self, solout: Any) -> None: ...

class complex_ode(ode):
    cf: Any = ...
    cjac: Any = ...
    def __init__(self, f: Any, jac: Optional[Any] = ...) -> None: ...
    def _wrap(self, t: Any, y: Any, *f_args: Any): ...
    def _wrap_jac(self, t: Any, y: Any, *jac_args: Any): ...
    @property
    def y(self): ...
    def set_integrator(self, name: Any, **integrator_params: Any): ...
    tmp: Any = ...
    def set_initial_value(self, y: Any, t: float = ...): ...
    def integrate(self, t: Any, step: bool = ..., relax: bool = ...): ...
    def set_solout(self, solout: Any) -> None: ...

class IntegratorConcurrencyError(RuntimeError):
    def __init__(self, name: Any) -> None: ...

class IntegratorBase:
    runner: Any = ...
    success: Any = ...
    istate: Any = ...
    supports_run_relax: Any = ...
    supports_step: Any = ...
    supports_solout: bool = ...
    integrator_classes: Any = ...
    scalar: Any = ...
    handle: Any = ...
    def acquire_new_handle(self) -> None: ...
    def check_handle(self) -> None: ...
    def reset(self, n: Any, has_jac: Any) -> None: ...
    def run(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any) -> None: ...
    def step(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any) -> None: ...
    def run_relax(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any) -> None: ...

class vode(IntegratorBase):
    runner: Any = ...
    messages: Any = ...
    supports_run_relax: int = ...
    supports_step: int = ...
    active_global_handle: int = ...
    meth: int = ...
    with_jacobian: Any = ...
    rtol: Any = ...
    atol: Any = ...
    mu: Any = ...
    ml: Any = ...
    order: Any = ...
    nsteps: Any = ...
    max_step: Any = ...
    min_step: Any = ...
    first_step: Any = ...
    success: int = ...
    initialized: bool = ...
    def __init__(self, method: str = ..., with_jacobian: bool = ..., rtol: float = ..., atol: float = ..., lband: Optional[Any] = ..., uband: Optional[Any] = ..., order: int = ..., nsteps: int = ..., max_step: float = ..., min_step: float = ..., first_step: float = ...) -> None: ...
    def _determine_mf_and_set_bands(self, has_jac: Any): ...
    rwork: Any = ...
    iwork: Any = ...
    call_args: Any = ...
    def reset(self, n: Any, has_jac: Any) -> None: ...
    istate: Any = ...
    def run(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any): ...
    def step(self, *args: Any): ...
    def run_relax(self, *args: Any): ...

class zvode(vode):
    runner: Any = ...
    supports_run_relax: int = ...
    supports_step: int = ...
    scalar: Any = ...
    active_global_handle: int = ...
    zwork: Any = ...
    rwork: Any = ...
    iwork: Any = ...
    call_args: Any = ...
    success: int = ...
    initialized: bool = ...
    def reset(self, n: Any, has_jac: Any) -> None: ...

class dopri5(IntegratorBase):
    runner: Any = ...
    name: str = ...
    supports_solout: bool = ...
    messages: Any = ...
    rtol: Any = ...
    atol: Any = ...
    nsteps: Any = ...
    max_step: Any = ...
    first_step: Any = ...
    safety: Any = ...
    ifactor: Any = ...
    dfactor: Any = ...
    beta: Any = ...
    verbosity: Any = ...
    success: int = ...
    def __init__(self, rtol: float = ..., atol: float = ..., nsteps: int = ..., max_step: float = ..., first_step: float = ..., safety: float = ..., ifactor: float = ..., dfactor: float = ..., beta: float = ..., method: Optional[Any] = ..., verbosity: int = ...) -> None: ...
    solout: Any = ...
    solout_cmplx: Any = ...
    iout: int = ...
    def set_solout(self, solout: Any, complex: bool = ...) -> None: ...
    work: Any = ...
    iwork: Any = ...
    call_args: Any = ...
    def reset(self, n: Any, has_jac: Any) -> None: ...
    istate: Any = ...
    def run(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any): ...
    def _solout(self, nr: Any, xold: Any, x: Any, y: Any, nd: Any, icomp: Any, con: Any): ...

class dop853(dopri5):
    runner: Any = ...
    name: str = ...
    def __init__(self, rtol: float = ..., atol: float = ..., nsteps: int = ..., max_step: float = ..., first_step: float = ..., safety: float = ..., ifactor: float = ..., dfactor: float = ..., beta: float = ..., method: Optional[Any] = ..., verbosity: int = ...) -> None: ...
    work: Any = ...
    iwork: Any = ...
    call_args: Any = ...
    success: int = ...
    def reset(self, n: Any, has_jac: Any) -> None: ...

class lsoda(IntegratorBase):
    runner: Any = ...
    active_global_handle: int = ...
    messages: Any = ...
    with_jacobian: Any = ...
    rtol: Any = ...
    atol: Any = ...
    mu: Any = ...
    ml: Any = ...
    max_order_ns: Any = ...
    max_order_s: Any = ...
    nsteps: Any = ...
    max_step: Any = ...
    min_step: Any = ...
    first_step: Any = ...
    ixpr: Any = ...
    max_hnil: Any = ...
    success: int = ...
    initialized: bool = ...
    def __init__(self, with_jacobian: bool = ..., rtol: float = ..., atol: float = ..., lband: Optional[Any] = ..., uband: Optional[Any] = ..., nsteps: int = ..., max_step: float = ..., min_step: float = ..., first_step: float = ..., ixpr: int = ..., max_hnil: int = ..., max_order_ns: int = ..., max_order_s: int = ..., method: Optional[Any] = ...) -> None: ...
    rwork: Any = ...
    iwork: Any = ...
    call_args: Any = ...
    def reset(self, n: Any, has_jac: Any) -> None: ...
    istate: Any = ...
    def run(self, f: Any, jac: Any, y0: Any, t0: Any, t1: Any, f_params: Any, jac_params: Any): ...
    def step(self, *args: Any): ...
    def run_relax(self, *args: Any): ...
