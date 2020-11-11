# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:35:42 2020

@author: 15025

the default language of my computer is german....cry!
"""

import os
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

        if not os.path.exists("./time_data_jogging.txt"):
            local_time = time.localtime()
            self.time_list = [time.strftime("%Y", local_time), time.strftime("%m", local_time),
                              time.strftime("%d", local_time),
                              time.strftime("%H", local_time), time.strftime("%M", local_time),
                              time.strftime("%S", local_time)]
        else:
            with open("./time_data_jogging.txt", "r") as f:
                time_data_list = f.readlines()
                new_data_list = []
                for data in time_data_list:
                    new_data_list.append(int(data.rstrip()))
                self.time_list = new_data_list
            # we need to judge here, whether the time gap reaches 6 hours
            # more than two days
            year_difference = int(time.strftime("%Y")) - self.time_list[0]
            month_difference = int(time.strftime("%m")) - self.time_list[1]
            day_difference = int(time.strftime("%d")) - self.time_list[2]
            hour_difference = int(time.strftime("%H")) - self.time_list[3]
            # the same day
            if year_difference == 0 and month_difference == 0 and day_difference == 0 and hour_difference < 6:
                print("两次运动时间间隔不足六个小时，请保证充足地休息！")
                print("")
                self.flag = False
            # the different day
            if year_difference == 0 and month_difference == 0 and day_difference == 1 and hour_difference < -18:
                print("两次运动时间间隔不足六个小时，请保证充足地休息！")
                print("")
                self.flag = False

    def main_program(self):
        if self.flag:
            self.remind_message()
            self.update_data()
        
    def remind_message(self):
        speech.say("los geht's")
        
        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    speech.say(self.message[i])
                    break
                
        speech.say("Fertig!")
        
    def update_data(self):
        with open("./time_data_jogging.txt", "w+") as f:
            f.write(str(self.time_list[0]) + '\n')
            f.write(str(self.time_list[1]) + '\n')
            f.write(str(self.time_list[2]) + '\n')
            f.write(str(self.time_list[3]) + '\n')
            f.write(str(self.time_list[4]) + '\n')
            f.write(str(self.time_list[5]) + '\n')
    

if __name__ == "__main__":
    main = Debug()
    main.main_program()
