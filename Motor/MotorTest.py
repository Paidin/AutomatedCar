# -*- coding: utf-8 -*-
"""
Test um den Motor Schrittweise zu beschleunigen und anzuhalten
"""

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

try:
    for dutyCycle in range(10, 61, 5):
        pwm.ChangeDutyCycle(float(dutyCycle))
        print("DutyCycle: ", dutyCycle)
        if str(input("Press Enter to continue >> ")) != "":
            break
            
except:
    print("Program closed")


for dutyCycle in range(50, -1, -1):
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.01)
  

# stoppe pwm
pwm.stop()

# nicht benötigt, pwm.stop reicht aus um Spannung an pin auf 0.000 V zu setzen
#GPIO.output(pin, False)

# GPIO.cleanup führt zu ca 50-100 mV am GPIO-Pin! statt 0 mV
#GPIO.cleanup()
