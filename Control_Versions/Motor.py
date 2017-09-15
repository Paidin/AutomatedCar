#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Klasse zur Steuerung des Motors via PWM vom RaspberryPi aus
    Entwickelt aus MotorFunctions.py
"""

import RPi.GPIO as gpio
import time


class Motor:
    # Initialisiere alle Variabeln um den Motor zu steuern
    def __init__(self, maxDutyCycle):
        # Speichere maximalen und aktuellen Tastgrad
        self.maxSpeed = int(maxDutyCycle)
        self.currSpeed = 0
        
        # Definiere PWM-Output Pin
        self.pin = 40
        # Nummeriere nach Pin-Nummer
        gpio.setmode(gpio.BOARD)  
        # Definiere Pin-Setup
        gpio.setup(self.pin, gpio.OUT)
    
        # Erstelle und starte Pulsweitenmodulation
        self.pwm = gpio.PWM(self.pin, 500)
        self.pwm.start(0)
        print("Engine running.")
        
    # Ändere die Geschwindigkeit des Motors 
    def changeSpeed(self, deltaDutyCycle):
        # Beschränke die akzeptierten Werte von 0 bis maxSpeed
        newDutyCycle = self.currSpeed + deltaDutyCycle
        if newDutyCycle > self.maxSpeed:
            newDutyCycle = self.maxSpeed
        if newDutyCycle < 0:
            newDutyCycle = 0
        
        # Ändere den Tastgrad langsam (Schutz der Schaltung)
        if newDutyCycle < self.currSpeed:
            for i in range(self.currSpeed, newDutyCycle-1, -1):
                self.pwm.ChangeDutyCycle(float(i))
                time.sleep(0.01)
        if newDutyCycle > self.currSpeed:
            for i in range(self.currSpeed, newDutyCycle+1, 1):
                self.pwm.ChangeDutyCycle(float(i))
                time.sleep(0.01)
        self.currSpeed = newDutyCycle
        return self.currSpeed
    
    # Lege neue Geschwindigkeit des Motors fest
    def setSpeed(self, newDutyCycle):
        # Beschränke die akzeptierten Werte von 0 bis maxSpeed
        if newDutyCycle > self.maxSpeed:
            newDutyCycle = self.maxSpeed
        if newDutyCycle < 0:
            newDutyCycle = 0
        
        # Ändere den Tastgrad langsam (Schutz der Schaltung)
        if newDutyCycle < self.currSpeed:
            for i in range(self.currSpeed, newDutyCycle-1, -1):
                self.pwm.ChangeDutyCycle(float(i))
                time.sleep(0.01)
        if newDutyCycle > self.currSpeed:
            for i in range(self.currSpeed, newDutyCycle+1, 1):
                self.pwm.ChangeDutyCycle(float(i))
                time.sleep(0.01)
        self.currSpeed = newDutyCycle
        return self.currSpeed

    # Gebe den zurzeit eingestellten Tastgrad zurück
    def getCurrentSpeed(self):
        return self.currSpeed    

    # Halte an und beende PWM
    def stop(self):
        self.changeSpeed(0)
        self.pwm.stop()
        print("Engine stopped.")
        
        
        
        
        
        
        
