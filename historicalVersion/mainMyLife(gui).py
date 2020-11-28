# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:29:04 2020

@author: 15025

main program of game---My Life

this structure only suits simple program. It is not useful to do so
"""

import pygame
import sys
import os
import time
import speech
import numpy as np

version = 'v1.05'
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


class MainGame:
    # the size of game window
    __SCREEN_WIDTH = 1000
    __SCREEN_HEIGHT = 800

    window = None

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
        time_list = [time.strftime("%Y", local_time), time.strftime("%m", local_time),
                     time.strftime("%d", local_time)]
    else:
        with open(".time_data_today", "r") as f:
            time_data_list = f.readlines()
            new_data_list = []
            for data in user_data_list:
                new_data_list.append(int(data.rstrip()))
            time_list = new_data_list

    def __init__(self):
        # to make the main windows be opened always at the center of screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # initialize modules of pygame
        pygame.init()
        # set window size of game
        MainGame.window = pygame.display.set_mode([MainGame.__SCREEN_WIDTH, MainGame.__SCREEN_HEIGHT])
        # set caption of window
        pygame.display.set_caption('My Life ' + version)
        # play background music
        MainGame.playBackgroundMusic1()

        self.image_directory = ["./dataBase/mainInterface.csv", "./dataBase/settingInterface.csv",
                                "./dataBase/gameScene1.csv", "./dataBase/gameScene2.csv", "./dataBase/attribute.csv"]

        self.button_list = []
        self.button_list_setting = []
        self.g1_button = []
        self.g2_button = []
        self.flag = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]

    def mainGame(self):
        # main loop of game
        main_flag = True
        start_flag = False
        setting_flag = False
        while True:
            if main_flag:
                self.displayMainInterface()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_list[0].collidepoint(pygame.mouse.get_pos()):
                            main_flag = False
                            start_flag = True
                            MainGame.window.fill(COLOR_BLACK)

                        if self.button_list[1].collidepoint(pygame.mouse.get_pos()):
                            main_flag = False
                            setting_flag = True
                            MainGame.window.fill(COLOR_BLACK)

                        if self.button_list[2].collidepoint(pygame.mouse.get_pos()):
                            MainGame.exitGame()
                pygame.display.update()

            if start_flag:
                self.displayGameScene1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.g1_button[0].collidepoint(pygame.mouse.get_pos()):
                            j = Jogging()
                            j.main_program()

                        if self.g1_button[1].collidepoint(pygame.mouse.get_pos()):
                            m = Meditation()
                            m.main_program()

                        if self.g1_button[2].collidepoint(pygame.mouse.get_pos()):
                            c = Cleaning()
                            c.main_program()

                        if self.g1_button[3].collidepoint(pygame.mouse.get_pos()):
                            self.display_data()  # 存在问题！

                        if self.g1_button[4].collidepoint(pygame.mouse.get_pos()):
                            s = Study(1)
                            s.main_program()

                        if self.g1_button[5].collidepoint(pygame.mouse.get_pos()):
                            s = Study(2)
                            s.main_program()

                pygame.display.update()

            if setting_flag:
                self.displaySettingInterface()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.button_list_setting[0].collidepoint(pygame.mouse.get_pos()):
                            self.flag[4], self.flag[5] = self.flag[5], self.flag[4]

                        if self.button_list_setting[1].collidepoint(pygame.mouse.get_pos()):
                            self.flag[6], self.flag[7] = self.flag[7], self.flag[6]

                        if self.button_list_setting[2].collidepoint(pygame.mouse.get_pos()):
                            self.flag[8], self.flag[9] = self.flag[9], self.flag[8]

                        if self.button_list_setting[3].collidepoint(pygame.mouse.get_pos()):
                            setting_flag = False
                            main_flag = True
                            MainGame.window.fill(COLOR_BLACK)

                pygame.display.update()

    def displayMainInterface(self):
        s = Scene(self.image_directory[0])
        self.button_list = s.displayMainScene()

    def displaySettingInterface(self):
        s = Scene(self.image_directory[1])
        self.button_list_setting = s.displaySettingScene(self.flag)

    def displayGameScene1(self):
        s = Scene(self.image_directory[2])
        self.g1_button = s.displayGame1()

    def displayGameScene2(self):
        s = Scene(self.image_directory[3])
        self.g2_button = s.displayGame1()

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
            # when click quit button, quit game
            if event.type == pygame.QUIT:
                MainGame.exitGame()

    @staticmethod
    def exitGame():
        pygame.quit()
        # exit from python is very important
        sys.exit()

    @staticmethod
    def playBackgroundMusic1():
        # create Music instance
        m = Music(r"./musics/诛仙1-草原.mp3")
        # we need to give a parameter count here, but it has default value, so
        # we also could leave out it here
        m.playMusic()

    @staticmethod
    def playBackgroundMusic2():
        m = Music(r"./musics/逍遥传说.mp3")
        m.playMusic()

    def display_data(self):
        s = Scene(self.image_directory[4])
        s.displayGame1()
        with open("./user_data.txt", "r") as f:
            content = f.readlines()
            new_data_list = []
            for data_list in content:
                new_data_list.append(data_list.rstrip())

        font = pygame.font.SysFont('fangsong', 30)
        text_health = font.render(new_data_list[0], True, COLOR_WHITE)
        text_mental = font.render(new_data_list[1], True, COLOR_WHITE)
        text_academy = font.render(new_data_list[2], True, COLOR_WHITE)
        text_cleaning = font.render(new_data_list[3], True, COLOR_WHITE)
        MainGame.window.blit(text_health, (290, 656))
        MainGame.window.blit(text_mental, (290, 707))
        MainGame.window.blit(text_academy, (570, 656))
        MainGame.window.blit(text_cleaning, (570, 707))


class Music:
    def __init__(self, music):
        self.music = music

        pygame.mixer.music.load(self.music)

    @staticmethod
    def playMusic(count=-1):
        # play background music in loop, for count = -1
        pygame.mixer.music.play(count)


class Scene:
    def __init__(self, directory):
        self.main_scene_name = []
        self.main_scene_type = []
        self.main_scene_directory = []
        self.main_scene_left = []
        self.main_scene_top = []
        with open(directory, "r") as f:
            all_data = f.readlines()
            for data_list in all_data[1:]:
                new_list = data_list.rstrip().split(",")
                self.main_scene_name.append(new_list[0])
                self.main_scene_type.append(new_list[1])
                self.main_scene_directory.append(new_list[2])
                self.main_scene_left.append(int(new_list[3]))
                self.main_scene_top.append(int(new_list[4]))

    def displayMainScene(self):
        button_list = []
        for i in range(len(self.main_scene_name)):
            if self.main_scene_type[i] == "image":
                image = pygame.image.load(self.main_scene_directory[i])
                MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
            else:
                image = pygame.image.load(self.main_scene_directory[i])
                button = MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
                button_list.append(button)

        return button_list

    def displaySettingScene(self, flag):
        button_list = []
        for i in range(len(self.main_scene_name)):
            if self.main_scene_type[i] == "image":
                image = pygame.image.load(self.main_scene_directory[i])
                MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))

            if self.main_scene_type[i] == "button_open" and flag[i] == 1:
                image = pygame.image.load(self.main_scene_directory[i])
                button = MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
                button_list.append(button)

            if self.main_scene_type[i] == "button_close" and flag[i] == 1:
                image = pygame.image.load(self.main_scene_directory[i])
                button = MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
                button_list.append(button)

            if self.main_scene_type[i] == "button":
                image = pygame.image.load(self.main_scene_directory[i])
                button = MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
                button_list.append(button)

        return button_list

    # the scene after we click start game
    def displayGame1(self):
        button_list = []
        for i in range(len(self.main_scene_name)):
            if self.main_scene_type[i] == "image":
                image = pygame.image.load(self.main_scene_directory[i])
                MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
            else:
                image = pygame.image.load(self.main_scene_directory[i])
                button = MainGame.window.blit(image, (self.main_scene_left[i], self.main_scene_top[i]))
                button_list.append(button)

        return button_list


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
                Jogging.quitGame()

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

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class Study:
    def __init__(self, choice):
        while True:
            self.choice = choice
            if self.choice == 1:
                self.total_time = 30 * 60
                # print("开始30分钟学习")
                break
            elif self.choice == 2:
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
            Study.quitGame()
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

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


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
                Meditation.quitGame()

                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    print(f"已经过去了{i + 1}分钟")
                    break

        speech.say("Fertig!")
        print("冥想结束!")

        MainGame.attribute_list[2] += 1

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


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
                Cleaning.quitGame()

                if round(time.time() - self.start_time) == self.timestamp[i] * 60:
                    print(f"已经过去了{i + 1}分钟")
                    break

        speech.say("Fertig!")
        print("清洁结束!")

        MainGame.attribute_list[3] += 1

    @staticmethod
    def quitGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


# execute program
if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
