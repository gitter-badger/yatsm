from __future__ import division

import numpy as np
import statsmodels.api as sm

from regression import robust_fit as rlm

ndays = 365.25


def multitemp_mask(x, Y, n_year, crit=400,
                   green=1, swir1=4,
                   maxiter=10):
    """ Multi-temporal masking using RLM

    Taken directly from CCDC (Zhu and Woodcock, 2014). This "temporal masking"
    procedure was ported from CCDC v9.3.

    Args:
      x (ndarray): array of ordinal dates
      Y (ndarray): matrix of observed spectra
      n_year (float): "number of years to mask"
      crit (float, optional): critical value for masking clouds/shadows
      green (int, optional): 0 indexed value for green band in Y (default: 1)
      swir1 (int, optional): 0 indexed value for SWIR (~1.55-1.75um) band in Y
        (default: 4)
      maxiter (int, optional): maximum iterations for RLM fit

    Returns:
      mask (ndarray): mask where False indicates values to be masked

    """
    green = Y.take(green, axis=0)
    swir1 = Y.take(swir1, axis=0)

    n_year = np.ceil(n_year)
    w = 2.0 * np.pi / ndays

    X = np.column_stack((np.ones_like(x),
                         np.cos(w * x),
                         np.sin(w * x),
                         np.cos(w / n_year * x),
                         np.sin(w / n_year * x)))

    green_RLM = rlm.RLM(M=rlm.bisquare, maxiter=maxiter).fit(X, green)
    swir1_RLM = rlm.RLM(M=rlm.bisquare, maxiter=maxiter).fit(X, swir1)

    mask = ((green - green_RLM.predict(X) < crit) *
            (swir1 - swir1_RLM.predict(X) > -crit))

    return mask


def smooth_mask(x, Y, span, crit=400, green=1, swir1=4,
                maxiter=5):
    """ Multi-temporal masking using LOWESS

    Taken directly from newer version of CCDC than Zhu and Woodcock, 2014. This
    "temporal masking" replaced the older method which used robust linear
    models. This version uses a regular LOWESS instead of robust LOWESS

    Note:   "span" argument is the inverse of "frac" from statsmodels and is
            actually 'k' in their code:

        `n = x.shape[0]`
        `k = int(frac * n + 1e-10)`

    Args:
      x (ndarray): array of ordinal dates
      Y (ndarray): matrix of observed spectra
      span (int): span of LOWESS
      crit (float, optional): critical value for masking clouds/shadows
      green (int, optional): 0 indexed value for green band in Y (default: 1)
      swir1 (int, optional): 0 indexed value for SWIR (~1.55-1.75um) band in Y
        (default: 4)
      maxiter (int, optional): maximum increases to span when checking for
        NaN in LOWESS results

    Returns:
      mask (ndarray): mask where False indicates values to be masked

    #TODO - We need to put the data on a regular period since span changes as
            is right now. Statsmodels will only allow for dropna, so we would
            need to impute missing data somehow...

    """
    # Reverse span to get frac
    frac = span / x.shape[0]
    # Estimate delta as "good choice": delta = 0.01 * range(exog)
    delta = (x.max() - x.min()) * 0.01

    # Run LOWESS checking for NaN in output
    i = 0
    green_lowess, swir1_lowess = np.nan, np.nan
    while (np.any(np.isnan(green_lowess)) or
           np.any(np.isnan(swir1_lowess))) and i < maxiter:
        green_lowess = sm.nonparametric.lowess(Y[green, :], x,
                                               frac=frac, delta=delta)
        swir1_lowess = sm.nonparametric.lowess(Y[swir1, :], x,
                                               frac=frac, delta=delta)
        span += 1
        frac = span / x.shape[0]
        i += 1

    mask = (((Y[green, :] - green_lowess[:, 1]) < crit) *
            ((Y[swir1, :] - swir1_lowess[:, 1]) > -crit))

#    train_plot_debug(x, Y, mask, swir1_lowess)
#    train_plot_debug(x, Y, mask, green_lowess, band=1)
    return mask


def train_plot_debug(x, Y, mask, fit, band=4):
    """ Training / historical period multitemporal cloud masking debug """
    import matplotlib.pyplot as plt

    clear = np.where(mask == 1)[0]
    cloud = np.where(mask == 0)[0]

    plt.plot(x[clear], Y[band, clear], 'ko', ls='')
    plt.plot(x[cloud], Y[band, cloud], 'rx', ls='')
    plt.plot(fit[:, 0], fit[:, 1], 'b-')
    plt.show()
