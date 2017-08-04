"""
Funktionen zu Steuerung eines DC-Brushed-Motors 
via ESC(ElectronicSpeedControl) und RaspberryPi

Dokumentation zur Pulsweitenmodulation mit Rpi.GPIO:
https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
"""

import RPi.GPIO as gpio
from time import sleep

# RaspberryPi Pin 5, GPIO3
ESC = 3

gpio.setmode(gpio.BOARD)
gpio.setup(ESC, gpio.OUT)

# nach Anleitung ESC und mit viel gutem Willen
def calibrate(Min, Neutral, Max):
	print("Motorkabel entfernen und ausschalten")
	input("Enter to continue >>> ")
	pwm = gpio.pwm(ESC, 50.0)
	pwm.start(Neutral)
	
	print("Einschalten und Set Knopf drücken")
	print("LED blinkt Rot-Grün-Orange-Rot")
	print("Set Knopf freigeben wenn LED rot leuchtet")
	print("Wenn nun LED rot blinkt fortfahren")
	input("Enter to continue >>> ")
	pwm.ChangeDutyCycle(Max)
	
	print("Set Knop einmal drücken, LED blinkt nun zweifach")
	input("Enter to continue >>> ")
	pwm.ChangeDutyCycle(Min)
	
	print("Set Knop einmal drücken, LED geht aus")
	input("Enter to continue >>> ")
	sleep(5)
	pwm.stop()
    print("Finished Calibration :)")

gpio.cleanup()
	
	
	
	












