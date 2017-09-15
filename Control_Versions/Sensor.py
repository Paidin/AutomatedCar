#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Diese Datei enthält eine Klasse, die es mithilfe eines
    HC-SR04 Ultraschallsensors ermöglicht, Entfernungen zu messen
    Entwickelt aus Distance.py
"""

import RPi.GPIO as gpio
import time


class Sensor:
    # Initialisiere alle Variabeln um Motor zu steuern
    def __init__(self):
        # Trigger und Echo Pins
        self.trig = 11
        self.echo = 12
        # Nummerierung nach Pin-Nummer
        gpio.setmode(gpio.BOARD)
        # Definiere Pin Setup
        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
        
    # Funktion um einen 10 Mikrosekunden langen Schallimpuls zu senden
    def sendTriggerPulse(self):
        # Setze Output auf HIGH
        gpio.output(self.trig, True)
        # Warte 10 Mikrosekunden (Impulsdauer)
        time.sleep(0.0001)   
        # Setze Output auf LOW
        gpio.output(self.trig, False)
        
    # Funktion um mit dem Ultraschallsensor die Distanz zu einem Objekt zu bestimmen
    def getDistance(self):
        # Sende Impuls
        self.sendTriggerPulse()
        # Warte maximal 1 Sekunde auf Beginn der Antwort
        gpio.wait_for_edge(self.echo, gpio.RISING, timeout=100)
        start = time.time()
        # Warte maximal 1 Sekunde auf Ende der Antwort
        gpio.wait_for_edge(self.echo, gpio.FALLING, timeout=100)
        end = time.time()
        # Berechne Distanz in cm aus der vergangenen Zeit
        distance = (end-start) * 34300 / 2.0
        
        # Werte über 1'700 cm können ignoriert werden (Timeout)
        if distance > 1700:
            return None
        return distance
        
    
if __name__ == "__main__":
    # Bereite Messungen vor
    sensor = Sensor()
    sensor.getDistance()
    
    try:
        while True:
            distance = sensor.getDistance()
            if distance != None:
                print("Distance: %.2f cm" % distance)
            else:
                print("Error - Messwert zu gross")
            # Sensor kann alle 20 ms neue Messung beginnen
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("Program closed")
