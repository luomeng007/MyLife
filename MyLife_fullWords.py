# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 19:55:11 2020

@author: 15025
"""

import os
import time
import speech
import numpy as np


class MainGame:
    if not os.path.exists("C:/Users/15025/Desktop/data.txt"):
        attribute_list = [0, 0, 0, 0]
    else:
        with open("C:/Users/15025/Desktop/data.txt", 'r') as f:
            data_list = f.readlines()
            new_data_list = []
            for data in data_list:
                new_data_list.append(float(data.rstrip()))
            attribute_list = new_data_list
    
    def __init__(self):
        pass
    
    def mainGame(self):
        while True:
            print("主界面")
            print("请您选择，提示：请输入序号1, 2或者3")
            print("1. 慢跑")
            print("2. 学习")
            print("3. 冥想")
            print("4. 清洁")
            print("5. 查看当前属性值")
            choice = input("您的决定: ")
            print("")
            if choice == "1":
                j = Jogging()
                j.mainProgram()
            elif choice == "2":
                s = Study()
                s.mainProgram()
            elif choice == "3":
                m = Meditation()
                m.mainProgram()
            elif choice == "4":
                c = Cleaning()
                c.mainProgram()
            elif choice == "5":
                self.displayData()
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1,2或者3")
                continue
            
            self.saveData()
                
    def displayData(self):
        print('-'*18+'玩家当前属性 ' + '-' * 18)
        print('健康值:'.ljust(20)+ '|' + '{0}'.format(MainGame.attribute_list[0]).rjust(28))
        print('学术值:'.ljust(20)+ '|' + '{0}'.format(MainGame.attribute_list[1]).rjust(28))
        print('精神值:'.ljust(20)+ '|' + '{0}'.format(MainGame.attribute_list[2]).rjust(28))
        print('清洁值:'.ljust(20)+ '|' + '{0}'.format(MainGame.attribute_list[3]).rjust(28))
        
    def saveData(self):
        with open("C:/Users/15025/Desktop/data.txt", "w+") as f:
            f.write(str(MainGame.attribute_list[0]) + '\n')
            f.write(str(MainGame.attribute_list[1]) + '\n')
            f.write(str(MainGame.attribute_list[2]) + '\n')
            f.write(str(MainGame.attribute_list[3]) + '\n')
            
            
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
        
        MainGame.attribute_list[0] += 1
    

class Study:
    def __init__(self):
        while True:
            print("请您选择，提示：请输入序号1或者2")
            print("1. 学习20分钟")
            print("2. 学习50分钟")
            self.choice = input("您的决定: ")
            print("")
            if self.choice == "1":
                self.total_time = 20 * 60
                break
            elif self.choice == "2":
                self.total_time = 50 * 60
                break
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1或者2")
                continue
        
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
        
        if self.choice == "1":
            MainGame.attribute_list[1] += 0.5
        if self.choice == "2":
            MainGame.attribute_list[1] += 1
        

class Meditation:
    def __init__(self):
        self.start_time = time.time()
        
        self.minutes = 20
        
        self.timestamp = np.arange(self.minutes) + 1

    def mainGame(self):
        print("开始冥想！")
        speech.say("los geht's")
        
        for i in range(self.minutes):
            while True:
                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    print(f"已经过去了{i + 1}分钟")
                    break
                
        speech.say("Fertig!")
        print("冥想结束!")
        
        MainGame.attribute_list[2] += 1


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
        
        MainGame.attribute_list[3] += 1
        
    
if __name__ == "__main__":
    # ML: My Life
    ML = MainGame()
    ML.mainGame()