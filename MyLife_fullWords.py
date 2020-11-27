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
    if not os.path.exists("./user_data.txt"):
        attribute_list = [0, 0, 0, 0]
    else:
        with open("./user_data.txt", 'r') as f:
            user_data_list = f.readlines()
            new_data_list = []
            for data in user_data_list:
                new_data_list.append(float(data.rstrip()))
            attribute_list = new_data_list

    if not os.path.exists("./time_data_today.txt"):
        # time_year = time.strftime("%Y", local_time)
        # time_month = time.strftime("%m", local_time)
        # time_day = time.strftime("%d", local_time)
        # time_hour = time.strftime("%H", local_time)
        # time_minute = time.strftime("%M", local_time)
        # time_second = time.strftime("%S", local_time)
        local_time = time.localtime()
        time_list = [time.strftime("%Y", local_time), time.strftime("%m", local_time), time.strftime("%d", local_time)]
    else:
        with open(".time_data_today", "r") as f:
            time_data_list = f.readlines()
            new_data_list = []
            for data in user_data_list:
                new_data_list.append(int(data.rstrip()))
            time_list = new_data_list

    def __init__(self):
        pass

    def main_game(self):
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
                j.main_program()
            elif choice == "2":
                s = Study()
                s.main_program()
            elif choice == "3":
                m = Meditation()
                m.main_program()
            elif choice == "4":
                c = Cleaning()
                c.main_program()
            elif choice == "5":
                self.display_data()
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1,2或者3")
                continue

            # 循环保存效率并不高
            self.save_data()

    @staticmethod
    def display_data():
        print('-' * 18 + '玩家当前属性 ' + '-' * 18)
        print('健康值:'.ljust(20) + '|' + '{0}'.format(MainGame.attribute_list[0]).rjust(28))
        print('学术值:'.ljust(20) + '|' + '{0}'.format(MainGame.attribute_list[1]).rjust(28))
        print('精神值:'.ljust(20) + '|' + '{0}'.format(MainGame.attribute_list[2]).rjust(28))
        print('清洁值:'.ljust(20) + '|' + '{0}'.format(MainGame.attribute_list[3]).rjust(28))

    @staticmethod
    def save_data():
        with open("./user_data.txt", "w+") as f:
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

        self.message = ["Eine Minute verging", "Zwei Minuten vergingen", "Drei Minuten vergingen",
                        "Vier Minuten vergingen",
                        "Fünf Minuten vergingen", "Sechs Minuten vergingen", "Sieben Minuten vergingen",
                        "Acht Minuten vergingen",
                        "Neu Minuten vergingen", "Zehn Minuten vergingen", "Elf Minuten vergingen",
                        "Zwölf Minuten vergingen",
                        "dreizehn Minuten vergingen", "vierzehn Minuten vergingen", "fünfzehn Minuten vergingen",
                        "Sechszehn Minuten vergingen",
                        "Siebzehn Minuten vergingen", "Achtzehn Minuten vergingen", "Neunzehn Minuten vergingen",
                        "Zwanzig Minuten vergingen"]

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
            self.start_jogging()
            # once the whole process is successfully finished, then we update the data
            self.update_data()

    def start_jogging(self):
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

    def update_data(self):
        # save current time to .txt file
        with open("./time_data_jogging.txt", "w+") as f:
            f.write(str(self.time_list[0]) + '\n')
            f.write(str(self.time_list[1]) + '\n')
            f.write(str(self.time_list[2]) + '\n')
            f.write(str(self.time_list[3]) + '\n')
            f.write(str(self.time_list[4]) + '\n')
            f.write(str(self.time_list[5]) + '\n')


class Study:
    def __init__(self):
        while True:
            print("请您选择，提示：请输入序号1或者2")
            print("1. 学习30分钟")
            print("2. 学习60分钟")
            self.choice = input("您的决定: ")
            print("")
            if self.choice == "1":
                self.total_time = 30 * 60
                break
            elif self.choice == "2":
                self.total_time = 60 * 60
                break
            else:
                print("您的输入值有误，请重新输入！提示：输入数字1或者2")
                continue

        self.start_time = time.time()

        self.flag = True

        if not os.path.exists("./time_data_study.txt"):
            self.time_total_study = 0
        else:
            with open("./time_data_study.txt", "r") as f:
                time_data = f.readline()
                self.time_total_study = float(time_data)
                # judge whether the total time reaches 8 hours
                if self.time_total_study >= 8:
                    print("今天学习时间太久了，请做点儿别的事情吧！")
                    print("")
                    self.flag = False
                if self.choice == "2" and self.time_total_study == 7.5:
                    print("今日剩余学习时间30分钟，请重新选择")
                    print("")
                    self.flag = False

    def main_program(self):
        if self.flag:
            self.start_learning()
            self.update_data()

    def start_learning(self):
        print("开始学习！")
        speech.say("los geht's")

        while round(time.time() - self.start_time) != self.total_time:
            # 这里可以加入一些语音互动
            pass

        speech.say("fertig!")
        print("学习完成！")

        if self.choice == "1":
            MainGame.attribute_list[1] += 0.25
            self.time_total_study += 0.5
        if self.choice == "2":
            MainGame.attribute_list[1] += 0.5
            self.time_total_study += 1

    def update_data(self):
        with open("./time_data_study.txt", "w+") as f:
            f.write(str(self.time_total_study) + '\n')


class Meditation:
    def __init__(self):
        self.start_time = time.time()

        self.minutes = 20

        self.timestamp = np.arange(self.minutes) + 1

    def main_program(self):
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

    def main_program(self):
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
    ML.main_game()
