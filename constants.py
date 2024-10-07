# Module defining all used constants

# Define the gravitational constant 
g = 9.81 # m/s^2

# Define gas constant
gam = 1.4
fgam = gam - 1
rgam = fgam/gam

# LCV values
LCV = 42.7 * 1E+06

# Initialises ISA values at sea level
t_sl = 288.15 # K
p_sl = 101325 # Pa
ro_sl = 1.2258 # kg/m^3
a_sl = 340.3 # m/s

# Breguet range equation take-off constant
k = 0.015

# Emissions constant
EIco2 = 3088 # g CO2 / kg
EIh20 = 1237 # g H20 / kg based on https://www.mit.edu/~hamsa/pubs/ICRAT_2014_YSC_HB_final.pdf