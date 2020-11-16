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
        self.playBackgroundMusic1()

        # the three button on main scene
        self.button1 = None
        self.button2 = None
        self.button3 = None

        # setting button list
        self.setting_button_list = None

        # set flag
        self.flag_list = ["open", "open", "open"]

    def mainGame(self):
        # main loop of game
        while True:
            # fill the window with whole black canvas
            # MainGame.window.fill(COLOR_BLACK)
            # wait for click to exit game
            self.startGame()
            # display selecting buttons on main scene
            self.displayMainSceneButton()
            # update display or we could not see anything
            pygame.display.update()

    # define a exit method of game
    def startGame(self):
        for event in pygame.event.get():
            # when click quit button, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # judge the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button1.collidepoint(pygame.mouse.get_pos()):
                    # only fill window once
                    MainGame.window.fill(COLOR_BLACK)
                    # we need to change the background music first
                    self.playBackgroundMusic2()
                    # enter sub-loop
                    while True:
                        self.quitGame()
                        pygame.display.update()
                        # we could add new elements here

                if self.button2.collidepoint(pygame.mouse.get_pos()):
                    MainGame.window.fill(COLOR_BLACK)
                    while True:
                        # add setting button
                        self.displaySettingButton(self.flag_list)
                        self.changeSettingButton()
                        pygame.display.update()
                        # we could have music setting, full screen display here or something else

                if self.button3.collidepoint(pygame.mouse.get_pos()):
                    while True:
                        self.exitGame()

    def quitGame(self):
        for event in pygame.event.get():
            # when click quit button, quit game
            if event.type == pygame.QUIT:
                self.exitGame()

    def exitGame(self):
        pygame.quit()
        # exit from python is very important
        sys.exit()

    def playBackgroundMusic1(self):
        # create Music instance
        m = Music(r"./musics/诛仙1-草原.mp3")
        # we need to give a parameter count here, but it has default value, so
        # we also could leave out it here
        m.playMusic()

    def playBackgroundMusic2(self):
        m = Music(r"./musics/逍遥传说.mp3")
        m.playMusic()

    def displayMainSceneButton(self):
        b = Button()
        self.button1, self.button2, self.button3 = b.displayMainSceneButton(200, 100)
        # debug
        # print(self.button1) # will get a rect object

    def displaySettingButton(self, flag_list):
        b = Button()
        self.setting_button_list = b.displaySettingButton(353, 100, flag_list)

    def changeSettingButton(self):
        for event in pygame.event.get():
            # when click quit button, quit game
            if event.type == pygame.QUIT:
                self.exitGame()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.setting_button_list[0].collidepoint(pygame.mouse.get_pos()):
                    if self.flag_list[0] == "open":
                        self.flag_list[0] = "close"
                        self.displaySettingButton(self.flag_list)
                    else:
                        self.flag_list[0] = "open"
                        self.displaySettingButton(self.flag_list)

                if self.setting_button_list[1].collidepoint(pygame.mouse.get_pos()):
                    if self.flag_list[1] == "open":
                        self.flag_list[1] = "close"
                        self.displaySettingButton(self.flag_list)
                    else:
                        self.flag_list[1] = "open"
                        self.displaySettingButton(self.flag_list)

                if self.setting_button_list[2].collidepoint(pygame.mouse.get_pos()):
                    if self.flag_list[2] == "open":
                        self.flag_list[2] = "close"
                        self.displaySettingButton(self.flag_list)
                    else:
                        self.flag_list[2] = "open"
                        self.displaySettingButton(self.flag_list)

                if self.setting_button_list[3].collidepoint(pygame.mouse.get_pos()):
                    break


class Music:
    def __init__(self, music):
        # use self.music store music we want to play
        self.music = music

        # this is not necessary, at the begining we initilaized all modules
        # pygame.mixer.init()

        # load music
        pygame.mixer.music.load(self.music)

    def playMusic(self, count=-1):
        # play background music in loop, for count = -1
        pygame.mixer.music.play(count)


class Button:
    def __init__(self):
        self.main_scene_images = {
            "title": pygame.image.load(r"./materials/游戏名称.png"),
            "start": pygame.image.load(r"./materials/开始游戏.png"),
            "setting": pygame.image.load(r"./materials/游戏设置.png"),
            "quit": pygame.image.load(r"./materials/退出游戏.png")
        }

        self.setting_images = {
            "open": pygame.image.load(r"./materials/打开状态.png"),
            "close": pygame.image.load(r"./materials/关闭状态.png"),
            "title": pygame.image.load(r"./materials/游戏设置分.png"),
            "music": pygame.image.load(r"./materials/背景音乐.png"),
            "key_press": pygame.image.load(r"./materials/按键音效.png"),
            "full_screen": pygame.image.load(r"./materials/全屏显示.png"),
            "return": pygame.image.load(r"./materials/返回主菜单.png")
        }

    def displayMainSceneButton(self, left, top):
        left1 = left + 180
        top1 = top + 220
        MainGame.window.blit(self.main_scene_images["title"], (left, top))
        button1 = MainGame.window.blit(self.main_scene_images["start"], (left1, top1))
        button2 = MainGame.window.blit(self.main_scene_images["setting"], (left1, top1 + 120))
        button3 = MainGame.window.blit(self.main_scene_images["quit"], (left1, top1 + 240))

        return button1, button2, button3

    def displaySettingButton(self, left, top, flag_list):
        # every time execute this part, clean setting_button_list first
        setting_button_list = []
        left1 = left + 30
        top1 = top + 200
        MainGame.window.blit(self.setting_images["title"], (left, top))
        MainGame.window.blit(self.setting_images["music"], (left1, top1))
        MainGame.window.blit(self.setting_images["key_press"], (left1, top1 + 100))
        MainGame.window.blit(self.setting_images["full_screen"], (left1, top1 + 200))
        button4 = MainGame.window.blit(self.setting_images["return"], (left1 + 60, top1 + 300))
        if flag_list[0] == "open":
            button1 = MainGame.window.blit(self.setting_images["open"], (left1 + 180, top1))
            setting_button_list.append(button1)
        if flag_list[0] == "close":
            button1 = MainGame.window.blit(self.setting_images["close"], (left1 + 180, top1))
            setting_button_list.append(button1)
        if flag_list[1] == "open":
            button2 = MainGame.window.blit(self.setting_images["open"], (left1 + 180, top1 + 100))
            setting_button_list.append(button2)
        if flag_list[1] == "close":
            button2 = MainGame.window.blit(self.setting_images["close"], (left1 + 180, top1 + 100))
            setting_button_list.append(button2)
        if flag_list[2] == "open":
            button3 = MainGame.window.blit(self.setting_images["open"], (left1 + 180, top1 + 200))
            setting_button_list.append(button3)
        if flag_list[2] == "close":
            button3 = MainGame.window.blit(self.setting_images["close"], (left1 + 180, top1 + 200))
            setting_button_list.append(button3)

        setting_button_list.append(button4)

        return setting_button_list


# execute program
if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
