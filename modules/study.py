# -*- coding: utf-8 -*-

import os
import time
import speech


class Study:
    def __init__(self):
        while True:
            print("请您选择，提示：请输入序号1或者2")
            print("1. 学习30分钟")
            print("2. 学习60分钟")
            self.choice = input("您的决定: ")
            print("")
            if self.choice == "1":
                self.total_time = 3
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
            self.time_total_study += 8
        if self.choice == "2":
            self.time_total_study += 1

    def update_data(self):
        with open("./time_data_study.txt", "w+") as f:
            f.write(str(self.time_total_study) + '\n')


if __name__ == "__main__":
    # ML: My Life
    s = Study()
    s.main_program()