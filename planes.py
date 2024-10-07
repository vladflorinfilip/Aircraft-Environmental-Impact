class Boeing_787_8:

    # Define plane weights and wing area
    w_mto = 220 * 1E3 # kg
    w_mf = 74 * 1E3 # kg
    w_e = 106 * 1E3 # kg
    w_p = 40 * 1E3 # kg
    S = 315 # m^2

    # Define value to store current airplane mass
    m = w_mf + w_e + w_p

    # Value to store if plane takes of
    take_off = True

    # Define value to store current flight height
    # initial
    h = 9500 # m

    # Define vparameter to store Mach
    mach = 0.0

    # Define EAS ratio for actual over optimal
    miu = 0.8

    # L/D constants
    K1 = 0.0125
    K2 = 0.0446

    # Engine parameters
    r = 45
    theta = 6
    etha_c = 0.9
    etha_t = 0.9
    fpr = 1.45
    etha_f = 0.92
    etha_tr = 0.9

    # Fan Pressure Ratio
    fpr = 1.45

    # Define paramater to hold cycle and propulsive efficiencies
    etha_cycle = 0
    etha_prop = 0

    # Define parameter to store burnt fuel value
    m_fuel = 0

    # Passengers
    pas = 240

class Airbus_320:

    # Define plane weights and wing area
    w_mto = 74 * 1E3 # kg
    w_mf = 12 * 1E3 # kg
    w_e =  45 * 1E3 # kg
    w_p = 17 * 1E3 # kg
    S = 315 # m^2

    # Define value to store current airplane mass
    m = w_mf + w_e + w_p

    # Value to store if plane takes of
    take_off = True

    # Define value to store current flight height
    # initial
    h = 9500 # m

    # Define vparameter to store Mach
    mach = 0.0

    # Define EAS ratio for actual over optimal
    miu = 0.8

    # L/D constants
    K1 = 0.0125
    K2 = 0.0446

    # Engine parameters
    r = 45
    theta = 6
    etha_c = 0.9
    etha_t = 0.9
    fpr = 1.45
    etha_f = 0.92
    etha_tr = 0.9

    # Fan Pressure Ratio
    fpr = 1.45

    # Define paramater to hold cycle and propulsive efficiencies
    etha_cycle = 0
    etha_prop = 0

    # Define parameter to store burnt fuel value
    m_fuel = 0

    # Passengers
    pas = 150
