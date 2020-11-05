# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:31:37 2020

@author: 15025
"""

import speech
import time


class Debug:
    def __init__(self):
        self.start_time = time.time()
        
        self.flag = True
        
        self.minutes = input("How many minutes do you prefer: \n")
        
        while self.flag:
            if self.minutes.startswith('-'):
                if self.minutes.lstrip('-').isdigit():
                    self.minutes = int(self.minutes)
                else:
                    print("")
                    print("The input should be a number in interval [0, 60]~", end="")
                    self.minutes = input("please input a correct value: \n")
                    continue 
                
            elif self.minutes.lstrip('-').isdigit():
                self.minutes = int(self.minutes)
                
            else:
                print("")
                print("The input should be a number in interval [0, 60]~~", end="")
                self.minutes = input("please input a correct value: \n")
                continue 
                
                
            if 0 < self.minutes <= 60:
                speech.say("Jetzt los")
                self.flag = False
            else:
                print("")
                print("The input number should in interval [0, 60]~~~", end="")
                self.minutes = input("please input a correct value: \n")
                continue
                    
        self.seconds = self.minutes * 60
        
        
    def mainProgram(self):
        while round(time.time() - self.start_time) != self.seconds:
            pass
        speech.say("Du solllest dich ausruhen")
        
        
main = Debug()
main.mainProgram()