# Stubs for scipy.stats.mstats_basic (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from typing import Any, Optional

def argstoarray(*args: Any): ...
def find_repeats(arr: Any): ...
def count_tied_groups(x: Any, use_missing: bool = ...): ...
def rankdata(data: Any, axis: Optional[Any] = ..., use_missing: bool = ...): ...

ModeResult = namedtuple('ModeResult', ['mode', 'count'])

def mode(a: Any, axis: int = ...): ...
def msign(x: Any): ...
def pearsonr(x: Any, y: Any): ...

SpearmanrResult = namedtuple('SpearmanrResult', ['correlation', 'pvalue'])

def spearmanr(x: Any, y: Any, use_ties: bool = ...): ...

KendalltauResult = namedtuple('KendalltauResult', ['correlation', 'pvalue'])

def kendalltau(x: Any, y: Any, use_ties: bool = ..., use_missing: bool = ...): ...
def kendalltau_seasonal(x: Any): ...

PointbiserialrResult = namedtuple('PointbiserialrResult', ['correlation', 'pvalue'])

def pointbiserialr(x: Any, y: Any): ...

LinregressResult = namedtuple('LinregressResult', ['slope', 'intercept', 'rvalue', 'pvalue', 'stderr'])

def linregress(x: Any, y: Optional[Any] = ...): ...
def theilslopes(y: Any, x: Optional[Any] = ..., alpha: float = ...): ...
def sen_seasonal_slopes(x: Any): ...

Ttest_1sampResult = namedtuple('Ttest_1sampResult', ['statistic', 'pvalue'])

def ttest_1samp(a: Any, popmean: Any, axis: int = ...): ...
ttest_onesamp = ttest_1samp

Ttest_indResult = namedtuple('Ttest_indResult', ['statistic', 'pvalue'])

def ttest_ind(a: Any, b: Any, axis: int = ..., equal_var: bool = ...): ...

Ttest_relResult = namedtuple('Ttest_relResult', ['statistic', 'pvalue'])

def ttest_rel(a: Any, b: Any, axis: int = ...): ...

MannwhitneyuResult = namedtuple('MannwhitneyuResult', ['statistic', 'pvalue'])

def mannwhitneyu(x: Any, y: Any, use_continuity: bool = ...): ...

KruskalResult = namedtuple('KruskalResult', ['statistic', 'pvalue'])

def kruskal(*args: Any): ...
kruskalwallis = kruskal

def ks_twosamp(data1: Any, data2: Any, alternative: str = ...): ...
ks_2samp = ks_twosamp

def trima(a: Any, limits: Optional[Any] = ..., inclusive: Any = ...): ...
def trimr(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., axis: Optional[Any] = ...): ...
def trim(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., relative: bool = ..., axis: Optional[Any] = ...): ...
def trimboth(data: Any, proportiontocut: float = ..., inclusive: Any = ..., axis: Optional[Any] = ...): ...
def trimtail(data: Any, proportiontocut: float = ..., tail: str = ..., inclusive: Any = ..., axis: Optional[Any] = ...): ...
trim1 = trimtail

def trimmed_mean(a: Any, limits: Any = ..., inclusive: Any = ..., relative: bool = ..., axis: Optional[Any] = ...): ...
def trimmed_var(a: Any, limits: Any = ..., inclusive: Any = ..., relative: bool = ..., axis: Optional[Any] = ..., ddof: int = ...): ...
def trimmed_std(a: Any, limits: Any = ..., inclusive: Any = ..., relative: bool = ..., axis: Optional[Any] = ..., ddof: int = ...): ...
def trimmed_stde(a: Any, limits: Any = ..., inclusive: Any = ..., axis: Optional[Any] = ...): ...
def tmean(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., axis: Optional[Any] = ...): ...
def tvar(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., axis: int = ..., ddof: int = ...): ...
def tmin(a: Any, lowerlimit: Optional[Any] = ..., axis: int = ..., inclusive: bool = ...): ...
def tmax(a: Any, upperlimit: Optional[Any] = ..., axis: int = ..., inclusive: bool = ...): ...
def tsem(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., axis: int = ..., ddof: int = ...): ...
def winsorize(a: Any, limits: Optional[Any] = ..., inclusive: Any = ..., inplace: bool = ..., axis: Optional[Any] = ...): ...
def moment(a: Any, moment: int = ..., axis: int = ...): ...
def variation(a: Any, axis: int = ...): ...
def skew(a: Any, axis: int = ..., bias: bool = ...): ...
def kurtosis(a: Any, axis: int = ..., fisher: bool = ..., bias: bool = ...): ...

DescribeResult = namedtuple('DescribeResult', ['nobs', 'minmax', 'mean', 'variance', 'skewness', 'kurtosis'])

def describe(a: Any, axis: int = ..., ddof: int = ..., bias: bool = ...): ...

SkewtestResult = namedtuple('SkewtestResult', ['statistic', 'pvalue'])

def skewtest(a: Any, axis: int = ...): ...

KurtosistestResult = namedtuple('KurtosistestResult', ['statistic', 'pvalue'])

def kurtosistest(a: Any, axis: int = ...): ...

NormaltestResult = namedtuple('NormaltestResult', ['statistic', 'pvalue'])

def normaltest(a: Any, axis: int = ...): ...
def mquantiles(a: Any, prob: Any = ..., alphap: float = ..., betap: float = ..., axis: Optional[Any] = ..., limit: Any = ...): ...
def scoreatpercentile(data: Any, per: Any, limit: Any = ..., alphap: float = ..., betap: float = ...): ...
def plotting_positions(data: Any, alpha: float = ..., beta: float = ...): ...
meppf = plotting_positions

def obrientransform(*args: Any): ...
def sem(a: Any, axis: int = ..., ddof: int = ...): ...

F_onewayResult = namedtuple('F_onewayResult', ['statistic', 'pvalue'])

def f_oneway(*args: Any): ...

FriedmanchisquareResult = namedtuple('FriedmanchisquareResult', ['statistic', 'pvalue'])

def friedmanchisquare(*args: Any): ...
