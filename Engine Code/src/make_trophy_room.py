
""" Title: make_trophy_room.py

    Purpose/Overview: Creates the Trophy Room at the end of the game.

    Author: Lillian

"""

from Engine import TrophyScene, trophies, IntObj
from functions import populate


def make_trophy_room():
    '''Makes the trophy room where the user can play with the inventions.'''
    global trophies
    s = TrophyScene()
    coords = [(175, 325), (325, 325),(470, 325)]

    
    # get the color of the trophy from the global trophies list,
    # to which the trophy colors were added when each puzzle was completed,
    # then place the three trophies in the final trophy scene
    for i in range(3):
        trophy = IntObj(s, 'data/'+trophies[i]+'_trophy.png',1)
        populate(s, trophy, coords[i][0], coords[i][1])
        s.trophy_list.append(trophy)

    x = s.main_loop()
    if x:
        exit()
        
