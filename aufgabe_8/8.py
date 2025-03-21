import numpy as np
import matplotlib.pyplot as plt
from lib import functions

'''
Funktion zum Erstellen des Ursprungssignals x
'''
def x(argument):
    # Zeitachse wird um 0.5 nach rechts verschoben
    t = argument - 0.5
    
    # Das Signal wird zunächst so definiert, dass die Linke hälfte des Signals nach oben gespiegelt wird. 
    # Das Zentrum des Signals wird als negatives Dreieck mit doppelter Frequenz aufgefasst
    center = - functions.dreieck(2*t)
    # Das breitere Teilsignal links und rechts wird durch ein verschobenes halbiertes Dreieck definiert.
    negativ = functions.dreieck(-t-0.5) * functions.u(-t+0.5)
    positiv = functions.dreieck(t-0.5) * functions.u(t+0.5)
    
    # Summe der Teilsignale
    temp = center + negativ + positiv
    
    # Multiplikation mit Signumfunktion führt zu einer Spiegelung der linken Hälfte des Signals nach unten.
    # Um das Signal vor der Spiegelung zu sehen, kommentiere die folgende Zeile aus und die darauffolgende ein
    signal = temp * functions.sign(t)
    # signal = temp
    return signal

'''
Time axis
'''
t_start = -5    # Startwert 
t_end = 5       # Endwert
num_samples = 2000
t = np.linspace(t_start, t_end, num_samples)

'''
Signal
'''
x_t = x(t)

# Plot 
plt.figure(figsize=(10,6))
plt.plot(t, x_t, label=r'$x(t) = rect()$', color='blue')
plt.title('Signal $x_1(t)$')
plt.xlabel('Zeit $t$ [ms]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
