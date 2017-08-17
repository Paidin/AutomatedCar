#diesen Code ind 298einmotor.py bei try einsetzen und den Rest löschen, falls 298einmotor.py funktioniert.



# PWM-Signal auf Pins 13 und 15 mit 100 Hz
pwmA = GPIO.PWM(EnableA ,100) 

try:
	while True :
		# Eingabefeld zur Richtungsauswahl
		richtung =input ("Wählen Sie die Drehrichtung: 'V' oder 'Z': ")

		# Duty Cycle eingeben
		geschwindigkeit = input("Wählen Sie die Geschwindigkeit: '1 - 100': ")
		if richtung == "V":
			# PWM starten mit 100 Hz und dem eingegebenen Duty Cycle 
			pwmA.start(float(geschwindigkeit))
			GPIO.output(Input1, True)
			GPIO.output(Input2, False)
			sleep (5)
			GPIO.output(EnableA, False)
			GPIO.output(Input1, False)
		if richtung == "Z": 
			pwmA.start(float(geschwindigkeit)) 
			GPIO.output(Input1, False) 
			GPIO.output(Input2, True)
			sleep (5) 
			GPIO.output(EnableA, False) 
			GPIO.output(Input2, False)

# Beim Beenden des Programms durch Strg+C wird # all_off() ausgeführt.
except KeyboardInterrupt :
	all_off()
