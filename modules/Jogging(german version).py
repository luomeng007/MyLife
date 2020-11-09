# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:35:42 2020

@author: 15025

the default language of my computer is german....cry!
"""

import speech
import time
import numpy as np


class Debug:
    def __init__(self):
        self.start_time = time.time()
        
        self.flag = True
        
        self.minutes = 20
        
        self.timestamp = np.arange(self.minutes) + 1
        
        self.message = ["Eine Minute verging", "Zwei Minuten vergingen", "Drei Minuten vergingen", "Vier Minuten vergingen",
                        "Fünf Minuten vergingen", "Sechs Minuten vergingen", "Sieben Minuten vergingen", "Acht Minuten vergingen",
                        "Neu Minuten vergingen", "Zehn Minuten vergingen", "Elf Minuten vergingen", "Zwölf Minuten vergingen",
                        "dreizehn Minuten vergingen", "vierzehn Minuten vergingen", "fünfzehn Minuten vergingen", "Sechszehn Minuten vergingen",
                        "Siebzehn Minuten vergingen", "Achtzehn Minuten vergingen", "Neunzehn Minuten vergingen", "Zwanzig Minuten vergingen"]
        
    def main_program(self):
        self.remind_message()
        
    def remind_message(self):
        speech.say("los geht's")
        
        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    speech.say(self.message[i])
                    break
                
        speech.say("Fertig!")
        
    def gui(self):
        pass
    

if __name__ == "__main__":
    main = Debug()
    main.main_program()