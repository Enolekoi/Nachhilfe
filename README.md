# Signalverarbeitung Nachhilfe Python-Skripte
In diesem Repository sind die Skripte für die Aufgaben 6-8 (8.4 fehlt).

# Installation
Um die Skripte ausführen zu können benötigst du Python3, Numpy und Matplotlib.
Numpy stellt viele Funktionen, die Matlab ähneln zur Verfügung und Matplotlib ist eine Bibliothek, die es ermöglicht, Plots zu erstellen.

## Python 3 unter Windows installieren

1. **Python herunterladen**:
   - Gehe zur offiziellen Python-Website: [python.org](https://www.python.org/).
   - Klicke auf den Button **"Downloads"**. Die Website erkennt automatisch dein Betriebssystem und schlägt die neueste Python-Version vor.
   - Lade das Installationsprogramm für Python 3.x herunter (z. B. Python 3.11).

2. **Python installieren**:
   - Öffne das heruntergeladene Installationsprogramm.
   - Stelle sicher, dass du das Kontrollkästchen **"Add Python to PATH"** aktivierst. Dies ist wichtig, um Python von der Kommandozeile aus ausführen zu können.
   - Klicke auf **"Install Now"**, um Python zu installieren.

3. **Installation überprüfen**:
   - Öffne die **Eingabeaufforderung** (Windows-Taste + R, gib `cmd` ein und drücke Enter).
   - Gib den folgenden Befehl ein:
     ```bash
     python --version
     ```
   - Wenn die Installation erfolgreich war, wird die Python-Version angezeigt (z. B. `Python 3.11.0`).

---

## Schritt 2: NumPy und Matplotlib installieren

Python enthält ein Paketverwaltungstool namens **pip**, mit dem du Pakete wie NumPy und Matplotlib installieren kannst.

1. **Öffne die Eingabeaufforderung**:
   - Drücke `Windows-Taste + R`, gib `cmd` ein und drücke Enter.

2. **Installiere NumPy**:
   - Gib den folgenden Befehl ein:
     ```bash
     pip install numpy
     ```
   - Warte, bis die Installation abgeschlossen ist.

3. **Installiere Matplotlib**:
   - Gib den folgenden Befehl ein:
     ```bash
     pip install matplotlib
     ```
   - Warte, bis die Installation abgeschlossen ist.

4. **Installation überprüfen**:
   - Um zu überprüfen, ob die Pakete erfolgreich installiert wurden, kannst du den folgenden Befehl in der Eingabeaufforderung ausführen:
     ```bash
     python -c "import numpy; import matplotlib; print('Installation erfolgreich!')"
     ```
   - Wenn keine Fehlermeldung angezeigt wird, sind die Pakete korrekt installiert.
---

# Ausführung der Skripte

Um die Skripte auszuführen, lade zunächst dieses Repository herunter.
Öffne eine Kommandozeile in dem Verzeichniss und führe für das Ausführen der Skripe einen Befehl nach folgenden Beispielen aus:
- Für Aufgabe 6.1
    ```
    python -m aufgabe_6.6_1 
    ```
- Für Aufgabe 8.3
    ```
    python -m aufgabe_8.8_3 
    ```

# Benutzerdefinierte Signalverarbeitungsfunktionen

Die Definition der Signalverarbeitungsfunktionen (z.B. rect, si, sign) befinden sich in `lib/functions.py`
