"""
	Skript um Entfernungsmessungen und Motorgeschwindigkeit zu kombinieren
"""


import RPi.GPIO as GPIO
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
Motor.changeVelocity(float(0))
input("Press Enter to continue >> ")

"""
# alter Code, ohne Verwendung unserer Funktionen in Distance.py und MotorFunctions.py
try:
	while checker == true
		distance1 = getDistance()
		time.sleep (0.1)
		distance2 = getDistance()
		dutyCycle = ((distance1 - distance2) / 0.1)*x
		if dutyCycle > 30
			dutyCycle = 30
		if dutyCycle = 0
			checker = false
		pwm.ChangeDutyCycle(float(dutyCycle))
"""

# neuer Code
try:
	while True:
		dist1 = Distance.getDistance()
		t1 = time.time()
		time.sleep(0.01)
		dist2 = Distance.getDistance()
		t2 = time.time()
		
		if dist1 == None or dist2 == None:
			continue
		
		# Mathematik dahinter überprüfen bitte :)
		speed = ((dist1 - dist2) / (t1 - t2))*x
		Motor.changeVelocity(float(speed))
		
			
except:
	print("Ok, something went wrong...")

finally:
	Motor.changeVelocity(float(0))
	Motor.stopMotor()
