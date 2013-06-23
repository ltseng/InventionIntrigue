"""Title: Start.py
    Purpose: To run the game from beginning to end
    Author: Lillian
"""

import pygame
from animation import IntroAnim
from Engine import MainMenu,CharSelect
from make_world_map import make_world_map
from make_trophy_room import make_trophy_room

def main():
    pygame.init()
    A = IntroAnim()
    A.play()
    s = MainMenu()
    #change 2nd value to change speed (high slower)
    pygame.key.set_repeat(300,100)
    mainloop = s.main_loop()
    if not mainloop:
        pass
    s = CharSelect()
    character = s.main_loop()
    if not character:
        return
    else:
        x = make_world_map(character,'data/WorldMap1.png')
        if not x:
            return
        x = make_world_map(character,'data/WorldMap2.png')
        if not x:
            return
        x = make_world_map(character,'data/WorldMap3.png')
        if not x:
            return
        x = make_trophy_room()
        if not x:
            return

if __name__ == "__main__":
    main()
