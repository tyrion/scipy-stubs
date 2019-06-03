# Stubs for scipy.ndimage.morphology (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def iterate_structure(structure: Any, iterations: Any, origin: Optional[Any] = ...): ...
def generate_binary_structure(rank: Any, connectivity: Any): ...
def binary_erosion(input: Any, structure: Optional[Any] = ..., iterations: int = ..., mask: Optional[Any] = ..., output: Optional[Any] = ..., border_value: int = ..., origin: int = ..., brute_force: bool = ...): ...
def binary_dilation(input: Any, structure: Optional[Any] = ..., iterations: int = ..., mask: Optional[Any] = ..., output: Optional[Any] = ..., border_value: int = ..., origin: int = ..., brute_force: bool = ...): ...
def binary_opening(input: Any, structure: Optional[Any] = ..., iterations: int = ..., output: Optional[Any] = ..., origin: int = ..., mask: Optional[Any] = ..., border_value: int = ..., brute_force: bool = ...): ...
def binary_closing(input: Any, structure: Optional[Any] = ..., iterations: int = ..., output: Optional[Any] = ..., origin: int = ..., mask: Optional[Any] = ..., border_value: int = ..., brute_force: bool = ...): ...
def binary_hit_or_miss(input: Any, structure1: Optional[Any] = ..., structure2: Optional[Any] = ..., output: Optional[Any] = ..., origin1: int = ..., origin2: Optional[Any] = ...): ...
def binary_propagation(input: Any, structure: Optional[Any] = ..., mask: Optional[Any] = ..., output: Optional[Any] = ..., border_value: int = ..., origin: int = ...): ...
def binary_fill_holes(input: Any, structure: Optional[Any] = ..., output: Optional[Any] = ..., origin: int = ...): ...
def grey_erosion(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def grey_dilation(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def grey_opening(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def grey_closing(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def morphological_gradient(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def morphological_laplace(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def white_tophat(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def black_tophat(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., structure: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def distance_transform_bf(input: Any, metric: str = ..., sampling: Optional[Any] = ..., return_distances: bool = ..., return_indices: bool = ..., distances: Optional[Any] = ..., indices: Optional[Any] = ...): ...
def distance_transform_cdt(input: Any, metric: str = ..., return_distances: bool = ..., return_indices: bool = ..., distances: Optional[Any] = ..., indices: Optional[Any] = ...): ...
def distance_transform_edt(input: Any, sampling: Optional[Any] = ..., return_distances: bool = ..., return_indices: bool = ..., distances: Optional[Any] = ..., indices: Optional[Any] = ...): ...
