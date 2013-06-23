"""Title: make_world_map.py
    Purpose: To make the different maps that show a player's progression through
            the game.
    Authors: Vidie, Sam, Mandy
"""    

from Engine import WorldMap
from make_explores import make_car_explore, make_plane_explore
from make_explores import make_rocket_explore
from make_trophy_room import make_trophy_room
from functions import populate

def make_world_map(character, img):
    '''Detects which map stage you are at and produces next explore scene.'''
    s = WorldMap(img)
    world = s.main_loop()
    if world:
        if img == 'data/WorldMap1.png':
            return make_car_explore(character)
        elif img == 'data/WorldMap2.png':
            return make_plane_explore(character)
        elif img == 'data/WorldMap3.png':
            return make_rocket_explore(character)
        elif img == 'data/Trophy_Background.png':
            return make_trophy_room()
    return False
    
