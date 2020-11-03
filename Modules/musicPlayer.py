# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:32:14 2020

@author: 15025
"""

import pygame
import os
import time
import random
import numpy
import sys


# initialize pygame
pygame.init()

# pygame.mixer.init()

# the music directory
music_path = r'C:/Users/15025/Desktop/music/'

# get all musics under this music directory
music = os.listdir(music_path)

# set the size of interface
pygame.display.set_mode([300,300])

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    if pygame.mixer.music.get_busy() == False:
        order = random.randint(0, len(music) - 1)
        
        os.chdir(music_path)
        
        pygame.mixer.music.load(music[order])
        # play music
        pygame.mixer.music.play()
