import numpy

def f_to_c(tf):
    return(5.0/9.0*(tf-32))
#tc: temp in celsius
def sat_vap_pres(tc):
    return(10.0*0.611*numpy.power(10,((7.5*tc)/(237.3+tc))))

# tdc: dewpoint temp in celsius tc: temp in celsius
def rel_hum(tc, tdc):
    e = 6.11*10.0**(7.5*tdc/(237.7+tdc))
    es = (6.11*10.0**(7.5*tc/(237.7+tc)))
    return(100.0*e/es)

# ea: vapor pressure es: sat. vapor pressure
def vpd(ea,es):
    return (ea - es)
