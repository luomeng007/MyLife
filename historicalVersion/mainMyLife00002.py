# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:29:04 2020

@author: 15025

main program of game---My Life
"""

import pygame
import sys
import os

version = 'v1.02'
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
        self.playaBackgroundMusic()

        # the three button on main scene
        self.button1 = None
        self.button2 = None
        self.button3 = None

    def mainGame(self):
        # main loop of game
        while True:
            # fill the window with whole black canvas
            # MainGame.window.fill(COLOR_BLACK)
            # wait for click to exit game
            self.startGame()
            # display selecting buttons on main scene
            self.displayButton()
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
                    print(pygame.mouse.get_pos())
                    # enter sub-loop
                    while True:
                        MainGame.window.fill(COLOR_BLACK)
                        self.quitGame()
                        pygame.display.update()
                        # we could add new elements here

                if self.button2.collidepoint(pygame.mouse.get_pos()):
                    while True:
                        MainGame.window.fill(COLOR_BLACK)
                        self.quitGame()
                        pygame.display.update()

                if self.button3.collidepoint(pygame.mouse.get_pos()):
                    while True:
                        MainGame.window.fill(COLOR_BLACK)
                        self.quitGame()
                        pygame.display.update()

    def quitGame(self):
        for event in pygame.event.get():
            # when click quit button, quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def playaBackgroundMusic(self):
        # create Music instance
        m = Music(r"D:/User(origin in C)/desktop/MyLife_main/musics/诛仙1-草原.mp3")
        # we need to give a parameter count here, but it has default value, so
        # we also could leave out it here
        m.playMusic()

    def displayButton(self):
        b = Button(200, 100)
        self.button1, self.button2, self.button3 = b.displayButton()
        # debug
        # print(self.button1)


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
    def __init__(self, left, top):
        self.images = {
            "title": pygame.image.load(r"D:\User(origin in C)\desktop\MyLife_main\materials/游戏名称.png"),
            "start": pygame.image.load(r"D:\User(origin in C)\desktop\MyLife_main\materials/开始游戏.png"),
            "setting": pygame.image.load(r"D:\User(origin in C)\desktop\MyLife_main\materials/游戏设置.png"),
            "quit": pygame.image.load(r"D:\User(origin in C)\desktop\MyLife_main\materials/退出游戏.png")
        }

        self.left = left
        self.top = top

        self.left1 = left + 180
        self.top1 = top + 220

    def displayButton(self):
        MainGame.window.blit(self.images["title"], (self.left, self.top))
        button1 = MainGame.window.blit(self.images["start"], (self.left1, self.top1))
        button2 = MainGame.window.blit(self.images["setting"], (self.left1, self.top1 + 120))
        button3 = MainGame.window.blit(self.images["quit"], (self.left1, self.top1 + 240))

        return button1, button2, button3


# execute program
if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
