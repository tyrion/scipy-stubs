# Stubs for scipy._lib._util (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from typing import Any, Optional

def _valarray(shape: Any, value: Any = ..., typecode: Optional[Any] = ...): ...
def _lazywhere(cond: Any, arrays: Any, f: Any, fillvalue: Optional[Any] = ..., f2: Optional[Any] = ...): ...
def _lazyselect(condlist: Any, choicelist: Any, arrays: Any, default: int = ...): ...
def _aligned_zeros(shape: Any, dtype: Any = ..., order: str = ..., align: Optional[Any] = ...): ...
def _prune_array(array: Any): ...

class DeprecatedImport:
    _old_name: Any = ...
    _new_name: Any = ...
    _mod: Any = ...
    def __init__(self, old_module_name: Any, new_module_name: Any) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, name: Any): ...

def check_random_state(seed: Any): ...
def _asarray_validated(a: Any, check_finite: bool = ..., sparse_ok: bool = ..., objects_ok: bool = ..., mask_ok: bool = ..., as_inexact: bool = ...): ...

ArgSpec = namedtuple('ArgSpec', ['args', 'varargs', 'keywords', 'defaults'])

def getargspec_no_self(func: Any): ...