#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    In der Entwicklungsphase, noch nicht getestet
    Funktion changeAngle() wird von SuperControlGUI.py verwendet

    Frequenz für Servos: 50 Hz (alle 20 Millisekunden Impuls erwartet)
    100 Hz dürfte auch funktionieren (Impuls alle 10 Millisekunden)
    Impulslänge:
        nach Raspi Kochbuch
        1.5 Millisekunden: Neutralstellung   90°
        1.0 Millisekunden: Ausschlag links    0°
        2.0 Millisekunden: Ausschlag rechts 180°
        
        oder für andere Winkelbereiche
        0.5 Millisekunden: Ausschlag links  -90°
        1.5 Millisekunden: Neutralstellung    0°
        2.5 Millisekunden: Ausschlag rechts +90°
    hier werden vorerst Angaben des Raspi Kochbuchs berücksichtigt  
"""


import RPi.GPIO as gpio
import threading
import time


class Servo:
    # Erstelle eine neue Instanz um einen Servo anzusteuern
    # @argument signalPin Pin-Nummer des Raspberry für Signalübertragung
    # @argument frequency Frequenz für die Pulsweitenmodulation
    def __init__(self, signalPin, frequency):
        # Setze die Raspberry Pins auf
        gpio.setmode(gpio.BOARD)
        gpio.setup(signalPin, gpio.OUT)
        
        self.maxRight   = 0.002     # Signallänge für max Ausschlag Rechts
        self.maxLeft    = 0.001     # Signallänge für max Ausschlag Links
        self.angle      = 0         # Aktueller Ausschlagwinkel range(-90, +90)
        self.frequency  = frequency # Frequenz für Pulsweitenmodulation
        self.running    = False     # Abbruchbedingung des mainLoops
        self.mainThread = threading.Thread(target=self.mainLoop) 
        
        # Starte PWM und setze Servo in Neuralstellung
        self.pwm = gpio.PWM(signalPin, self.frequency)
        self.pwm.start(0)
        self.setAngle(0)
        
    # Funktion um einen anderen Ausschlag des Servo festzulegen
    # Akzeptierter Winkelbereich: -90° (links) bis +90° (rechts)
    # Neutralstellung: 0°
    def setAngle(self, newAngle):
        # Rechne auf Werte im Gültigkeitsbereich um
        newAngle += 90
        self.angle = self.checkAngle(newAngle)
        # Berechne die benötigte Signallänge
        signalLength  = (self.maxRight-self.maxLeft)/100
        signalLength *= 100/180*self.angle
        signalLength += self.maxLeft
        # Aktualisiere die Pulsweitenmodulation
        newDutyCycle = 100 * self.frequency * signalLength
        self.pwm.ChangeDutyCycle(float(newDutyCycle))
    
    # Funktion um den Ausschlag um eine bestimmten Winkel zu ändern         
    def changeAngle(self, deltaAngle):
        # Rechne den Wert um und übergebe ihn setAngle
        self.angle += (deltaAngle - 90)
        self.setAngle(self.angle)
            
    # Kontrolliere den Gültigkeitsbereich des Ausschlagwinkels
    def checkAngle(self, angle):
        if angle < 0:
            return 0
        elif angle > 180:
            return 180
        else:
            return angle
    
    # Aktualisiere bei Keyboard-Input
    def mainLoop(self):
        while self.running:
            # Überprüfe ob KeyPressedEvent stattfand
            # changeAngle()
            # or set running false
            pass
    
    # Starte den mainLoop als thread  
    def start(self):
        self.running = True
        self.mainThread.start()
        print("Servo mainLoop was started")
        
    # Beende den mainLoop thread
    def stop(self):
        self.running = False
        self.mainThread.join()
        print("Servo mainLoop was terminated")
        
        
 # ----------------------------------------------------------------------------       
if __name__ == "__main__":
    
    servo = Servo(10, 100)
    servo.start()
    time.sleep(5)
    servo.stop()
    pass

