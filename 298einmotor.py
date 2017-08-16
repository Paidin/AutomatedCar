from time import sleep 
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)

def all_off(): 
GPIO.output(EnableA, False) 
GPIO.output(Input1,False) 
GPIO.output(Input2,False) 


#Namen könnten bei unserem Motortreiber anders sein
EnableA = 13 
Input1 = 3 
Input2 = 5 


GPIO.setup(EnableA,GPIO.OUT) 
GPIO.setup(Input1,GPIO.OUT) 
GPIO.setup(Input2,GPIO.OUT) 

all_off()

try:
	while True :
	
	richtung =
		input(" Geben sie Drehrichtung des Motors an: 'V' oder 'Z': ")
		
	if richtung == "V" :
			GPIO.output(EnableA, True)
			GPIO.output(Input1, True) 
			GPIO.output(Input2, False)
			sleep (5)				#Motor dreht jeweils 5 Sekunden.
			GPIO.output(EnableA, False) 
			GPIO.output(Input1, False)
			
	if richtung =="Z"  :
			GPIO.output(EnableA, True)
			GPIO.output(Input1, False)
			GPIO.output(Input2, True)
			sleep (5)				#Motor dreht jeweils 5 Sekunden.
			GPIO.output(EnableA, False) 
			GPIO.output(Input2, False)
		
		
		except KeyboardInterrupt : 
		all_off()