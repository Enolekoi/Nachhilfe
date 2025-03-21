import numpy as np
import matplotlib.pyplot as plt
from lib import functions

'''
Time axis
'''
t_start = -5    # Startwert
t_end = 5       # Endwert
num_samples = 2000  # Anzahl an Samples
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
argument = 5*t - 3 # argument der Si-Funktion
x_t = functions.si(argument)

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x_4(t) = si(5*t -3)$', color='blue')
plt.title('Signal $x_4(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
