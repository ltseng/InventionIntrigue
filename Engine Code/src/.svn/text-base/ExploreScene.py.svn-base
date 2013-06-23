""" Title: ExploreScene.py
    Purpose: Extends the Scene class in Engine.py to include an inventory
    at the bottom of the screen.
    Author: Lillian
"""

from Engine import Scene
from Inventory import Inventory


class ExploreScene(Scene):
    """ Creates a scene in which the Actor can move around and interact
        with other things"""
    def __init__(self,img):
        '''Initiates ExploreScene'''
        Scene.__init__(self,img)
        self.inventory = Inventory(self)
        self.SpriteList.add()
