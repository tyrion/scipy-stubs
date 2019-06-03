# Stubs for scipy.linalg._testutils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class _FakeMatrix:
    _data: Any = ...
    __array_interface__: Any = ...
    def __init__(self, data: Any) -> None: ...

class _FakeMatrix2:
    _data: Any = ...
    def __init__(self, data: Any) -> None: ...
    def __array__(self): ...

def _get_array(shape: Any, dtype: Any): ...
def _id(x: Any): ...
def assert_no_overwrite(call: Any, shapes: Any, dtypes: Optional[Any] = ...) -> None: ...
