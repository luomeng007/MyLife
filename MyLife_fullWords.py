# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:55:11 2020

@author: 15025
"""

import time
import speech
import numpy as np


class MainGame:
    def __init__(self):
        pass
    
    def mainGame(self):
        while True:
            print("主界面")
            print("请您选择，提示：请输入序号1, 2或者3")
            print("1. 慢跑")
            print("2. 学习")
            print("3. 清洁")
            choice = input("您的决定:  ")
            print("")
            if choice == "1":
                j = Jogging()
                j.mainProgram()
            elif choice == "2":
                s = Study()
                s.mainProgram()
            elif choice == "3":
                c = Cleaning()
                c.mainProgram()
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1,2或者3")
            
            
class Jogging:
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
    
    def mainProgram(self):
        self.startJogging()
        
    def startJogging(self):
        print("慢跑开始！")
        speech.say("los geht's")
        
        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    speech.say(self.message[i])
                    print(f"已经过去了{i + 1}分钟")
                    break
                
        speech.say("Fertig!")
        print("慢跑结束!")
    

class Study:
    def __init__(self):
        while True:
            print("请您选择，提示：请输入序号1或者2")
            print("1. 学习20分钟")
            print("2. 学习50分钟")
            self.choice = input("您的决定:  ")
            print("")
            if self.choice == "1":
                self.total_time = 20 * 60
                break
            elif self.choice == "2":
                self.total_time = 50 * 60
                break
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1或者2")
        
        self.start_time = time.time()
    
    def mainProgram(self):
        self.startLearning()
        
    def  startLearning(self):
        print("开始学习！")
        speech.say("los geht's")
        
        while round(time.time() - self.start_time) != self.total_time:
            # 这里可以加入一些语音互动
            pass
        
        speech.say("fertig!")
        print("学习完成！")
        

class Cleaning:
    def __init__(self):
        self.start_time = time.time()
        
        self.minutes = 20
        
        self.timestamp = np.arange(self.minutes) + 1
    
    def mainProgram(self):
        print("开始打扫！")
        speech.say("los geht's")
        
        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    print(f"已经过去了{i + 1}分钟")
                    break
                
        speech.say("Fertig!")
        print("清洁结束!")
        
    
if __name__ == "__main__":
    # ML: My Life
    ML = MainGame()
    ML.mainGame()