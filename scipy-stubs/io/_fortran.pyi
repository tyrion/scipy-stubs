# Stubs for scipy.io._fortran (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class FortranFile:
    _fp: Any = ...
    _header_dtype: Any = ...
    def __init__(self, filename: Any, mode: str = ..., header_dtype: Any = ...) -> None: ...
    def _read_size(self): ...
    def write_record(self, *items: Any) -> None: ...
    def read_record(self, *dtypes: Any, **kwargs: Any): ...
    def read_ints(self, dtype: str = ...): ...
    def read_reals(self, dtype: str = ...): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: Any, value: Any, tb: Any) -> None: ...