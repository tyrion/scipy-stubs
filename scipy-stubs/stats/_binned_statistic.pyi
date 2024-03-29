# Stubs for scipy.stats._binned_statistic (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from typing import Any, Optional

BinnedStatisticResult = namedtuple('BinnedStatisticResult', ['statistic', 'bin_edges', 'binnumber'])

def binned_statistic(x: Any, values: Any, statistic: str = ..., bins: int = ..., range: Optional[Any] = ...): ...

BinnedStatistic2dResult = namedtuple('BinnedStatistic2dResult', ['statistic', 'x_edge', 'y_edge', 'binnumber'])

def binned_statistic_2d(x: Any, y: Any, values: Any, statistic: str = ..., bins: int = ..., range: Optional[Any] = ..., expand_binnumbers: bool = ...): ...

BinnedStatisticddResult = namedtuple('BinnedStatisticddResult', ['statistic', 'bin_edges', 'binnumber'])

def binned_statistic_dd(sample: Any, values: Any, statistic: str = ..., bins: int = ..., range: Optional[Any] = ..., expand_binnumbers: bool = ...): ...
