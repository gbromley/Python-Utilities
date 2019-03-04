# grabs the specified months similar to JJA type seasonal extractors in xarray
#
import statsmodels.api as sm
import numpy as np
import xarray as xr



def extract_months(month, start, end):
    return (month >= start) & (month <= end)




def mk_test(x, alpha = 0.05):
    import numpy
    from scipy.stats import norm
    """
    Input:
        x:   a vector of data
        alpha: significance level (0.05 default)

    Output:
        trend: tells the trend (increasing, decreasing or no trend)
        h: True (if trend is present) or False (if trend is absence)
        p: p value of the significance test
        z: normalized test statistics

    Examples
    --------
      >>> x = np.random.rand(100)
      >>> trend,h,p,z = mk_test(x,0.05)
    """
    n = len(x)

    # calculate S
    s = 0
    for k in range(n-1):
        for j in range(k+1,n):
            s += numpy.sign(x[j] - x[k])

    # calculate the unique data
    unique_x = numpy.unique(x)
    g = len(unique_x)

    # calculate the var(s)
    if n == g: # there is no tie
        var_s = (n*(n-1)*(2*n+5))/18
    else: # there are some ties in data
        tp = numpy.zeros(unique_x.shape)
        for i in range(len(unique_x)):
            tp[i] = sum(unique_x[i] == x)
        var_s = (n*(n-1)*(2*n+5) + numpy.sum(tp*(tp-1)*(2*tp+5)))/18

    if s>0:
        z = (s - 1)/numpy.sqrt(var_s)
    elif s == 0:
            z = 0
    elif s<0:
        z = (s + 1)/numpy.sqrt(var_s)

    # calculate the p_value
    p = 2*(1-norm.cdf(abs(z))) # two tail test
    h = abs(z) > norm.ppf(1-alpha/2)

    if (z<0) and h:
        trend = 'decreasing'
    elif (z>0) and h:
        trend = 'increasing'
    else:
        trend = 'no trend'

    return trend, h, p, z


def ufunc_calc_trends(time_series):
    #create the y intercept for the ols
    index_array = np.arange(0,len(time_series),1)
    index = sm.add_constant(index_array)

    #create the model
    model = sm.OLS(time_series,index)
    results = model.fit()
    #return the slope
    slope = results.params[1]
    return slope * 10.0

def nc_trend_calc(da):
    # takes calc trend function and applies it over lat lon
    # key is that input_core_dims = 'time' and vectorize = true
    result = xr.apply_ufunc(ufunc_calc_trends, da,
                            input_core_dims=[['year']],
                            dask='parallelized',
                            vectorize=True)
    return result
def ddate_to_datetime(time):
    #taking decimal year (2017.08333) to normal datetime
    # stupid berkley data
    time = time - 1970
    year = time.astype(int)

    rem = time - year
    base = year.astype('datetime64[Y]')
    result = base + np.timedelta64(365,'D')*rem

    return result
