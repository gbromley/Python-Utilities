
# coding: utf-8

# In[ ]:

def f_to_c(tf):
    return(5.0/9.0*(tf-32)) 

def sat_vap_pres(tc):
    return(0.611*np.exp((17.27*tc/(237.3+tc)))

def rel_hum(tc, tcd):
    e = 6.11*10.0**(7.5*tdc/(237.7+tdc))
    es = (6.11*10.0**(7.5*tc/(237.7+tc)))
    return(100.0*e/es)

