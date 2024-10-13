import pandas as pd
from lightkurve import LightCurve
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
df = pd.read_csv('exo_test2/norm/Sec31_cam4_ccd3_cut3_object1987_norm_good.csv')


# Extract time and flux data
time = df['mjd']
flux = df['counts']

# Create a LightCurve object
lc = LightCurve(time=time, flux=flux)

# Fit the light curve (example: using a simple polynomial fit)
lc.plot()
#plt.show()

print()


period = np.linspace(1, 40, 20000)
# Create a BLSPeriodogram
bls = lc.to_periodogram(method='bls', period=period, frequency_factor=500);
bls.plot()

plt.show()

planet_b_period = bls.period_at_max_power
planet_b_t0 = bls.transit_time_at_max_power
planet_b_dur = bls.duration_at_max_power
#
# # Check the value for period
# planet_b_period

ax = lc.fold(period=planet_b_period, epoch_time=planet_b_t0).scatter()
ax.set_xlim(-10, 10)

# Create a cadence mask using the BLS parameters
planet_b_mask = bls.get_transit_mask(period=planet_b_period,
                                     transit_time=planet_b_t0,
                                     duration=planet_b_dur)

# Create a BLS model using the BLS parameters
planet_b_model = bls.get_transit_model(period=planet_b_period,
                                       transit_time=planet_b_t0,
                                       duration=planet_b_dur)

ax = lc.fold(planet_b_period, planet_b_t0).scatter()
planet_b_model.fold(planet_b_period, planet_b_t0).plot(ax=ax, c='r', lw=2)
ax.set_xlim(-5, 5)

### A problem with variable names copied from the tutorial

# period = np.linspace(1, 300, 10000)
# bls = planet_b_mask.to_periodogram('bls', period=period, frequency_factor=500)
# bls.plot()
#
# planet_c_period = bls.period_at_max_power
# planet_c_t0 = bls.transit_time_at_max_power
# planet_c_dur = bls.duration_at_max_power
#
# planet_c_model = bls.get_transit_model(period=planet_c_period,
#
# ax = lc.scatter();
# planet_b_model.plot(ax=ax, c='dodgerblue', label='Planet b Transit Model');
# planet_c_model.plot(ax=ax, c='r', label='Planet c Transit Model');



# Check the value for period
# planet_c_period



plt.show()
print()





#lc.flatten(window_length=101).plot()
