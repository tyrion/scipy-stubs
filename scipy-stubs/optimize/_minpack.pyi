# Stubs for scipy.optimize._minpack (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def _chkder(m, n, x, fvec, fjac, ldfjac, xp, fvecp, mode, err) -> Any: ...
def _hybrd(*args, **kwargs) -> Any: ...
def _hybrj(*args, **kwargs) -> Any: ...
def _lmder(*args, **kwargs) -> Any: ...
def _lmdif(*args, **kwargs) -> Any: ...

class error(Exception): ...
