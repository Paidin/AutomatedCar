#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Klasse mit Funktionen, die es ermöglichen einen beliebig langen Verlauf
    zu speichern
    
    Könnte benutzt werden, um stark abweichende Messwerte des Ultraschall-
    moduls zu erkennen und sie zu ignorieren, um Auto ruckfreier fahren 
    zu lassen.
"""

# Speichere gemessene Werte
class History:
    
    # Initialisiere alle nötigen Variabeln
    def __init__(self, length):
        self.maxLength = int(length)
        self.history = []
        for i in range(0, self.maxLength):
            self.history.append(0)
    
    # Aktualisiere den Verlauf
    def update(self, value):
        for i in range(self.maxLength-1, 0, -1):
            self.history[i] = self.history[(i-1)]
        self.history[0] = value
    
    # Gebe den Wert eines beliebigen Items zurück - Neuestes Item: int(1)
    def getItem(self, num):
        try:
            return self.history[num-1]
        except:
            return False

    # Gebe eine Liste mit allen Items zurück
    def getItemList(self):
        return self.history
    
    # Print Funktion für diese Klasse
    def print(self):
        print(self.history)
