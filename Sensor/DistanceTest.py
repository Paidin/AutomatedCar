# -*- coding: utf-8 -*-
"""
Basierend auf Sensor/Distance.py, kann mit diesem Skript eine Messreihe über 30 Messungen
angelegt werden, wobei die Messdaten des HC-SR04 Sensors in einer Datei gespeichert werden.
So können sie später besser analysiert werden.
"""

from Distance import *

import time
import statistics as stat

# Initialisiere einige Variabeln
tgtDistance = int(input("Soll-Abstand zum Hindernis [cm] >> "))
height = float(input("Höhe des Sensors [cm] >>"))
addition = str(input("Dateinamenszusatz >> "))
Log = open("Messung-" + str(tgtDistance) + "-" + addition, "wt")
print("Sensorhoehe: " + str(height) + " cm", file=Log)
print("Soll-Abstand: " + str(tgtDistance) + " cm", file=Log)
print("Messdaten [cm]: ", file=Log)

# Initialisiere Pins und führe eine erste Messung durch
# erste Messung erhält nie eine brauchbare Antwort des Sensors
initPins()
getDistance()
# Nach 25.08.17 eigentlich nicht nötig, da Timeouts ignoriert => return None

# Führe die Messreihe aus
data = []
timeouts = 0
for i in range(0, 30):
    distance = getDistance()
    # Wenn kein timeout erfolgte, benutze dieses Messergebnis
    if distance != None:
        # print("%.4f" % distance)
        print("%.4f" % distance, file=Log)
        data.append(distance)
    # Stelle sicher, dass 30 Werte in der Messreihe sind
    else:
        i -= 1
        timeouts += 1
    time.sleep(1)
    
# Beende die Messungen
print("Timeouts: " + str(timeouts), file=Log)
clearPins()
Log.close()

# Gebe eine kurze Zusammenfassung der Messreihe auf dem Bildschirm aus
median = stat.median(data)
offset = median - tgtDistance
print("\n===========================================")
print("Zusammenfassung der Messdaten\n")
print("Sensorhöhe [cm]:", height)
print("Soll-Abstand [cm]:", tgtDistance)
print("Anzahl Timeouts: ", timeouts)
print("Median der Messreihe [cm]:", median)
print("Abweichung vom Soll [cm]:", offset)
print("Abweichung vom Soll  [%]:", offset/tgtDistance*100)
print("===========================================")
    

    
