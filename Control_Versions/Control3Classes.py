#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Skript zur Anpassung der Geschwindigkeit des Motors in Abhängigkeit
    zur Entfernung des vorausfahrenden Fahrzeuges
"""

import time
import Sensor
import Motor


# Ziel-Entfernung, die eingehalten werden soll
tgtDistance = 30 

# Aktuelle Geschwindigkeit, ausserhalb der Klasse gespeichert
speed = 0

# Initialisiere Ultraschallsensor
sensor = Sensor.Sensor()
sensor.getDistance()

# Initialisiere Motor mit maximalem Tastgrad von 30%
motor = Motor.Motor(30)
motor.changeSpeed(int(0))


try:
    while True:
        # Ermittle Entfernung zum Hindernis
        dist = sensor.getDistance()
        time.sleep(0.01)
        
        # Ignoriere ungültige Messungen
        if dist is None:
            continue
        
        # Änderung der Geschwindigkeit
        if dist > tgtDistance:
            motor.changeSpeed(int(5))
        if dist < tgtDistance:
            motor.changeSpeed(int(-5))
        
        pass
    
except:
    print("Ok, something went wrong...")
    print("or someone pressed ^C")
    
finally:
    motor.stop()
        



