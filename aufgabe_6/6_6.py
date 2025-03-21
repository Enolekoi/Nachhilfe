import numpy as np
import matplotlib.pyplot as plt
from lib import functions

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
A = 2   # Signalamplitude
omega0 = 2*np.pi * 0.2  # Frequenz \omega_0
argument = 1j * omega0 * t  # Argument der Exponentialfunktion

x_t = A * np.exp(argument)

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x_6(t) = e^{j*\omega_0 * t}$', color='blue')
plt.title('Signal $x_6(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
