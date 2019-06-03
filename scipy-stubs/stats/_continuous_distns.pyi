# Stubs for scipy.stats._continuous_distns (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._distn_infrastructure import rv_continuous
from typing import Any, Optional

class ksone_gen(rv_continuous):
    def _cdf(self, x: Any, n: Any): ...
    def _ppf(self, q: Any, n: Any): ...

ksone: Any

class kstwobign_gen(rv_continuous):
    def _cdf(self, x: Any): ...
    def _sf(self, x: Any): ...
    def _ppf(self, q: Any): ...

kstwobign: Any

class norm_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _logcdf(self, x: Any): ...
    def _sf(self, x: Any): ...
    def _logsf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _isf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...
    def fit(self, data: Any, **kwds: Any): ...

norm: Any

class alpha_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, a: Any): ...
    def _logpdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _stats(self, a: Any): ...

alpha: Any

class anglit_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

anglit: Any

class arcsine_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

arcsine: Any

class FitDataError(ValueError):
    args: Any = ...
    def __init__(self, distr: Any, lower: Any, upper: Any) -> None: ...

class FitSolverError(RuntimeError):
    args: Any = ...
    def __init__(self, mesg: Any) -> None: ...

class beta_gen(rv_continuous):
    def _rvs(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _logpdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _ppf(self, q: Any, a: Any, b: Any): ...
    def _stats(self, a: Any, b: Any): ...
    def _fitstart(self, data: Any): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

beta: Any

class betaprime_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _logpdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _munp(self, n: Any, a: Any, b: Any): ...

betaprime: Any

class bradford_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any, moments: str = ...): ...
    def _entropy(self, c: Any): ...

bradford: Any

class burr_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, c: Any, d: Any): ...
    def _cdf(self, x: Any, c: Any, d: Any): ...
    def _ppf(self, q: Any, c: Any, d: Any): ...
    def _munp(self, n: Any, c: Any, d: Any): ...

burr: Any

class burr12_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, c: Any, d: Any): ...
    def _logpdf(self, x: Any, c: Any, d: Any): ...
    def _cdf(self, x: Any, c: Any, d: Any): ...
    def _logcdf(self, x: Any, c: Any, d: Any): ...
    def _sf(self, x: Any, c: Any, d: Any): ...
    def _logsf(self, x: Any, c: Any, d: Any): ...
    def _ppf(self, q: Any, c: Any, d: Any): ...
    def _munp(self, n: Any, c: Any, d: Any): ...

burr12: Any

class fisk_gen(burr_gen):
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, x: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

fisk: Any

class cauchy_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _sf(self, x: Any): ...
    def _isf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...
    def _fitstart(self, data: Any, args: Optional[Any] = ...): ...

cauchy: Any

class chi_gen(rv_continuous):
    def _rvs(self, df: Any): ...
    def _pdf(self, x: Any, df: Any): ...
    def _logpdf(self, x: Any, df: Any): ...
    def _cdf(self, x: Any, df: Any): ...
    def _ppf(self, q: Any, df: Any): ...
    def _stats(self, df: Any): ...

chi: Any

class chi2_gen(rv_continuous):
    def _rvs(self, df: Any): ...
    def _pdf(self, x: Any, df: Any): ...
    def _logpdf(self, x: Any, df: Any): ...
    def _cdf(self, x: Any, df: Any): ...
    def _sf(self, x: Any, df: Any): ...
    def _isf(self, p: Any, df: Any): ...
    def _ppf(self, p: Any, df: Any): ...
    def _stats(self, df: Any): ...

chi2: Any

class cosine_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

cosine: Any

class dgamma_gen(rv_continuous):
    def _rvs(self, a: Any): ...
    def _pdf(self, x: Any, a: Any): ...
    def _logpdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _sf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _stats(self, a: Any): ...

dgamma: Any

class dweibull_gen(rv_continuous):
    def _rvs(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _stats(self, c: Any): ...

dweibull: Any

class expon_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _sf(self, x: Any): ...
    def _logsf(self, x: Any): ...
    def _isf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

expon: Any

class exponnorm_gen(rv_continuous):
    def _rvs(self, K: Any): ...
    def _pdf(self, x: Any, K: Any): ...
    def _logpdf(self, x: Any, K: Any): ...
    def _cdf(self, x: Any, K: Any): ...
    def _sf(self, x: Any, K: Any): ...
    def _stats(self, K: Any): ...

exponnorm: Any

class exponweib_gen(rv_continuous):
    def _pdf(self, x: Any, a: Any, c: Any): ...
    def _logpdf(self, x: Any, a: Any, c: Any): ...
    def _cdf(self, x: Any, a: Any, c: Any): ...
    def _ppf(self, q: Any, a: Any, c: Any): ...

exponweib: Any

class exponpow_gen(rv_continuous):
    def _pdf(self, x: Any, b: Any): ...
    def _logpdf(self, x: Any, b: Any): ...
    def _cdf(self, x: Any, b: Any): ...
    def _sf(self, x: Any, b: Any): ...
    def _isf(self, x: Any, b: Any): ...
    def _ppf(self, q: Any, b: Any): ...

exponpow: Any

class fatiguelife_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...

fatiguelife: Any

class foldcauchy_gen(rv_continuous):
    def _rvs(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _stats(self, c: Any): ...

foldcauchy: Any

class f_gen(rv_continuous):
    def _rvs(self, dfn: Any, dfd: Any): ...
    def _pdf(self, x: Any, dfn: Any, dfd: Any): ...
    def _logpdf(self, x: Any, dfn: Any, dfd: Any): ...
    def _cdf(self, x: Any, dfn: Any, dfd: Any): ...
    def _sf(self, x: Any, dfn: Any, dfd: Any): ...
    def _ppf(self, q: Any, dfn: Any, dfd: Any): ...
    def _stats(self, dfn: Any, dfd: Any): ...

f: Any

class foldnorm_gen(rv_continuous):
    def _argcheck(self, c: Any): ...
    def _rvs(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _stats(self, c: Any): ...

foldnorm: Any

class weibull_min_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _sf(self, x: Any, c: Any): ...
    def _logsf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

weibull_min: Any

class weibull_max_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _logcdf(self, x: Any, c: Any): ...
    def _sf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

weibull_max: Any

class frechet_r_gen(weibull_min_gen):
    def __call__(self, *args: Any, **kwargs: Any): ...
    def cdf(self, *args: Any, **kwargs: Any): ...
    def entropy(self, *args: Any, **kwargs: Any): ...
    def expect(self, *args: Any, **kwargs: Any): ...
    def fit(self, *args: Any, **kwargs: Any): ...
    def fit_loc_scale(self, *args: Any, **kwargs: Any): ...
    def freeze(self, *args: Any, **kwargs: Any): ...
    def interval(self, *args: Any, **kwargs: Any): ...
    def isf(self, *args: Any, **kwargs: Any): ...
    def logcdf(self, *args: Any, **kwargs: Any): ...
    def logpdf(self, *args: Any, **kwargs: Any): ...
    def logsf(self, *args: Any, **kwargs: Any): ...
    def mean(self, *args: Any, **kwargs: Any): ...
    def median(self, *args: Any, **kwargs: Any): ...
    def moment(self, *args: Any, **kwargs: Any): ...
    def nnlf(self, *args: Any, **kwargs: Any): ...
    def pdf(self, *args: Any, **kwargs: Any): ...
    def ppf(self, *args: Any, **kwargs: Any): ...
    def rvs(self, *args: Any, **kwargs: Any): ...
    def sf(self, *args: Any, **kwargs: Any): ...
    def stats(self, *args: Any, **kwargs: Any): ...
    def std(self, *args: Any, **kwargs: Any): ...
    def var(self, *args: Any, **kwargs: Any): ...

frechet_r: Any

class frechet_l_gen(weibull_max_gen):
    def __call__(self, *args: Any, **kwargs: Any): ...
    def cdf(self, *args: Any, **kwargs: Any): ...
    def entropy(self, *args: Any, **kwargs: Any): ...
    def expect(self, *args: Any, **kwargs: Any): ...
    def fit(self, *args: Any, **kwargs: Any): ...
    def fit_loc_scale(self, *args: Any, **kwargs: Any): ...
    def freeze(self, *args: Any, **kwargs: Any): ...
    def interval(self, *args: Any, **kwargs: Any): ...
    def isf(self, *args: Any, **kwargs: Any): ...
    def logcdf(self, *args: Any, **kwargs: Any): ...
    def logpdf(self, *args: Any, **kwargs: Any): ...
    def logsf(self, *args: Any, **kwargs: Any): ...
    def mean(self, *args: Any, **kwargs: Any): ...
    def median(self, *args: Any, **kwargs: Any): ...
    def moment(self, *args: Any, **kwargs: Any): ...
    def nnlf(self, *args: Any, **kwargs: Any): ...
    def pdf(self, *args: Any, **kwargs: Any): ...
    def ppf(self, *args: Any, **kwargs: Any): ...
    def rvs(self, *args: Any, **kwargs: Any): ...
    def sf(self, *args: Any, **kwargs: Any): ...
    def stats(self, *args: Any, **kwargs: Any): ...
    def std(self, *args: Any, **kwargs: Any): ...
    def var(self, *args: Any, **kwargs: Any): ...

frechet_l: Any

class genlogistic_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...

genlogistic: Any

class genpareto_gen(rv_continuous):
    b: Any = ...
    def _argcheck(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _sf(self, x: Any, c: Any): ...
    def _logsf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _isf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

genpareto: Any

class genexpon_gen(rv_continuous):
    def _pdf(self, x: Any, a: Any, b: Any, c: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any, c: Any): ...
    def _logpdf(self, x: Any, a: Any, b: Any, c: Any): ...

genexpon: Any

class genextreme_gen(rv_continuous):
    b: Any = ...
    a: Any = ...
    def _argcheck(self, c: Any): ...
    def _loglogcdf(self, x: Any, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _logcdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _sf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _isf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...
    def _fitstart(self, data: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

genextreme: Any

class gamma_gen(rv_continuous):
    def _rvs(self, a: Any): ...
    def _pdf(self, x: Any, a: Any): ...
    def _logpdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _sf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _stats(self, a: Any): ...
    def _entropy(self, a: Any): ...
    def _fitstart(self, data: Any): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

gamma: Any

class erlang_gen(gamma_gen):
    def _argcheck(self, a: Any): ...
    def _fitstart(self, data: Any): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

erlang: Any

class gengamma_gen(rv_continuous):
    def _argcheck(self, a: Any, c: Any): ...
    def _pdf(self, x: Any, a: Any, c: Any): ...
    def _logpdf(self, x: Any, a: Any, c: Any): ...
    def _cdf(self, x: Any, a: Any, c: Any): ...
    def _sf(self, x: Any, a: Any, c: Any): ...
    def _ppf(self, q: Any, a: Any, c: Any): ...
    def _isf(self, q: Any, a: Any, c: Any): ...
    def _munp(self, n: Any, a: Any, c: Any): ...
    def _entropy(self, a: Any, c: Any): ...

gengamma: Any

class genhalflogistic_gen(rv_continuous):
    b: Any = ...
    def _argcheck(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _entropy(self, c: Any): ...

genhalflogistic: Any

class gompertz_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _entropy(self, c: Any): ...

gompertz: Any

class gumbel_r_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _logcdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

gumbel_r: Any

class gumbel_l_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _logsf(self, x: Any): ...
    def _sf(self, x: Any): ...
    def _isf(self, x: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

gumbel_l: Any

class halfcauchy_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

halfcauchy: Any

class halflogistic_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _munp(self, n: Any): ...
    def _entropy(self): ...

halflogistic: Any

class halfnorm_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

halfnorm: Any

class hypsecant_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

hypsecant: Any

class gausshyper_gen(rv_continuous):
    def _argcheck(self, a: Any, b: Any, c: Any, z: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any, c: Any, z: Any): ...
    def _munp(self, n: Any, a: Any, b: Any, c: Any, z: Any): ...

gausshyper: Any

class invgamma_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, a: Any): ...
    def _logpdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _sf(self, x: Any, a: Any): ...
    def _isf(self, q: Any, a: Any): ...
    def _stats(self, a: Any, moments: str = ...): ...
    def _entropy(self, a: Any): ...

invgamma: Any

class invgauss_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self, mu: Any): ...
    def _pdf(self, x: Any, mu: Any): ...
    def _logpdf(self, x: Any, mu: Any): ...
    def _cdf(self, x: Any, mu: Any): ...
    def _stats(self, mu: Any): ...

invgauss: Any

class norminvgauss_gen(rv_continuous):
    _support_mask: Any = ...
    def _argcheck(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _rvs(self, a: Any, b: Any): ...
    def _stats(self, a: Any, b: Any): ...

norminvgauss: Any

class invweibull_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

invweibull: Any

class johnsonsb_gen(rv_continuous):
    _support_mask: Any = ...
    def _argcheck(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _ppf(self, q: Any, a: Any, b: Any): ...

johnsonsb: Any

class johnsonsu_gen(rv_continuous):
    def _argcheck(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _ppf(self, q: Any, a: Any, b: Any): ...

johnsonsu: Any

class laplace_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

laplace: Any

class levy_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...

levy: Any

class levy_l_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...

levy_l: Any

class levy_stable_gen(rv_continuous):
    def _rvs(self, alpha: Any, beta: Any): ...
    def _argcheck(self, alpha: Any, beta: Any): ...
    def _pdf(self, x: Any, alpha: Any, beta: Any) -> None: ...

levy_stable: Any

class logistic_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _sf(self, x: Any): ...
    def _isf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

logistic: Any

class loggamma_gen(rv_continuous):
    def _rvs(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...

loggamma: Any

class loglaplace_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...
    def _entropy(self, c: Any): ...

loglaplace: Any

class lognorm_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self, s: Any): ...
    def _pdf(self, x: Any, s: Any): ...
    def _logpdf(self, x: Any, s: Any): ...
    def _cdf(self, x: Any, s: Any): ...
    def _logcdf(self, x: Any, s: Any): ...
    def _ppf(self, q: Any, s: Any): ...
    def _sf(self, x: Any, s: Any): ...
    def _logsf(self, x: Any, s: Any): ...
    def _stats(self, s: Any): ...
    def _entropy(self, s: Any): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

lognorm: Any

class gilbrat_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

gilbrat: Any

class maxwell_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

maxwell: Any

class mielke_gen(rv_continuous):
    def _pdf(self, x: Any, k: Any, s: Any): ...
    def _cdf(self, x: Any, k: Any, s: Any): ...
    def _ppf(self, q: Any, k: Any, s: Any): ...

mielke: Any

class kappa4_gen(rv_continuous):
    a: Any = ...
    b: Any = ...
    def _argcheck(self, h: Any, k: Any): ...
    def _pdf(self, x: Any, h: Any, k: Any): ...
    def _logpdf(self, x: Any, h: Any, k: Any): ...
    def _cdf(self, x: Any, h: Any, k: Any): ...
    def _logcdf(self, x: Any, h: Any, k: Any): ...
    def _ppf(self, q: Any, h: Any, k: Any): ...
    def _stats(self, h: Any, k: Any): ...

kappa4: Any

class kappa3_gen(rv_continuous):
    def _argcheck(self, a: Any): ...
    def _pdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _stats(self, a: Any): ...

kappa3: Any

class moyal_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _sf(self, x: Any): ...
    def _ppf(self, x: Any): ...
    def _stats(self): ...
    def _munp(self, n: Any): ...

moyal: Any

class nakagami_gen(rv_continuous):
    def _pdf(self, x: Any, nu: Any): ...
    def _cdf(self, x: Any, nu: Any): ...
    def _ppf(self, q: Any, nu: Any): ...
    def _stats(self, nu: Any): ...

nakagami: Any

class ncx2_gen(rv_continuous):
    def _rvs(self, df: Any, nc: Any): ...
    def _logpdf(self, x: Any, df: Any, nc: Any): ...
    def _pdf(self, x: Any, df: Any, nc: Any): ...
    def _cdf(self, x: Any, df: Any, nc: Any): ...
    def _ppf(self, q: Any, df: Any, nc: Any): ...
    def _stats(self, df: Any, nc: Any): ...

ncx2: Any

class ncf_gen(rv_continuous):
    def _rvs(self, dfn: Any, dfd: Any, nc: Any): ...
    def _pdf_skip(self, x: Any, dfn: Any, dfd: Any, nc: Any) -> None: ...
    def _cdf(self, x: Any, dfn: Any, dfd: Any, nc: Any): ...
    def _ppf(self, q: Any, dfn: Any, dfd: Any, nc: Any): ...
    def _munp(self, n: Any, dfn: Any, dfd: Any, nc: Any): ...
    def _stats(self, dfn: Any, dfd: Any, nc: Any): ...

ncf: Any

class t_gen(rv_continuous):
    def _rvs(self, df: Any): ...
    def _pdf(self, x: Any, df: Any): ...
    def _logpdf(self, x: Any, df: Any): ...
    def _cdf(self, x: Any, df: Any): ...
    def _sf(self, x: Any, df: Any): ...
    def _ppf(self, q: Any, df: Any): ...
    def _isf(self, q: Any, df: Any): ...
    def _stats(self, df: Any): ...

t: Any

class nct_gen(rv_continuous):
    def _argcheck(self, df: Any, nc: Any): ...
    def _rvs(self, df: Any, nc: Any): ...
    def _pdf(self, x: Any, df: Any, nc: Any): ...
    def _cdf(self, x: Any, df: Any, nc: Any): ...
    def _ppf(self, q: Any, df: Any, nc: Any): ...
    def _stats(self, df: Any, nc: Any, moments: str = ...): ...

nct: Any

class pareto_gen(rv_continuous):
    def _pdf(self, x: Any, b: Any): ...
    def _cdf(self, x: Any, b: Any): ...
    def _ppf(self, q: Any, b: Any): ...
    def _sf(self, x: Any, b: Any): ...
    def _stats(self, b: Any, moments: str = ...): ...
    def _entropy(self, c: Any): ...

pareto: Any

class lomax_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _sf(self, x: Any, c: Any): ...
    def _logsf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...
    def _entropy(self, c: Any): ...

lomax: Any

class pearson3_gen(rv_continuous):
    def _preprocess(self, x: Any, skew: Any): ...
    def _argcheck(self, skew: Any): ...
    def _stats(self, skew: Any): ...
    def _pdf(self, x: Any, skew: Any): ...
    def _logpdf(self, x: Any, skew: Any): ...
    def _cdf(self, x: Any, skew: Any): ...
    def _rvs(self, skew: Any): ...
    def _ppf(self, q: Any, skew: Any): ...

pearson3: Any

class powerlaw_gen(rv_continuous):
    def _pdf(self, x: Any, a: Any): ...
    def _logpdf(self, x: Any, a: Any): ...
    def _cdf(self, x: Any, a: Any): ...
    def _logcdf(self, x: Any, a: Any): ...
    def _ppf(self, q: Any, a: Any): ...
    def _stats(self, a: Any): ...
    def _entropy(self, a: Any): ...

powerlaw: Any

class powerlognorm_gen(rv_continuous):
    _support_mask: Any = ...
    def _pdf(self, x: Any, c: Any, s: Any): ...
    def _cdf(self, x: Any, c: Any, s: Any): ...
    def _ppf(self, q: Any, c: Any, s: Any): ...

powerlognorm: Any

class powernorm_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _logpdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...

powernorm: Any

class rdist_gen(rv_continuous):
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _munp(self, n: Any, c: Any): ...

rdist: Any

class rayleigh_gen(rv_continuous):
    _support_mask: Any = ...
    def _rvs(self): ...
    def _pdf(self, r: Any): ...
    def _logpdf(self, r: Any): ...
    def _cdf(self, r: Any): ...
    def _ppf(self, q: Any): ...
    def _sf(self, r: Any): ...
    def _logsf(self, r: Any): ...
    def _isf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

rayleigh: Any

class reciprocal_gen(rv_continuous):
    a: Any = ...
    b: Any = ...
    d: Any = ...
    def _argcheck(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _logpdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _ppf(self, q: Any, a: Any, b: Any): ...
    def _munp(self, n: Any, a: Any, b: Any): ...
    def _entropy(self, a: Any, b: Any): ...

reciprocal: Any

class rice_gen(rv_continuous):
    def _argcheck(self, b: Any): ...
    def _rvs(self, b: Any): ...
    def _cdf(self, x: Any, b: Any): ...
    def _ppf(self, q: Any, b: Any): ...
    def _pdf(self, x: Any, b: Any): ...
    def _munp(self, n: Any, b: Any): ...

rice: Any

class recipinvgauss_gen(rv_continuous):
    def _pdf(self, x: Any, mu: Any): ...
    def _logpdf(self, x: Any, mu: Any): ...
    def _cdf(self, x: Any, mu: Any): ...
    def _rvs(self, mu: Any): ...

recipinvgauss: Any

class semicircular_gen(rv_continuous):
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _stats(self): ...
    def _entropy(self): ...

semicircular: Any

class skew_norm_gen(rv_continuous):
    def _argcheck(self, a: Any): ...
    def _pdf(self, x: Any, a: Any): ...
    def _cdf_single(self, x: Any, *args: Any): ...
    def _sf(self, x: Any, a: Any): ...
    def _rvs(self, a: Any): ...
    def _stats(self, a: Any, moments: str = ...): ...

skewnorm: Any

class trapz_gen(rv_continuous):
    def _argcheck(self, c: Any, d: Any): ...
    def _pdf(self, x: Any, c: Any, d: Any): ...
    def _cdf(self, x: Any, c: Any, d: Any): ...
    def _ppf(self, q: Any, c: Any, d: Any): ...

trapz: Any

class triang_gen(rv_continuous):
    def _rvs(self, c: Any): ...
    def _argcheck(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _stats(self, c: Any): ...
    def _entropy(self, c: Any): ...

triang: Any

class truncexpon_gen(rv_continuous):
    b: Any = ...
    def _argcheck(self, b: Any): ...
    def _pdf(self, x: Any, b: Any): ...
    def _logpdf(self, x: Any, b: Any): ...
    def _cdf(self, x: Any, b: Any): ...
    def _ppf(self, q: Any, b: Any): ...
    def _munp(self, n: Any, b: Any): ...
    def _entropy(self, b: Any): ...

truncexpon: Any

class truncnorm_gen(rv_continuous):
    a: Any = ...
    b: Any = ...
    _nb: Any = ...
    _na: Any = ...
    _sb: Any = ...
    _sa: Any = ...
    _delta: Any = ...
    _logdelta: Any = ...
    def _argcheck(self, a: Any, b: Any): ...
    def _pdf(self, x: Any, a: Any, b: Any): ...
    def _logpdf(self, x: Any, a: Any, b: Any): ...
    def _cdf(self, x: Any, a: Any, b: Any): ...
    def _ppf(self, q: Any, a: Any, b: Any): ...
    def _stats(self, a: Any, b: Any): ...

truncnorm: Any

class tukeylambda_gen(rv_continuous):
    def _argcheck(self, lam: Any): ...
    def _pdf(self, x: Any, lam: Any): ...
    def _cdf(self, x: Any, lam: Any): ...
    def _ppf(self, q: Any, lam: Any): ...
    def _stats(self, lam: Any): ...
    def _entropy(self, lam: Any): ...

tukeylambda: Any

class FitUniformFixedScaleDataError(FitDataError):
    args: Any = ...
    def __init__(self, ptp: Any, fscale: Any) -> None: ...

class uniform_gen(rv_continuous):
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, q: Any): ...
    def _stats(self): ...
    def _entropy(self): ...
    def fit(self, data: Any, *args: Any, **kwds: Any): ...

uniform: Any

class vonmises_gen(rv_continuous):
    def _rvs(self, kappa: Any): ...
    def _pdf(self, x: Any, kappa: Any): ...
    def _cdf(self, x: Any, kappa: Any): ...
    def _stats_skip(self, kappa: Any): ...
    def _entropy(self, kappa: Any): ...

vonmises: Any
vonmises_line: Any

class wald_gen(invgauss_gen):
    _support_mask: Any = ...
    def _rvs(self): ...
    def _pdf(self, x: Any): ...
    def _logpdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _stats(self): ...

wald: Any

class wrapcauchy_gen(rv_continuous):
    def _argcheck(self, c: Any): ...
    def _pdf(self, x: Any, c: Any): ...
    def _cdf(self, x: Any, c: Any): ...
    def _ppf(self, q: Any, c: Any): ...
    def _entropy(self, c: Any): ...

wrapcauchy: Any

class gennorm_gen(rv_continuous):
    def _pdf(self, x: Any, beta: Any): ...
    def _logpdf(self, x: Any, beta: Any): ...
    def _cdf(self, x: Any, beta: Any): ...
    def _ppf(self, x: Any, beta: Any): ...
    def _sf(self, x: Any, beta: Any): ...
    def _isf(self, x: Any, beta: Any): ...
    def _stats(self, beta: Any): ...
    def _entropy(self, beta: Any): ...

gennorm: Any

class halfgennorm_gen(rv_continuous):
    def _pdf(self, x: Any, beta: Any): ...
    def _logpdf(self, x: Any, beta: Any): ...
    def _cdf(self, x: Any, beta: Any): ...
    def _ppf(self, x: Any, beta: Any): ...
    def _sf(self, x: Any, beta: Any): ...
    def _isf(self, x: Any, beta: Any): ...
    def _entropy(self, beta: Any): ...

halfgennorm: Any

class crystalball_gen(rv_continuous):
    def _pdf(self, x: Any, beta: Any, m: Any): ...
    def _cdf(self, x: Any, beta: Any, m: Any): ...
    def _munp(self, n: Any, beta: Any, m: Any): ...
    def _argcheck(self, beta: Any, m: Any): ...

crystalball: Any

class argus_gen(rv_continuous):
    def _pdf(self, x: Any, chi: Any): ...
    def _cdf(self, x: Any, chi: Any): ...
    def _sf(self, x: Any, chi: Any): ...

argus: Any

class rv_histogram(rv_continuous):
    _support_mask: Any = ...
    _histogram: Any = ...
    _hpdf: Any = ...
    _hbins: Any = ...
    _hbin_widths: Any = ...
    _hcdf: Any = ...
    def __init__(self, histogram: Any, *args: Any, **kwargs: Any) -> None: ...
    def _pdf(self, x: Any): ...
    def _cdf(self, x: Any): ...
    def _ppf(self, x: Any): ...
    def _munp(self, n: Any): ...
    def _entropy(self): ...
    def _updated_ctor_param(self): ...
