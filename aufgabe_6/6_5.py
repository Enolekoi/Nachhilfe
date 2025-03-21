import numpy as np
import matplotlib.pyplot as plt
from lib import functions

'''
Time axis
'''
t_start = -2
t_end = 0
num_samples = 2000
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
T = 0.1
# Definition von Periodenfrequenzen \Omega = (2*pi / T)
Omega = (2*np.pi)/T
# Argument des Einheitssprungs
argument_u = -t - 2*T
# Argument der SI-Funktion
argument_si = Omega*t

# Definition des Signals
# x_t = functions.u(argument_u)
# x_t = functions.si(argument_si)
x_t = functions.u(argument_u) * functions.si(argument_si)

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x_5(t) = u(-t -2T) * si(\Omega t)$', color='blue')
plt.title('Signal $x_5(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
