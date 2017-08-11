# -*- coding: utf-8 -*-
"""
Diese Datei enthält Funktionen, die es mithilfe eines
HC-SR04 Ultraschallsensors ermöglichen, Entfernungen zu messen

Hinweise zur RPi Bibliothek
  - Nummeriere nach Pin-Nummer
    gpio.setmode(gpio.BOARD)
    
  - Nummeriere nach GPIO-Bezeichnung
    gpio.setmode(gpio.BCM)
    
  - Output der GPIO-Pins ein/ausschalten
    gpio.output(pin, [True, False])
    gpio.output(pin, [gpio.HIGH, gpio.LOW])   
    
  - Zustandsänderungen (Edges)
    gpio.RISING     gpio.LOW >>> gpio.HIGH
    gpio.FALLING    gpio.HIGH >>> gpio.LOW
    gpio.BOTH       gpio.RISING or gpio.FALLING
    
  - Abwarten einer Zustandsänderung an den GPIO-Pins
    gpio.wait_for_edge(pin, [gpio.RISING, gpio.FALLING, gpio.BOTH], timeout=milliseconds)

  - Dokumentation der RPi Bibliothek und Download
    https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/   
"""

import RPi.GPIO as gpio
import time

# Initialisiere GPIO-Pins
def initPins():
    # Trigger Pin-Nummer
    trig = 11
    # Echo Pin-Nummer
    echo = 12
    
    # Nummeriere nach Pin-Nummer
    gpio.setmode(gpio.BOARD)
    
    # Definiere Pin-Setup
    gpio.setup(trig, gpio.OUT)
    gpio.setup(echo, gpio.IN)

    
# Zurücksetzen der GPIO-Pins
def clearPins():
    gpio.cleanup()

    
# Funktiuon um einen 10 Mikrosekunden langen Schallimpuls zu senden
def sendTriggerPulse():
    # Setze Output auf HIGH
    gpio.output(trig, True)
    # Warte 10 Mikrosekunden (Impulsdauer)
    time.sleep(0.0001)   
    # Setze Output auf LOW
    gpio.output(trig, False)

    
# Funktion um mit dem Ultraschallsensor die Distanz zu einem Objekt zu bestimmen
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
    return distance


if __name__=="__main__":
    initPins()
    try:
        while True:
            print("Distance: %.2f cm" % (getDistance()))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program closed")
    clearPins()

