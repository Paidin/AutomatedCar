# -*- coding: utf-8 -*-
"""
	Skript um Entfernungsmessungen und Motorgeschwindigkeit zu kombinieren
	Änderung der Geschwindigkeit in Abängigkeit des Abstandes zum Hindernis
"""

import time

# Modul als Klasse schreiben ???
import Distance
import MotorFunctions as Motor

# Soll-Distanz in [cm]
maxDistance = 30

# Geschwindigkeit des Autos
speed = 0

Motor.initMotor()
Distance.initPins()
Distance.getDistance()

Motor.maxVelocity = 30
Motor.changeVelocity(int(speed))
input("Press Enter to continue >> ")


try:
	while True:
		# Ermittle Entfernung zum Hindernis
		dist = Distance.getDistance()
		t = time.time()
		time.sleep(0.01)
		
		# Ignoriere ungültige Messungen
		if dist == None:
			continue
		
		# Änderung der Geschwindigkeit
		if dist > maxDistance:
			speed += 5
		if dist < maxDistance:
			speed -= 5
		
		# Neuen Tastgrad als Integer übergeben
		Motor.changeVelocity(int(speed))
					
except:
	print("Ok, something went wrong...")

finally:
	Motor.changeVelocity(int(speed))
Motor.stopMotor()
