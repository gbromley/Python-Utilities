# grabs the specified months similar to JJA type seasonal extractors in xarray
#
def extract_months(month, start, end):
    return (month >= start) & (month <= end)
