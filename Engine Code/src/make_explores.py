""" Title: make_explores.py

    Purpose: Creates explore scenes for each level.
    
    Overview: Contains functions that create the explore scenes
              and populate them with sprites.
              
    Authors: Mandy, Sam and Vidie

    Changes: 29 Nov [SPB] Populated make_rocket_explore with rocket
                          button interactive objects.

"""

from Engine import NPC, IntObj, Actor
from ExploreScene import ExploreScene
from functions import populate, add_inventory
from Missions import car_puzzle, plane_puzzle, rocket_puzzle


def make_car_explore(character):
    '''Makes the car explore scene of the game.'''
    s = ExploreScene('data/Explore_Ford.png')
    
    # Create car Sprites, Ford NPC, and actor    
    wheel = IntObj(s,'data/Car/wheels.png',1)
    axle = IntObj(s,'data/Car/axle.png')
    windshield = IntObj(s,'data/Car/windshield.png')
    bolts = IntObj(s,'data/Car/bolts.png',1)
    engine = IntObj(s,'data/Car/engine.png',1)
    body = IntObj(s,'data/Car/body.png',1)
    seat = IntObj(s,'data/Car/seat.png',1)
    steering_wheel = IntObj(s,'data/Car/steering.png',1)
    Ford = NPC(s,'data/FordNPC.png',1)
    player = Actor(s,character)

    # Add car Sprites, Ford NPC, and actor to Scene SpriteList 
    populate(s, wheel, 200, 300)
    populate(s, axle, 300, 100)
    populate(s, windshield, 300, 300)
    populate(s,bolts, 200, 200)
    populate(s,engine, 500, 100)
    populate(s,body, 500, 200)
    populate(s,seat, 500, 300)
    populate(s,steering_wheel, 500, 400)
    populate(s,Ford, 100, 200)
    populate(s, player, 200, 100)
    
    puzzle = s.main_loop()
    if puzzle:
        if car_puzzle():
            return True
            
def make_plane_explore(character):
    """Makes the plane explore scene of the game. Woohoo!"""
    s = ExploreScene('data/Explore_Wright.jpg')
    
    # Create plane Sprites, Wright brothers NPC, and actor    
    b = IntObj(s,'data/Plane/Elevator_small.png',1)
    c = IntObj(s,'data/Plane/Engines_small.png',1)
    d = Actor(s,character)
    e = NPC(s,'data/Wright_Brothers.png', 1)
    f = IntObj(s,'data/Plane/Fuselage_small.png',1)
    g = IntObj(s,'data/Plane/Propeller_small.png',1)
    h = IntObj(s,'data/Plane/Rudder_small.png',1)
    i = IntObj(s,'data/Plane/Wings_small.png',1)
    j = IntObj(s,'data/Plane/Wings_small_2.png',1)
    k = IntObj(s,'data/Plane/Engines_small.png',1)
    
    # Add plane Sprites, Wright brothers  NPC, and actor to Scene SpriteList 
    populate(s, b, 470, 350)
    populate(s, k, 45, 360)
    populate(s, c, 345, 105)
    populate(s, f, 605, 345)
    populate(s, g, 495, 210)
    populate(s, h, 620, 120)
    populate(s, i, 50, 210)
    populate(s, j, 340, 365)
    populate(s, e, 200, 165)
    populate(s, d, 380, 210)
    
    puzzle = s.main_loop()
    if puzzle:
        if plane_puzzle():
            return True

def make_rocket_explore(character):
    '''Makes the rocket explore scene of the game.'''
    s = ExploreScene('data/Explore_Rocket.png')
    
    # Create rocket Sprites, rocket scientist NPC, and actor    
    b1 = IntObj(s, 'data/Rocket/button.png')
    b2 = IntObj(s, 'data/Rocket/button.png')
    b3 = IntObj(s, 'data/Rocket/button.png')
    b4 = IntObj(s, 'data/Rocket/button.png')
    b5 = IntObj(s, 'data/Rocket/button.png')
    b6 = IntObj(s, 'data/Rocket/button.png')
    b7 = IntObj(s, 'data/Rocket/button.png')
    b8 = IntObj(s, 'data/Rocket/button.png')
    scientist = NPC(s,'data/Scientist.png', 1)
    player = Actor(s, character)

    # Add rocket Sprites, rocket scientist  NPC, and actor to Scene SpriteList 
    populate(s, b2, 270, 340)   #behind person
    populate(s, b1, 300, 300)
    populate(s, b3, 560, 350)
    populate(s, b4, 400, 375)
    populate(s, b5, 450, 275)
    populate(s, b6, 530, 315)
    populate(s, b7, 180, 365)
    populate(s, b8, 100, 340)
    populate(s,scientist, 500, 175)
    populate(s, player, 350, 300)
    
    puzzle = s.main_loop()
    if puzzle:
        if rocket_puzzle():
            return True

