# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import planes as p
from engine import eng
from stage import stage
from emissions import emissions

# Define main loop

##############################################################################
def main():
    
    # Range
    s = 12000 # km
    s_lb = 2090.31 # km to Bucharest
    s_lbog = 8457.5 # km to Bogota

    # Calculate emissions at different altitudes 
    altitudes = [6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000] # m
    ratios = [10,15,20,25,30,35,40,45,50] # OPR

    # Vectors to store emissions
    fuelpr_v = np.zeros(len(altitudes))
    co2_v = np.zeros(len(altitudes))
    nox_v = np.zeros(len(altitudes))
    h2o_v = np.zeros(len(altitudes))
    mach1 = np.zeros(len(altitudes))
    co2_vv = np.zeros(10)
    nox_vv = np.zeros(10)
    fuelpr_r = np.zeros((len(altitudes)+1,len(ratios)))
    co2_r = np.zeros((len(altitudes),len(ratios)))
    nox_r = np.zeros((len(altitudes),len(ratios)))
    h2o_r = np.zeros((len(altitudes),len(ratios)))
    eff_r = np.zeros((len(altitudes),len(ratios)))

    # Store data in dictionary
    _data  = []

    i = 0
    for h in altitudes: 
        j = 0
        for r in ratios: 
            plane1 = p.Boeing_787_8()
            plane1.r = r
            plane1.etha_cycle = eng(plane1.theta,plane1.r,plane1.etha_c,plane1.etha_t)
            plane1.h = h


            # Iterate calculations for n stages MAIN LOOP
            n = 10
            s_stage = s/n
            for k in range(n):
                stage(plane1,s_stage)

         # Calculate emissions and store them in vectors (emissions per payload-range)
            fuelpr, co2, nox, h2o = emissions(plane1,s)
            fuelpr_r[i][j] = fuelpr
            co2_r[i][j] = co2
            nox_r[i][j] = nox
            h2o_r[i][j] = h2o
            eff_r[i][j] = plane1.etha_cycle
            j = j + 1


            _data.append([h/1000, co2, nox, h2o])
        i = i + 1


    # Plot Emissions with altitude FIG. 2a
    #_df = pd.DataFrame(_data, columns=["Altitude [km]", "CO2", "NOx", "H2O"])

    #_df.plot(x="Altitude [km]", y=[ "CO2", "NOx", "H2O"], kind="bar",figsize=(8,4))
    altitudes = [x//1000 for x in altitudes]

    #COLOR_T = "maroon"
    #COLOR_P = "navy"


    #fig, ax1 = plt.subplots(figsize=(8, 8))
    #ax2 = ax1.twinx()

    #ax1.plot(altitudes, co2_v, '-o', color=COLOR_T)
    #ax2.plot(altitudes, nox_v, '-o', color=COLOR_P)

    #ax1.set_xlabel("Altitude [km]", fontsize=14)
    #ax1.set_ylabel("CO2 [g/(passenger-km)]", color=COLOR_T, fontsize=14)
    #ax1.tick_params(axis="y", labelcolor=COLOR_T)

    #ax2.set_ylabel("NOx [g/(passenger-km)]", color=COLOR_P, fontsize=14)
    #ax2.tick_params(axis="y", labelcolor=COLOR_P)

    #fig.autofmt_xdate()

    # Plot Fuel Burn FIG. 1b
    #plt.barh(altitudes,fuelpr_v,color = 'navy')
    #plt.xlabel('Fuel [kg/passenger-km]')
    #plt.xlim(0.03,0.045)
    #plt.ylabel('Altitude [km]')

    # Plot velocity ratio with mach FIG. 1a
    #plt.plot(mach1,altitudes,color = 'slategrey', label = 'v = 0.8')
    #plt.plot(mach2,altitudes,color = 'dimgray', label = 'v = 1')
    #plt.plot(mach3,altitudes,color = 'black', label = 'v = 1.2')
    #plt.plot([0.85,0.85],[6,13],'--',color = 'red', label = 'Transonic limit')
    #plt.grid()
    #plt.ylim(6,13)
    #plt.xlim(0.4,1.0)
    #plt.xlabel('Mach')
    #plt.ylabel('Altitude [km]')
    #plt.legend()

    # Iterate calculations for n stages MAIN LOOP
    #for j in range(10):
        # London to Bucharest step altitude flight
    #    plane1 = p.Boeing_787_8()
    #    plane1.etha_cycle = eng(plane1.theta,plane1.r,plane1.etha_c,plane1.etha_t)
    #    plane1.h = 9000 # km Initial 
    #    plane1.miu = 0.95

    #    for i in range(10):
    #        s_stage = s_lbog/n
    #        stage(plane1,s_stage)
    #        if j > i: 
    #            plane1.h = plane1.h + 304.8

        # Calculate emissions and store them in vectors (emissions per payload-range)
        #fuelpr, co2, nox, h2o = emissions(plane1,s_lbog)
        #print(fuelpr, co2, nox, h2o)
        #co2_vv[j] = co2
        #nox_vv[j] = nox
    


    COLOR_T = "crimson"
    COLOR_P = "darkolivegreen"


    #fig, ax1 = plt.subplots(figsize=(8, 8))
    #ax2 = ax1.twinx()
    #plt.rcParams.update({'font.size': 20})
    #name = ['B787-8 stepping', 'A320 stepping', 'A320 constant']
    #X_axis = np.arange(10)
    #ax1.plot(ratios, eff_r, '-o', color=COLOR_T)
    #ax2.plot(ratios, nox_r, '-x', color=COLOR_P)

   # ax1.set_xlabel("Overall Pressure Ratio", fontsize=20)
    #ax1.set_ylabel("Cycle Efficiency", color=COLOR_T, fontsize=20)
   # ax1.tick_params(axis="y", labelcolor=COLOR_T)

   # ax2.set_ylabel("NOx [g/(passenger-km)]", color=COLOR_P, fontsize=20)
   # ax2.tick_params(axis="y", labelcolor=COLOR_P)
    #ax2.set_ylim(0,4)

    #fig.autofmt_xdate()
    for i in range(len(altitudes)):
        plt.plot(ratios,nox_r[i],'-o',label = '{} km'.format(altitudes[i]))
    # Plot barchart for GWP NOx and CO2 FIG. 2b
    plt.legend()
    plt.grid()
    plt.xlabel('OPR')
    plt.ylabel('NOx [g/(passenger-km)]')
    plt.show()

###############################################################################

main()