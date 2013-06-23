""" Title: BasicSprite.py
    Purpose/Overview: Contains the BasicSprite Class, which extends the Sprite
    class given by PyGame. Provides the base initialization for other classes.
    Author: Lillian
"""


import pygame

class BasicSprite(pygame.sprite.Sprite):
    """ This provides the attributes and methods for the base class Sprite
        Inherits from the Pygame Sprite Class."""

    """ i.e. tree, barn, etc. """

    def __init__(self, scene, img, alpha=1):
        """ Initializes a basic sprite"""
        # We'll have to decide whether or not to include a screen as one of a
        # Basic sprite's attributes.
        pygame.sprite.Sprite.__init__(self)
        if alpha == 0:
            self.image = pygame.image.load(img).convert()
        else:
            self.image = pygame.image.load(img).convert_alpha()
        self.x = 0; self.dx = 0
        self.y = 0; self.dy = 0
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.img_name = img
        scene.SpriteList.add(self)

    def update(self):
        '''Updates location of sprite'''
        self.x += self.dx
        self.y += self.dy
        self.rect = self.image.get_rect(center = (self.x, self.y))
