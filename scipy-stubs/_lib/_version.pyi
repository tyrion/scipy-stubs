# Stubs for scipy._lib._version (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class NumpyVersion:
    vstring: Any = ...
    version: Any = ...
    pre_release: str = ...
    is_devversion: Any = ...
    def __init__(self, vstring: Any) -> None: ...
    def _compare_version(self, other: Any): ...
    def _compare_pre_release(self, other: Any): ...
    def _compare(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __repr__(self): ...