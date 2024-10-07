# import modules
import numpy as np
import constants as c
from isa import isa
from prop import prop

def stage(P,s_stage):

    # 1. Find current wing loading
    w_load = P.m * c.g / P.S

    # 2. Calculate optimum EAS for maximum lift-to-drag
    eas_opt = (2*w_load/c.ro_sl) ** 0.5 * (P.K2/P.K1) ** 0.25

    # 3. Calculate actual EAS from selected velocity ratio
    eas = eas_opt * P.miu

    # 4.1. Calculate flow conditions at new altitude
    t, p, ro, a = isa(P.h)

    # 4.2. Calculate TAS and Mach 
    tas = eas * np.sqrt(c.ro_sl / ro)
    mach = tas/a
    P.mach = mach

    # 4.3. Check if Mach is below transonic limit
    if mach > 0.85: 
        print('WARNING: Mach above transonic limit')
    
    # 5.1. Calculate engine propulsive efficiency 
    P.etha_prop = prop(P.fpr,mach,P.etha_f)

    # 5.2. Calculate lift-to-drag
    beta_opt = 2 * np.sqrt(P.K1*P.K2)
    beta = 0.5 * beta_opt * (P.miu**2 + 1/(P.miu**2)) # beta = inverse of L/D

    # 5.3. Determine range parameter
    H = P.etha_prop * P.etha_cycle * P.etha_tr * (1/beta) * c.LCV/c.g
    H = H * 1E-3 # convert to km

    # 5.4. Calculate fuel burn for current stage
    if P.take_off == True: 
        w_end = P.m * (np.exp(-s_stage/H) - c.k)
        P.take_off = False
    else:
        w_end = P.m * np.exp(-s_stage/H)    

    # 5.5. Check fuel required has not supassed fuel capacity
    P.m_fuel = P.m_fuel + P.m - w_end
    P.m = w_end
    if P.m_fuel > P.w_mf: 
        print('WARNING: Fuel ran out')