# Stubs for scipy.linalg.interpolative (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

_DTYPE_ERROR: Any
_TYPE_ERROR: Any

def _is_real(A: Any): ...
def seed(seed: Optional[Any] = ...) -> None: ...
def rand(*shape: Any): ...
def interp_decomp(A: Any, eps_or_k: Any, rand: bool = ...): ...
def reconstruct_matrix_from_id(B: Any, idx: Any, proj: Any): ...
def reconstruct_interp_matrix(idx: Any, proj: Any): ...
def reconstruct_skel_matrix(A: Any, k: Any, idx: Any): ...
def id_to_svd(B: Any, idx: Any, proj: Any): ...
def estimate_spectral_norm(A: Any, its: int = ...): ...
def estimate_spectral_norm_diff(A: Any, B: Any, its: int = ...): ...
def svd(A: Any, eps_or_k: Any, rand: bool = ...): ...
def estimate_rank(A: Any, eps: Any): ...
