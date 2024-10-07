# import modules
import constants as c
import numpy as np

# Define function to calculate propulsive efficiency
# given 
def prop(fpr, mach,etha_f):
    
    p02_p = (1 + 0.5 * c.fgam * mach**2) ** (1/c.rgam)
    mj = np.sqrt(2 * (1/c.fgam) * ((fpr*p02_p) ** c.rgam - 1))
    tj_t = (1 + 0.5 * c.fgam * mach **2) / (1+ 0.5 * c.fgam * mj **2) * fpr ** (c.rgam/etha_f)
    etha_p = 2 * (1 + mj / mach * np.sqrt(tj_t)) ** (-1)
    return etha_p