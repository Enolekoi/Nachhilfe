import numpy as np
import matplotlib.pyplot as plt

'''
Time axis
'''
t_start = -10   # Startwert
t_end = 10      # Endwert
num_samples = 2000  # Anzahl an Samples
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
# Definition von Periodenfrequenzen \Omega_1 und \Omega_2
Omega1 = (2 * np.pi) / 5
Omega2 = (2 * np.pi) / 10
# Definition des Signals
x_t = np.cos(Omega1 * t) + np.cos(Omega2 * t)

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x_2(t) = \cos(\Omega_1 t) + \cos(\Omega_2 t)$', color='blue')
plt.title('Signal $x_2(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
