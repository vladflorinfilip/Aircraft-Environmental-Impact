# Import modules
import numpy as np
import constants as c

# This function takes a given altitude and returns the expected temperature and 
# pressure and density using the ISA model 
def isa(h):

    # Find location based on altitude
    if h > 11000 :
        location = 'stratosphere'
    else:
        location = 'troposphere'

    if location == 'troposphere' :
        # Calculates temperature
        t = c.t_sl - 6.5 * h * 1E-03

        # Calculates pressure
        p = c.p_sl * (t/c.t_sl) ** 5.256

        # Calculates density
        ro = c.ro_sl * (t/c.t_sl) ** 4.256

        # Calculates speed of sound
        a = c.a_sl * (t/c.t_sl) ** 0.5

    elif location == 'stratosphere':
        # Calculates temperature
        t = 216.65 # K
        p_t = c.p_sl * (t/c.t_sl) ** 5.256
        ro_t = c.ro_sl * (t/c.t_sl) ** 4.256

        # Calculates pressure
        p = p_t * np.exp(-0.1577*(h * 1E-03 - 11))

        # Calculates density
        ro = ro_t * np.exp(-0.1577*(h * 1E-03 - 11))

        # Calculates speed of sound
        a = c.a_sl * (t/c.t_sl) ** 0.5

    return t, p, ro, a
        