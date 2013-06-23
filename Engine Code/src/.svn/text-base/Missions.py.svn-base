""" Title: Missions.py
    Purpose: To provide information about the puzzles and display the results
            screen. Also handles the events for some puzzles and updates
            the global trophies list.
    Authors: Sam, Vidie, Mandy
"""

import pygame
from pygame.locals import *
from BasicSprite import BasicSprite
from Puzzles import Puzzle, CarPuzzle, PlanePuzzle, RocketPuzzle, Car, Flag
from Engine import trophies, MissionScene
from functions import add_inventory


#-----------------------------------------------------------#
#           Puzzle creator functions                        #
#-----------------------------------------------------------#

def car_puzzle():
    """Creates the car puzzle"""
    keep_playing = True
    
    mission_img = 'data/Car/car_background.png'
    opening = MissionScene(mission_img, (0,0,0))
    opening.mission_text = ['Get fifteen flags to complete the puzzle',
                            'but do not go off the screen.',
                            'The puzzle is timed: a better time means '
                            + 'a better score',
                            'Time will start once you press Enter']
    keep_playing = opening.main_loop()
    
    if not keep_playing:
        return False

    while True:
        car_pz = CarPuzzle()
        car = Car(car_pz)
        end = car_pz.main_loop(car)
        
        if type(end) == tuple:
            if end[1]:
                break
        else:
            return False
        
        failed = MissionScene(mission_img, (0,0,0))
        failed.mission_text = ["It's okay, you can try again.",
                               "Just press Enter.", "", ""]
        keep_playing = failed.main_loop()

        if not keep_playing:
            return False
        
    if end[0] < 35:
        trophies.append('gold')
    elif 35 <= end[0] < 50:
        trophies.append('silver')
    else:
        trophies.append('bronze')
        
    won = MissionScene(mission_img, (0,0,0))
    won.mission_text = ["Yay! Well done!",
                        'You stopped the villain from sabotaging my car!',
                        'You finished in ' + str(end[0]) + ' seconds,',
                        'and your trophy is ' + trophies[0] + '!',]
    won.main_loop()
    return True

def plane_puzzle():
    '''Creates the scene for the plane puzzle'''
##    global trophies
    img = 'data/Plane/Biplane.png'
    pz = PlanePuzzle(img)
    
    wing = BasicSprite(pz, 'data/Plane/Wings.png')
    add_inventory(pz, wing, 100, 150)
    
    elevators = BasicSprite(pz, 'data/Plane/Elevator.png') 
    add_inventory(pz, elevators, 65, 400)
    
    engine = BasicSprite(pz, 'data/Plane/Engines_small.png')
    add_inventory(pz, engine, 605, 420)
    
    engine2 = BasicSprite(pz, 'data/Plane/Engines_small.png')
    add_inventory(pz, engine2, 530, 450)
    
    fuselage = BasicSprite(pz, 'data/Plane/Fuselage.png')
    add_inventory(pz, fuselage, 460,365)
    
    propeller = BasicSprite(pz, 'data/Plane/Propeller.png')
    add_inventory(pz, propeller, 495, 210)
    
    rudder = BasicSprite(pz, 'data/Plane/Rudder.png')
    add_inventory(pz, rudder, 620, 120)
    
    end = pz.main_loop()
    if end[0] < 30:
        trophies.append('gold')
    elif 30 <= end[0] < 40:
        trophies.append('silver')
    else:
        trophies.append('bronze')
        
    if pz.complete:
        won = MissionScene('data/Plane/Biplane_pretty.png', (0,0,0))
        won.mission_text = ['Congratulations! You completed the second puzzle.',
                            'Thank you for helping us beat the villain!',
                            'Your time was ' + str(end[0]) + ' seconds,',
                            ' and your trophy is ' + trophies[1] + '!']
        won.main_loop()
        return True

def rocket_puzzle():
    '''Creates the scene for the rocket puzzle'''
    info_img = 'data/Rocket/Rocket_Info.png'
    info = MissionScene(info_img, (0,0,0))
    info.mission_text = ['Using the keyboard,',
                         'press the number of the button',
                         'in the correct order',
                         'to get the shuttle in orbit.',
                         "Then, hit Enter."]
    info.main_loop()
    pz_img = 'data/Rocket/Rocket_Puzzle.png'
    pz = RocketPuzzle(pz_img)    
    rocket_counter = pz.main_loop()

    if rocket_counter < 4:
        trophies.append('gold')
    elif 4 <= rocket_counter < 10:
        trophies.append('silver')
    else:
        trophies.append('bronze')

    
    if pz.complete:
        won = MissionScene(info_img, (0,0,0))
        won.mission_text = ['Congrats!',
                            'You completed the game',
                            'in only ' + str(rocket_counter) + ' attempts.',
                            'Your trophy is ' + trophies[2] + '!']
        won.mission_text = ['Congrats, you completed the game!',
                            'The villian is defeated forever!!!',
                            'You only took ' + str(rocket_counter) + ' attempts.',
                            'Your trophy is ' + trophies[2] + '!']
        won.main_loop()
        return True


