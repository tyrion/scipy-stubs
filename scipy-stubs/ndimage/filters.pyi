# Stubs for scipy.ndimage.filters (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def correlate1d(input: Any, weights: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def convolve1d(input: Any, weights: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def gaussian_filter1d(input: Any, sigma: Any, axis: int = ..., order: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., truncate: float = ...): ...
def gaussian_filter(input: Any, sigma: Any, order: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., truncate: float = ...): ...
def prewitt(input: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ...): ...
def sobel(input: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ...): ...
def generic_laplace(input: Any, derivative2: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., extra_arguments: Any = ..., extra_keywords: Optional[Any] = ...): ...
def laplace(input: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ...): ...
def gaussian_laplace(input: Any, sigma: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., **kwargs: Any): ...
def generic_gradient_magnitude(input: Any, derivative: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., extra_arguments: Any = ..., extra_keywords: Optional[Any] = ...): ...
def gaussian_gradient_magnitude(input: Any, sigma: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., **kwargs: Any): ...
def correlate(input: Any, weights: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def convolve(input: Any, weights: Any, output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def uniform_filter1d(input: Any, size: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def uniform_filter(input: Any, size: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def minimum_filter1d(input: Any, size: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def maximum_filter1d(input: Any, size: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def minimum_filter(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def maximum_filter(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def rank_filter(input: Any, rank: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def median_filter(input: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def percentile_filter(input: Any, percentile: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ...): ...
def generic_filter1d(input: Any, function: Any, filter_size: Any, axis: int = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ..., extra_arguments: Any = ..., extra_keywords: Optional[Any] = ...): ...
def generic_filter(input: Any, function: Any, size: Optional[Any] = ..., footprint: Optional[Any] = ..., output: Optional[Any] = ..., mode: str = ..., cval: float = ..., origin: int = ..., extra_arguments: Any = ..., extra_keywords: Optional[Any] = ...): ...
