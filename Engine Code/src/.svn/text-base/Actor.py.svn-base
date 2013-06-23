# Actor class for Engine.py
import pygame
from BasicSprite import BasicSprite
from pygame.locals import *

class Actor(BasicSprite):
    """ Controllable Character """
    """ i.e. You! """

    def __init__(self, scene, img):
        '''Inherits from BasicSprite, adds actor to Actor group of scene'''
        BasicSprite.__init__(self, scene, img)
        scene.Actor.add(self)

    def update(self, Actor, event, scene):
        '''Updates location of Actor'''
        self.movement(event)
        self.boundary(scene)
        self.x += self.dx
        self.y += self.dy
        self.rect = self.image.get_rect(center = (self.x, self.y))

        
    def movement(self, event):
        '''Controls a sprite's movement depending on arrow of keyboards'''

        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.dx = 0
                self.dy = -10
            elif event.key == K_DOWN:
                self.dx = 0
                self.dy = 10
            elif event.key == K_LEFT:
                self.dx = -10
                self.dy = 0
            elif event.key == K_RIGHT:
                self.dx = 10
                self.dy = 0
            else:
                self.dx = 0
                self.dy = 0

    def boundary(self, scene):
        '''Keeps actor from moving out of the screen'''
        scrWidth = scene.screen.get_width()
        scrHeight = scene.screen.get_height()
        if self.x > scrWidth:
            self.x = scrWidth
        if self.x < 0:
            self.x = 0
        if self.y > scrHeight-125:
            self.y = scrHeight-125
        if self.y < 0:
            self.y = 0

