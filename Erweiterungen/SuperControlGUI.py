#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Dateiname: SuperControlGUI.py
    derzeit noch in der Entwicklungsphase und daher noch nicht voll einsatzfähig
    
    Diese Datei soll Lenkung des Servos über eine graphische Benutzeroberfläche
    ermöglichen. Soll über VNC-verbindung kontrolliert werden
    
    Ausserdem ermöglicht sie eine manuelle Kontrolle über das Fahrzeug und 
    erlaubt es den Abstandregeltempomaten ein oder auszuschlten
"""

import tkinter as tk
import threading


import Servo
import CruiseControlClass

#%%
StopCruiseControl = True

class Application(tk.Frame):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack()
        
        # Slider für Servo
        self.servo = tk.Scale(self.frame, from_=(-90), to=(+90), orient=tk.HORIZONTAL, command=self.changeServoAngle, length=600)
        self.servo.grid(row=0, column=1)
        
        # Slider für Speed
        self.speed = tk.Scale(self.frame, from_=(30), to=(0), orient=tk.VERTICAL, command=self.changeMotorSpeed, length=200)
        self.speed.grid(row=0, column=0)
        
        # Buttonum das Programm zu schliessen
        self.buttonClose = tk.Button(self.frame, text="Close", command=self.close, height=5, width=10)
        self.buttonClose.grid(row=1, column=2)
        
        # Button zu ein/ausschalten des Abstandregeltempomaten
        self.buttonACC = tk.Button(self.frame, text="Start ACC", command=self.changeDrivingMode, height=5)
        self.buttonACC.grid(row=1, column=0)
        
        # Klasse zur Ansteuerung des Servos
        self.servoMotor = Servo.Servo(38, 50)
        
        # Klasse des Abstandregeltempomaten
        self.ACC = CruiseControlClass.Cruise(50, 30)
        print("Engine running\n connect power-supply")
        
      
    def changeServoAngle(self, angle):
        self.servoMotor.setAngle(angle)
        #thread = threading.Thread(target=self.servoMotor.setAngle, args=(angle))
        #thread.start()
        pass
        
    def changeMotorSpeed(self, speed):
        self.ACC.getMotor().setSpeed(int(speed))
        #thread = threading.Thread(target=self.ACC.getMotor().setSpeed, args=(int(speed)))
        #thread.start()
        pass
        
    def changeDrivingMode(self):
        global StopCruiseControl
        self.buttonACC.destroy()
        self.speed.destroy()
        
        # Starte Abstandsregeltempomaten
        if StopCruiseControl:
            # Ändere den Button
            self.buttonACC = tk.Button(self.frame, text="Stop ACC", command=self.changeDrivingMode, height=20)
            self.buttonACC.grid(row=0, column=0)
            # Aktiviere ACC
            StopCruiseControl = False
            control = threading.Thread(target=self.ACC.mainloop, name="Adaptive Cruise Control")
            control.start()
            
        # Starte manuellen Modus
        else:
            # Deaktiviere ACC
            StopCruiseControl = True
            # Erstelle Schieberegler für Speed
            self.speed = tk.Scale(self.frame, from_=(30), to=(0), orient=tk.VERTICAL, command=self.changeMotorSpeed, length=200)
            self.speed.grid(row=0, column=0)
            # Ändere den Button
            self.buttonACC = tk.Button(self.frame, text="Start ACC", command=self.changeDrivingMode, height=5)
            self.buttonACC.grid(row=1, column=0)
            
    # Schliesse das Fenster und beende alle Prozesse         
    def close(self):
        try:
            self.ACC.close()
        except: pass
        self.frame.master.destroy()




#%%
# Starte Programm
if __name__ == "__main__":
    
    try:
        root = tk.Tk()
        root.title("Servo Control")
        app = Application(root)
        root.mainloop()
        
    except Exception as e:
        print("Error:", e)
  
