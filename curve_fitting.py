import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# plt.ion()
# %matplotlib inline

g1_norm = np.array([0.02919, 0.02671, 0.02739, 0.02729, 0.02962, 0.0315, 0.03654,0.03917,0.04514,0.05226,0.06055,
              0.07148,0.0818,0.0955,0.11099,0.12653,0.14125,0.1584,0.17856,0.19556,0.21209,0.23527,0.26115,
              0.28318,0.30599,0.32903,0.34887,0.37841,0.40406,0.43396,0.46243,0.49468,0.51494,0.53984,0.57029,
              0.58986,0.62005,0.65019,0.67662,0.71411,0.74319,0.76037,0.793,0.82787,0.86618,0.89554,0.94215,
              0.9589,0.98553,1])
g1_real = np.array([8.07E-09,7.38E-09,7.57E-09,7.54E-09,8.19E-09,8.70E-09,1.01E-08,1.08E-08,1.25E-08,1.44E-08,
               1.67E-08,1.98E-08,2.26E-08,2.64E-08,3.07E-08,3.50E-08,3.90E-08,4.38E-08,4.93E-08,5.40E-08,
               5.86E-08,6.50E-08,7.22E-08,7.82E-08,8.46E-08,9.09E-08,9.64E-08,1.05E-07,1.12E-07,1.20E-07,
               1.28E-07,1.37E-07,1.42E-07,1.49E-07,1.58E-07,1.63E-07,1.71E-07,1.80E-07,1.87E-07,1.97E-07,
               2.05E-07,2.10E-07,2.19E-07,2.29E-07,2.39E-07,2.47E-07,2.60E-07,2.65E-07,2.72E-07,2.76E-07,])

g_max = g1_real.max()
w1 = g1_real/g_max

MAXIMUM_ALLOWED_PULSES = 5

delta_w = []
for N_window in range(MAXIMUM_ALLOWED_PULSES):
    w_tmp = []
    for i in range(50-N_window):
        w_tmp.append(w1[i+N_window]-w1[i])
    xx = np.average(np.asarray(w_tmp))
    delta_w.append(xx)

delta_w = np.asarray(delta_w)
print(np.flip(delta_w))

neuron_spike_cycle = N_window * 1000e-6

time = np.arange(1,N_window+2)*neuron_spike_cycle

# define fitting function
def func_pot(t, g, tau):
    w = g * np.exp(- t/ tau)
    return w


#plot the experimental results
plt.figure(1, figsize=(8,6))
plt.plot(time, np.flip(delta_w), label='Potentiation')

popt, pcov = curve_fit(func_pot, time, np.flip(delta_w), bounds=(0, [0.15, 0.02]))
print(popt)

plt.plot(time, func_pot(time, *popt), 'r-')

plt.legend()
plt.show()