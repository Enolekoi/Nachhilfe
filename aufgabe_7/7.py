import numpy as np
import matplotlib.pyplot as plt
from lib import functions

'''
Time axis
''' 
t_start = -6    # Startwert
t_end = 0       # Endwert
num_samples = 2000  # Anzahl an Samples
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
T = 1   # Periodendauer T

amplitude_rect = 3  # Amplitude des Rechtecksignals
argument_rect = -((0.5*t)/T) - 1.5  # Argument des Rechtecksignals
offset_rect = 0     # DC-Offset des Rechtecksignals (=0)
# Definition des Rechtecksignals
rect = amplitude_rect * functions.rect(argument_rect) + offset_rect

amplitude_dreieck = 2   # Amplitude des Dreiecksignals
argument_dreieck = -((1*t)/T) - 3   # Argument des Dreiecksignals
offset_dreieck = 0      # DC-Offset des Dreiecksignals (=0)
# Definition des Dreiecksignals
dreieck = amplitude_dreieck * functions.dreieck(argument_dreieck) + offset_dreieck

# Signal ist Rechtecksignal - Dreiecksignal
x_t = rect - dreieck

'''
Plot 
'''
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x(t) = rect()$', color='blue')
plt.title('Signal $x_1(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
