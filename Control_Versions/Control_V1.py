"""
	Skript um Entfernungsmessungen und Motorgeschwindigkeit zu kombinieren
	in Abhängigkeit der relativen Geschwindigkeit zum vorausfahrenen Fahrzeug
"""

import time

# Modul als Klasse schreiben ???
import Distance
import MotorFunctions as Motor

# Konstante zur Anpassung des Tastgrads
x = 1

Motor.initMotor()
Distance.initPins()
Distance.getDistance()

Motor.maxVelocity = 30
Motor.changeVelocity(int(0))
input("Press Enter to continue >> ")

try:
	while True:
		# Entfernungsmessungen
		dist1 = Distance.getDistance()
		t1 = time.time()
		time.sleep(0.01)
		dist2 = Distance.getDistance()
		t2 = time.time()
		
		if dist1 == None or dist2 == None:
			continue
		# Problem:
		# bei kleinen Messungenauigkeiten wird durch das extrem kleine delta t
		# eine grosse Geschwindigkeit errechnet, auch wenn Vrelativ = 0 sein sollte
		speed = ((dist1 - dist2) / (t1 - t2))*x
		Motor.changeVelocity(int(speed))		
			
except:
	print("Ok, something went wrong...")

finally:
	Motor.changeVelocity(int(0))
	Motor.stopMotor()
