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

version = 'v1.04'
COLOR_BLACK = (0, 0, 0)


class MainGame:
    # the size of game window
    __SCREEN_WIDTH = 1000
    __SCREEN_HEIGHT = 800

    window = None

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

        self.image_directory = ["./dataBase/mainInterface.csv", "./dataBase/settingInterface.csv"]

        self.button_list = []
        self.button_list_setting = []
        self.flag = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]

    def mainGame(self):
        # main loop of game
        while True:
            self.displayMainInterface()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_list[0].collidepoint(pygame.mouse.get_pos()):
                        MainGame.window.fill(COLOR_BLACK)
                        MainGame.playBackgroundMusic2()
                        while True:
                            MainGame.quitGame()
                            pygame.display.update()

                    if self.button_list[1].collidepoint(pygame.mouse.get_pos()):
                        MainGame.window.fill(COLOR_BLACK)
                        flag = True
                        while flag:
                            for event1 in pygame.event.get():
                                if event1.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event1.type == pygame.MOUSEBUTTONDOWN:
                                    if self.button_list_setting[3].collidepoint(pygame.mouse.get_pos()):
                                        flag = False
                            self.displaySettingInterface()
                            pygame.display.update()

                    if self.button_list[2].collidepoint(pygame.mouse.get_pos()):
                        MainGame.exitGame()

            pygame.display.update()

    def getEvent(self):
        pass

    def displayMainInterface(self):
        s = Scene(self.image_directory[0])
        self.button_list = s.displayMainScene()

    def displaySettingInterface(self):
        s = Scene(self.image_directory[1])
        self.button_list_setting = s.displaySettingScene(self.flag)

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


class Music:
    def __init__(self, music):
        # use self.music store music we want to play
        self.music = music

        # this is not necessary, at the beginning we initialized all modules
        # pygame.mixer.init()

        # load music
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


class Button:
    def __init__(self):
        pass


# execute program
if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
