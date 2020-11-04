# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:35:42 2020

@author: 15025
"""

import speech
import time
import numpy as np
import random
# if two files are not in a common directory, we need to add sentence as below
import sys
sys.path.append(r"D:/User(origin in C)/desktop/MyLife-main/Modules/")
import remindMessage


class Debug:
    def __init__(self):
        self.start_time = time.time()

        self.flag = True

        self.minutes = 20

        self.timestamp = np.arange(self.minutes) + 1

        self.message = remindMessage.message

    def mainProgram(self):
        self.remindMessage()


    def remindMessage(self):
        speech.say("运动开始啦！")

        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    speech.say(self.message[i][random.randint(0, len(self.message[i]) - 1)])
                    break

        speech.say("恭喜主人，完成运动!")

    def Gui(self):
        pass


if __name__ == "__main__":
    main = Debug()
    main.mainProgram()
