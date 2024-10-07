# import
import constants as c
import numpy as np
from isa import isa

def emissions(P,s):

    # Passager number
    pas = P.pas

    # Calculate burnt fuel kg per payload-km [kg/kgkm]
    fuelpr = P.m_fuel / (s * P.w_p) 
    
    # Calculate CO2 emissions
    co2 = fuelpr * c.EIco2 * pas

    # Calculate NOx emissions
    t, p, ro, a = isa(P.h)
    print(P.h)
    print(P.mach)
    t02 = t * (1 + 0.5 * c.fgam * P.mach **2)
    t03 = t02 * (1 + (P.r ** c.rgam - 1)/P.etha_c)
    EInox = 0.011445 * np.exp(0.00676593 * t03)
    print()
    nox = fuelpr * EInox * 2 * 15.1 * pas

    # Calculate water emissions
    h2o = fuelpr * c.EIh20 * pas

    # Update fuelpr to be per passenger-km
    fuelpr = fuelpr * pas

    return fuelpr, co2, nox, h2o
