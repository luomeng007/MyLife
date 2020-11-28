# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:29:04 2020

@author: 15025

main program of game---My Life
"""

import pygame
import sys


version = 'v1.00'


class MainGame:
    # the size of game window
    __SCREEN_WIDTH = 1000
    __SCREEN_HEIGHT = 800
    window = None

    def __init__(self):
        # initialize modules of pygame
        pygame.init()
        # set window size of game
        MainGame.window = pygame.display.set_mode([MainGame.__SCREEN_WIDTH, MainGame.__SCREEN_HEIGHT])
        # set caption of window
        pygame.display.set_caption('My Life ' + version)
        # play background music
        self.playaBackgroundMusic()

    def mainGame(self):
        # main loop of game
        while True:
            # wait for click game
            self.exitGame()

    @staticmethod
    # define a exit method of game
    def exitGame():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def playaBackgroundMusic():
        # create Music instance
        m = Music(r"C:/Users/15025/Desktop/MyLife/musics/逍遥传说.mp3")
        # we need to give a parameter count here, but it has default value, so 
        # we also could leave out it here
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


# execute program
if __name__ == "__main__":
    # ML for My Life
    game_ML = MainGame()
    game_ML.mainGame()
