# import modules
import constants as c

# This function takes
# theta = turbine temperature ration
# r = compressor pressure ratio
# etha_c and etha_t  compressor and turbine efficiencies
def eng(theta,r,etha_c,etha_t):

    # Check theta, r and etha_c/etha_t
    if theta > 6: 
        print('ERROR: Turbine temperature ratio too high, risk of blades failing')
        exit()
    if r > 50:
        print("ERROR: Risk of compressor separation")
        exit()
    if etha_c > 0.92 or etha_t > 0.92:
        print('ERROR: Efficiencies are limited by leakages, tip clearance, 3D flow, boundary layers')
        exit()
    
    # Non-dimensional net work
    w_net = theta * etha_t * (1 - 1/r**c.rgam) - (r**c.rgam - 1) / etha_c

    # Non-dimensional heat in
    q = theta - 1 - (r**c.rgam - 1) / etha_c

    # Calculate efficiency
    etha_cycle = w_net/q

    return etha_cycle