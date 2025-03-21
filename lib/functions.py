import numpy as np

'''
Implementierung von wichtigen Funktionen der Signalverarbeitung
'''

'''
rect(x)
    Implementierung eines Rechtecksignals
Inputs:
    x -> [numpy Array] Zeitachse
Outputs:
    Rechtecksignal
'''
def rect(x):
    # Werte zwischen -1 und 1 werden 1 alle übrigen 0
    return np.where(np.abs(x) < 1, 1, np.where(np.abs(x) == 1, 0.5, 0))

'''
si(x)
    Implementierung der Si-Funktion (sin(x)/x)
Inputs:
    x -> [numpy Array] Zeitachse
Outputs:
    Si-Funktion
'''
def si(x):
    # Alle Funktionswerte sind sin(x)/x, außer für x=0 -> 1
    return np.where(x == 0, 1.0, np.sin(x)/x)

'''
u(x)
    Implementierung des Einheitssprunges
Inputs:
    x -> [numpy Array] Zeitachse
Outputs:
    Einheitssprung
'''
def u(x):
    # Alle negativen Funktionswerte werden 0, bei x=0 -> 0.5 und bei x>0 -> 1
    return np.where(x < 0, 0, np.where(x == 0, 0.5, 1))

'''
dreieck(x)
    Implementierung eines Dreiecksignals
Inputs:
    x -> [numpy Array] Zeitachse
Outputs:
    Dreiecksignal
'''
def dreieck(x):
    # Alle x-Werte |x| > 1 -> 0, anstieg von 0 auf 1 im Bereich [-1, 0], abfall von 1 auf 0 im Bereich [0, 1]
    return np.where(np.abs(x) <= 1, 1 - np.abs(x), 0)

'''
sign(x)
    Implementierung der Signum-Funktion (Vorzeichenwechsel)
Inputs:
    x -> [numpy Array] Zeitachse
Outputs:
    Signum-Funktion
'''
def sign(x):
    # Alle Werte für x < 0 werden mit -1 multipliziert
    return np.where(x < 0, -1, np.where(x == 0, 0, 1))
