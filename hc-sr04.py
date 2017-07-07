## https://tutorials-raspberrypi.de/entfernung-messen-mit-ultraschallsensor-hc-sr04/

#!/usr/bin/python3
# Datei ultraschall.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
trig = 11 # GPIO-Pin-Nummern
echo = 13
GPIO.setup(echo, GPIO.IN) 
GPIO.setup(trig, GPIO.OUT)

while True :
	GPIO.output(trig, True) 
	time.sleep (0.00001) # 10  Mikrosekunden
	GPIO.output(trig, False)
	
	while GPIO.input(echo) == 0: 
		pass
	start = time.time()
	while GPIO.input(echo) == 1:
		pass
	ende = time.time()
	entfernung = ((ende - start) * 34300) / 2 
	print("Entfernung:", entfernung , "cm") 
	time.sleep (0.5)
	
GPIO.cleanup()
