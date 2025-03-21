import numpy as np
import matplotlib.pyplot as plt
from lib import functions

'''
Time axis
'''
t_start = 0     # Startwert
t_end = 10      # Endwert
num_samples = 2000  # Anzahl an Samples
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
T = 3   # Periodendauer T
argument = ((2*t)/T) - 5    # Argument des Rechtecks
x_t = functions.rect(argument)

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x_1(t) = rect()$', color='blue')
plt.title('Signal $x_1(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
