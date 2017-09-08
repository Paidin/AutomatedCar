import RPi.GPIO as GPIO
import time
 
pin = 40 

 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 500)
pwm.start(0)

dutyCycle = 0
pwm.ChangeDutyCycle(float(dutyCycle))
input("Press Enter to start >> ")

checker = true
distance1 = 1.0
distance2 = 1.0
x = 1.0 # Auswechseln durch Geschwindigkeit/DutyCycle Konstante

def initPins():
    # Trigger Pin-Nummer
    global trig
    trig = 11
    # Echo Pin-Nummer
    global echo
    echo = 12
    
def sendTriggerPulse():
    # Setze Output auf HIGH
    gpio.output(trig, True)
    # Warte 10 Mikrosekunden (Impulsdauer)
    time.sleep(0.0001)   
    # Setze Output auf LOW
    gpio.output(trig, False)
    
def getDistance():
    # Sende Impuls
    sendTriggerPulse()
    # Warte maximal 1 Sekunde auf Beginn der Antwort
    gpio.wait_for_edge(echo, gpio.RISING, timeout=1000)
    start = time.time()
    # Warte maximal 1 Sekunde auf Ende der Antwort
    gpio.wait_for_edge(echo, gpio.FALLING, timeout=1000)
    end = time.time()
    # Berechne Distanz in cm aus der vergangenen Zeit
    distance = (end-start) * 34300 / 2.0
    

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
		
finally:
	for dutyCycle in range(50, -1, -1):
    	pwm.ChangeDutyCycle(dutyCycle)
    	time.sleep(0.01)
	# stoppe pwm
	pwm.stop()