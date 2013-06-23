import pygame
"""Title: Animation.py
   Purpose: To play the beginning animation and associated sounds within the
   game screen at the beginning of the game
   Author: Lillian
"""

from pygame.locals import *
import os
from Engine import Scene

class IntroAnim():
    '''Animation: intro to the game before it starts'''
    def __init__(self):
        '''Initiates the intro animation instance'''
        print 'Initializing Game...'
        self.__frames = []
        pygame.display.init()
        self.__screen = pygame.display.set_mode((640,480))
        for i in range(423):
            zeros = 4-len(str(i+1))
            num = zeros * '0' + str(i+1)
            path = 'data/anim/BeginningAnim'+num+'.jpg'
            img = pygame.image.load(path).convert()
            self.__frames.append(img)
        self.AudioMaster()
        self.__running = True

    def AudioMaster(self):
        '''Sets the audio for the animation'''
        pygame.mixer.init(44100, -16, 2, 100)
        self.__laugh = pygame.mixer.Sound('data/anim/evillaugh.ogg')
        self.__hey = pygame.mixer.Sound('data/anim/hey.ogg')

    def play(self):
        '''Plays the animation'''
        i = 0
        while self.__running == True:
            if i < len(self.__frames):
                if i == 205:
                    self.__laugh.play()
                if i == 305:
                    self.__hey.play()
                self.__screen.blit(self.__frames[i], (0,0))
                pygame.display.update()
                pygame.time.wait(40)
                self.__events()
                i += 1
            else:
                self.__running == False
                return
        pygame.mixer.quit()
        
    def __events(self):
        '''If player presses escape or return while the animation is playing,
        the animation ends'''
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.__running = False
                if event.key == QUIT:
                    self.__running = False
                if event.key == K_RETURN:
                    self.__running = False

### -- Debugging code -- ###
if __name__ == "__main__":
    pygame.init()
    x = IntroAnim()
    x.play()
