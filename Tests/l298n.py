#!/usr/bin/python3
# -*- coding : utf -8 -* 
# Quelle: RaspberryPi, das umfassende Handbuch (Kofler, Kühnast, Scherbeck)

from time import sleep 
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)

# Funktion, um alle genutzten Pins auf Low zu schalten
def all_off(): 
GPIO.output(EnableA, False) 
GPIO.output(EnableB,False) 
GPIO.output(Input1,False) 
GPIO.output(Input2,False) 
GPIO.output(Input3,False) 
GPIO.output(Input4,False) 
return

# Den GPIO-Pins werden die Namen der L298-Eingänge zugewiesen.
EnableA = 13 
EnableB = 15 
Input1 = 3 
Input2 = 5 
Input3 = 7
Input4 = 11

# Alle genutzten GPIO-Pins als Ausgang deklarieren.
GPIO.setup(EnableA,GPIO.OUT) 
GPIO.setup(EnableB,GPIO.OUT) 
GPIO.setup(Input1,GPIO.OUT) 
GPIO.setup(Input2,GPIO.OUT) 
GPIO.setup(Input3,GPIO.OUT) 
GPIO.setup(Input4,GPIO.OUT)

# Funktion "all_off" aufrufen
all_off()


try:
	while True :
		# Eingabefeld zur Motorauswahl .
		# Groß-/Kleinschreibung beachten.
		motor = input("Geben Sie den Motor ein: 'A' oder 'B': ") 
		# Eingabefeld zur Richtungsauswahl .
		richtung =
		input("Geben Sie die Drehrichtung ein: 'V' oder 'Z': ")
		
		# if-Schleifen zur Abfrage der vorherigen Eingabe
		if motor == "A" and richtung == "V" :
			GPIO.output(EnableA, True)
			GPIO.output(Input1, True) 
			GPIO.output(Input2, False)
			sleep (5)				#Motor dreht jeweils 5 Sekunden.
			GPIO.output(EnableA, False) 
			GPIO.output(Input1, False)
		if motor == "A" and richtung == "Z" :
			GPIO.output(EnableA, True) 
			GPIO.output(Input1, False) 
			GPIO.output(Input2, True) 
			sleep (5) 
			GPIO.output(EnableA, False) 
			GPIO.output(Input2, False)
		if motor == "B" and richtung == "V" :
			GPIO.output(EnableB, True) 
			GPIO.output(Input3, True) 
			GPIO.output(Input4, False) 
			sleep (5) 
			GPIO.output(EnableB, False) 
			GPIO.output(Input3, False)
		if motor == "B" and richtung == "Z" :
			GPIO.output(EnableB, True) 
			GPIO.output(Input3, False) 
			GPIO.output(Input4, True) 
			sleep (5) 
			GPIO.output(EnableB, False) 
			GPIO.output(Input4, False)
			
# beim Programmende durch Strg+C wird "all_off" ausgeführt
except KeyboardInterrupt : 
	all_off()
			
			
			
			
			
