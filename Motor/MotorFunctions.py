# -*- coding: utf-8 -*-
"""
Funktionen zur Steuerung des Motors via PWM
"""

import RPi.GPIO as gpio
import time
 

maxVelocity = 60
 
# Initialisiere alle Variabeln um den Motor zu steuern
def initMotor():
    # Speichere den derzeitigen duty-cycle
    global currentDutyCycle
    currentDutyCycle = 0
    
    # PWM-Output Pin-Nummer
    motorPin = 40 
    # Nummeriere nach Pin-Nummer
    gpio.setmode(gpio.BOARD)  
    # Definiere Pin-Setup
    gpio.setup(motorPin, gpio.OUT)
    
    # Erstelle und starte PWM
    global pwm
    pwm = gpio.PWM(motorPin, 500)
    pwm.start(0)
    # pwm.ChangeDutyCycle(float(currentDutyCycle))
    print("Motor einsatzbereit")


# Ändere die Geschwindigkeit des Motors
def changeVelocity(newDutyCycle):
    global currentDutyCycle
    # Beschränke die akzeptierten Werte von 0 bis maxVelocity
    if newDutyCycle > maxVelocity:
        newDutyCycle = maxVelocity
    if newDutyCycle < 0:
        newDutyCycle = 0
        
    # Ändere den duty-cycle schonend für die Diode
    if newDutyCycle < currentDutyCycle:
        for i in range(currentDutyCycle, newDutyCycle-1, -1):
            pwm.ChangeDutyCycle(float(i))
            time.sleep(0.01)
        pass
    if newDutyCycle > currentDutyCycle:
        for i in range(currentDutyCycle, newDutyCycle+1, 1):
            pwm.ChangeDutyCycle(float(i))
            time.sleep(0.01)
        pass
    currentDutyCycle = newDutyCycle
    
# Halte an und beende PWM
def stopMotor():
    changeVelocity(0)
    pwm.stop()
    print("Motor ausgeschaltet")
    
    
    
# Teste das Skript
if __name__ == "__main__":
    initMotor()
    for i in range(0, 70, 10):
        changeVelocity(i)
        time.sleep(2.5)
    stopMotor()
