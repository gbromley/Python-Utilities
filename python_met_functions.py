import numpy

def f_to_c(tf):
    return(5.0/9.0*(tf-32)) 

def sat_vap_pres(tc):
    return(0.611*numpy.exp((17.27*tc/(237.3+tc))))

def rel_hum(tc, tdc):
    e = 6.11*10.0**(7.5*tdc/(237.7+tdc))
    es = (6.11*10.0**(7.5*tc/(237.7+tc)))
    return(100.0*e/es)

def vpd(ea,es):
    return (ea - es)