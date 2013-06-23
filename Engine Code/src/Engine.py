""" Title: Engine.py

    Purpose: Game engine; provides methods for sprite initialization
    
    Overview: Contains super and subclasses for sprites and scenes

    Authors: Lillian, Mandy, Sam, and Vidie

    Changes: 16 Nov [MBK] Changed mainLoop of Scene class so that inventory
             items are placed in the correct locations.
             16 Nov [SPB] NPC update now calls correct mission scene by matching
             each NPC to a mission scene.
             17 Nov [MBK, SPB, LT] Renamed explore, puzzle, and mission scenes.
             17 Nov [MBK] Fixed cheat code for mainLoop of Puzzle
             17 Nov [LT] Changed MainMenu to have three MenuLink options
             17 Nov [VP] Standardizing all class names to camel naming and all
                 functions and methods to underscore naming
                 (e.g. CamelNaming vs Underscore_Naming)
             17 Nov [SPB] Changed image path in plane explore scene and fixed
                 invocation of CarPuzzle class in car_puzzle function to agree
                 with CamelNaming
             19 Nov [MBK] Created PlanePuzzle scene; removed hangar images
             21 Nov [MBK] Fixed inventory bug; x & y set in Int_Obj, not Scene
                          Wright bros. image bug fixed: calls mission scene now
                          Wrote add_inventory function and PlanePuzzle
                          Changed do_something in Class Int_Obj and added info
                          mission scenes
            23 Nov [SPB] Separated explore scene creator functions into separate
                file: make_explores.py.
                Added section comment blocks to help separate file.
            24 Nov [VP] Changed MissionScene so that it outputs True when the
                text is done and False when the player quits the game.
                Added random module to the imports.
                Added classes: Car, Flag, and CarPuzzle
                Added function: car_puzzle()
                Deleted the copy of this opening text that came after the
                imports because they said the exact same thing.
                Deleted the imports that came after deleted text, because
                they are also the same thing as the imports that came after
                this text, except less.
                NOTE: there is now an error: 'make_plane_explore' is not
                defined. Edited NPC's text in function car_mission.
                Added Car Information.
            24 Nov [MBK] Fixed import error, so make_plane_explore works
            24 Nov [VP] Deleted the extra input to TrophyScene.__init__ in
                make_.
                Edited the winning car_puzzle text so that it tells you your
                time after you complete the puzzle.
            24 Nov [SPB] Changed mission text for rocket mission scene.
            25 Nov [LT] Initialized beginning animation to play before the main
                menu. Also updated the credits scene link in the Main Menu.
                Also created the trophy scene. Also implemented the 3D object
                visualization. Everyone will need to install Panda3D to view
                them, but it's no big deal if you don't want to. The .exe file
                is in the data/installation folder.
            25 Nov [SPB] Created RocketPuzzle class, changed sprites in rocket_
                puzzle scene, so there are none.
            26 Nov [SPB] Modified RocketPuzzle to fix the bug of pressing in
                the correct order, but not starting with the 0th element as the
                first button.
                Also, fixed bug where incorrectly pressing a button did not
                reset order to zero correct.
            27 Nov [LT] Put the car images in the Explore_Car scene. Also
                changed the explore scenes to incorporate the girl and boy
                characters. Also modified the animation to incorporate the
                subprocess module instead of the os module
            28 Nov [VP] Editted CarPuzzle such that you now have to get 15
                flags, and the car speeds up after every five flag
            29 Nov [SPB] Created counter variable in RocketPuzzle to keep track
                of the number of tries on the rocket puzzle.
                Added two mission scenes to rocket_puzzle that give instructions
                and how many tries it took to complete.
            29 Nov [MBK] Added mission scene to PlanePuzzle after winning.
                         Changed the position of text in MissionScene.
                         PlanePuzzle now keeps track of time.
                         Now after completing the plane puzzle, you get a grade.
            30 Nov [VP] Added the making of the info screens for each car item
                Added "car_" in front of all the car info functions and "plane_"
                in front of the plane info functions
            30 Nov [MBK] Scene mainloop now blits actor after everything else
            30 Nov [SPB] Made RocketPuzzle more modular by creating dictionary
                of key inputs and matching buttons. Added images of pressed
                buttons when correctly pushed to help player see if his/her
                order is correct.
            01 Dec [MBK] Made color an attribute of MissionScene __init__
                         Added global trophies list for puzzle rewards
                         Changed PlanePuzzle
            01 Dec [VP] Changed NPC so that when the actor interacts with it
                with an inventory of 8, it returns True, otherwise false.
                Changed Scene main_loop to return True if the NPC.update returns
                True, and deleted the PZ move to the puzzle.
                Created CreditScene class and changed MainMenu so that it calls
                CreditScene.
                Changed NPC text to say to come talk to them when inventory
                is full.
            01 Dec [LT] changed animation to play within the game screen instead
                of using VLC. Also split up BasicSprite, Actor, and Inventory
            02 Dec [SPB] Fixed bug in rocket counter.
                Added trophy to rocket puzzle.
            02 Dec [MBK] Edited mission text to include the villain
            09 Dec [LT] Split up the code, added __init__.py, and changed the
                header information for all the .py files. Cleaned up the code
                and removed unnecessary variable assignments. Removed leftover
                testing code.
    
"""
import pygame, sys, os
from BasicSprite import BasicSprite
from Actor import Actor
from Inventory import Inventory
from pygame.locals import *
import random
# Make a global trophies list that each puzzle will append a color to
global trophies
trophies = []


#-----------------------------------------------------------------------#
#                       Subclasses of Sprite                            #
#-----------------------------------------------------------------------# 

class NPC(BasicSprite):
    """ Controls Non-Player Character behavior """
    """ i.e. Wright Brothers, Ford """

    def __init__(self, scene, img, alpha=1):
        '''Inherits from BasicSprite, adds NPC to Sprite group'''
        BasicSprite.__init__(self, scene, img, alpha)

    def update(self, Actor, event, scene):
        """ For entering cutscene if actor approaches and has keyboard input"""
        self.rect = self.image.get_rect(center = (self.x, self.y))
        if self.check_bounds(Actor) and event.type == KEYDOWN and \
           event.key == K_RETURN:
            if self.img_name == 'data/Wright_Brothers.png':
                if len(scene.Inventory) == 8:
                    return True
                plane_mission()
                return False
            elif self.img_name == 'data/FordNPC.png':
                if len(scene.Inventory) == 8:
                    return True
                car_mission()
                return False
            elif self.img_name == 'data/Scientist.png':
                if len(scene.Inventory) == 8:
                    return True
                rocket_mission()
                return False
        return False

    def check_bounds(self, Actor):
        ''' Uses the PyGame Sprite class to return True when an actor is next
        to an NPC'''
        if len(pygame.sprite.spritecollide(self, Actor, 0)) >= 1:
            return True
        else:
            return False

class IntObj(BasicSprite):
    """ Controls interactive object behavior """
    """ i.e. Wings, random factory parts"""

    def __init__(self, scene, img, alpha=1):
        '''Inherits from BasicSprite, adds obj to Sprite group'''
        BasicSprite.__init__(self, scene, img, alpha)

    def update(self, Actor, event, scene):
        '''If spacebar pressed and check_Bounds is True, then IntObj. should
        "do something", die, and then blit itself onto the Inventory Scene'''
        self.rect = self.image.get_rect(center = (self.x, self.y))
        if self.check_bounds(Actor) and event.type == KEYDOWN and \
           event.key == K_RETURN:
            self.do_something(scene)
        
    def die(self, scene):
        """ Remove object from screen and add to Inventory screen when picked
        up"""
        scene.SpriteList.remove(self)
        index = len(scene.Inventory)
        self.x = index * 80 + 40
        self.y = scene.height - 40
        self.rect = self.image.get_rect(center = (self.x, self.y))
        scene.Inventory.add(self)

    def do_something(self, scene):
        '''Create new mission scene that has text information about the item,
        then calls die.'''
        if self.img_name == 'data/Car/wheels.png':
            car_wheel_info()
        elif self.img_name == 'data/Car/axle.png':
            car_axle_info()
        elif self.img_name == 'data/Car/windshield.png':
            car_windshield_info()
        elif self.img_name == 'data/Car/bolts.png':
            car_bolts_info()
        elif self.img_name == 'data/Car/engine.png':
            car_engine_info()
        elif self.img_name == 'data/Car/body.png':
            car_body_info()
        elif self.img_name == 'data/Car/seat.png':
            car_seat_info()
        elif self.img_name == 'data/Car/steering.png':
            car_steering_info()
            
        elif self.img_name == 'data/Plane/Wings_small.png':
            plane_wing_info()
        elif self.img_name == 'data/Plane/Wings_small_2.png':
            plane_wing_info_2()
        elif self.img_name == 'data/Plane/Engines_small.png':
            plane_engine_info()
        elif self.img_name == 'data/Plane/Elevator_small.png':
            plane_elevator_info()
        elif self.img_name == 'data/Plane/Fuselage_small.png':
            plane_fuselage_info()
        elif self.img_name == 'data/Plane/Propeller_small.png':
            plane_propeller_info()
        elif self.img_name == 'data/Plane/Rudder_small.png':
            plane_rudder_info()
        self.die(scene)

    def check_bounds(self, Actor):
        """ Return True when an actor is on top of IntObj """
        if len(pygame.sprite.spritecollide(self, Actor, 0)) >= 1:
            return True
        else:
            return False

#-----------------------------------------------------------------------#
#                  Scene class and subclasses of Scene                  #
#-----------------------------------------------------------------------#

class Scene(object):
    """ This provides the attributes and methods for the basic Scene class
        that will be the foundation for all scenes"""

    def __init__(self, img):
        """Initializes the scene screen and background image"""
        self.screen = pygame.display.set_mode((640, 480))
        pygame.mouse.set_visible(True)
        self.img = pygame.image.load(img).convert()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.SpriteList = pygame.sprite.Group()
        self.Actor = pygame.sprite.Group()
        self.Inventory = pygame.sprite.Group()
        self.keepgoing = True
        
        
    def main_loop(self):
        """ Controls the behavior of the objects in the scene """
        while self.keepgoing:
            self.screen.blit(self.img,(0,0))
            self.SpriteList.draw(self.screen)
            self.Actor.draw(self.screen)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.keepgoing = False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.keepgoing = False
                for sprite in self.SpriteList:
                    if isinstance(sprite, Actor) or isinstance(sprite, IntObj):
                        sprite.update(self.Actor, event, self)
                    elif isinstance(sprite,NPC):
                        explore_done = sprite.update(self.Actor, event, self)
                    else:
                        sprite.update()
                ##---------- CHEAT CODE ------------##
                if event.type == KEYDOWN and event.key == K_q:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_p:
                        return True
                ##-------- END CHEAT CODE ----------##
            self.Inventory.draw(self.screen)
            if explore_done:
                return True
            pygame.display.update()
        return False

class MissionScene(Scene):
    """Open up a NEW screen, offer option to close, preserve the old scene
        so it doesn't have to initialize all over again."""
    def __init__(self, img, color):
        Scene.__init__(self, img)
        self.mission_text = []
        self.mission_text_index = 0
        self.color = color

    def main_loop(self):
        """ Makes it so when you press Enter, it moves to the next text."""
        font = pygame.font.Font("InternationalPlayboy.ttf", 22);
        font_height = font.get_linesize()
        siz = font.size(self.mission_text[self.mission_text_index])
        SCREEN_SIZE = (640, 480)
        while True:
            self.screen.blit(self.img,(0,0))
            for index in range(4):        
                self.screen.blit(font.render(self.mission_text[
                self.mission_text_index + index], True, self.color),
                            (75,SCREEN_SIZE[1] * 1 / 5 + index * siz[1]))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
                    if event.key == K_RETURN:
                        self.mission_text_index += 4
                        if self.mission_text_index+3 >= len(self.mission_text):
                            return True
            pygame.display.update()


class CreditScene(Scene):
    '''Creates a scene for displaying the team members who have worked on
       this project.'''

    def main_loop(self):
        while self.keepgoing:
            self.screen.blit(self.img,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.keepgoing = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.keepgoing = False
                    if event.key == K_RETURN:
                        self.keepgoing = False
            pygame.display.update()
        return False



class TrophyScene(Scene):
    """Creates scene where player can interact with trophies. """

    def __init__(self):
        '''Creates a list of trophies.'''
        Scene.__init__(self,'data/Trophy_Background.png')
        self.trophy_list = list()
        # Eventually, trophy will have to be an Interactive Object/3D object
        
    def main_loop(self):
        """Provide methods for interacting with trophies"""
        while True:
            self.screen.blit(self.img,(0,0))
            self.SpriteList.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return False
                if pygame.mouse.get_pressed()[0] == True:
                    pos = pygame.mouse.get_pos()
                    for sprite in self.SpriteList:
                        x = self.check_bounds(pos, sprite)
                        if x != None:
                            self.show_3D(x)

    def check_bounds(self, pos, sprite):
        '''Detects whether mouse is on trophy '''
        mouse_x = pos[0]; mouse_y = pos[1]
        left_edge = sprite.rect[0]; top = sprite.rect[1];
        width = sprite.rect[2]; height = sprite.rect[3];
        if mouse_x > left_edge and mouse_x < (left_edge + width)\
           and mouse_y > top and mouse_y < (top + height):
            print 'Starting 3D Viewer...'
            if sprite == self.trophy_list[0]:
                return 'Ford.egg'
            if sprite == self.trophy_list[1]:
                return 'Wright.egg'
            if sprite == self.trophy_list[2]:
                return 'Rocket.egg'
        return

    def show_3D(self,fname):
        '''Determines if user has pview, and if not, raises an error.'''
        try:
            os.popen('pview ' + 'data/' + fname)
        except:
            print "You don't have pview installed..."
        return

class MainMenu(Scene):
    """Creates home screen, where user can choose to start the game,
       view credits, or quit."""

    def __init__(self):
        '''Initializes the various files in a list and groups them '''
        Scene.__init__(self,'data/MainMenu.png')
        self.__files = ['data/Start_on.png','data/Credits_off.png',
                      'data/Quit_off.png','data/Start_off.png',
                      'data/Credits_on.png','data/Quit_off.png',
                      'data/Start_off.png','data/Credits_off.png',
                      'data/Quit_on.png']
        self.__links = []
        for x in self.__files:
            link = self.__menu_link(x)
            # reposition the link files
            link.x = 320
            link.y = 240
            self.__links.append(link)
        self.__start_on = self.__links[0:3]
        self.__credits_on = self.__links[3:6]
        self.__quit_on = self.__links[6:]
        # Start with the 'Start' icon highlighted
        for y in self.__start_on:
            self.SpriteList.add(y)

    def main_loop(self):
        '''Continues to correct scene depending on user interaction.'''
        self.__refresh_list(self.__start_on)
        while self.keepgoing:
            self.screen.blit(self.img,(0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_UP:
                        if self.__same_list(self.SpriteList, self.__credits_on):
                            self.__refresh_list(self.__start_on)
                        elif self.__same_list(self.SpriteList, self.__quit_on):
                            self.__refresh_list(self.__credits_on)
                    if event.key == K_DOWN:
                        if self.__same_list(self.SpriteList, self.__start_on):
                            self.__refresh_list(self.__credits_on)
                        elif self.__same_list(self.SpriteList,
                                              self.__credits_on):
                            self.__refresh_list(self.__quit_on)
                    if event.key == K_RETURN:
                        if self.__same_list(self.SpriteList, self.__start_on):
                            self.keepgoing = False
                        if self.__same_list(self.SpriteList, self.__credits_on):
                            s = CreditScene('data/Credits.png')
                            s.main_loop()
                        if self.__same_list(self.SpriteList, self.__quit_on):
                            exit()
            for x in self.SpriteList:
                x.update()
            self.SpriteList.draw(self.screen)
            pygame.display.update()
        return False

    def __refresh_list(self, new_list):
        '''Creates new list of sprites  '''
        self.SpriteList.empty()
        for link in new_list:
            self.SpriteList.add(link)

    def __same_list(self, list1, list2):
        x = len(list1); count = 0
        for i in list2:
            if i in list1:
                count+=1
        if count == x:
            return True
        
    def __menu_link(self,img):
        return BasicSprite(self, img,1)

class CharSelect(Scene):
    """Creates a scene for displaying the different avatars that the player
       can choose to play"""

    def __init__(self):
        Scene.__init__(self,'data/CharSelect.png')
        files = ['data/Boy_High.png','data/Girl.png',
                 'data/Boy.png','data/Girl_High.png']
        self.__links = []
        for x in files:
            char = self.__menu_link(x)
            char.x += 320; char.y += 240
            self.__links.append(char)
        self.__boy_on = self.__links[0:2]
        self.__girl_on = self.__links[2:]
        for y in self.__boy_on:
            self.SpriteList.add(y)

    def main_loop(self):
        self.__refresh_list(self.__boy_on)
        global character
        while self.keepgoing:
            self.screen.blit(self.img,(0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
                    if event.key == K_LEFT:
                        self.__refresh_list(self.__boy_on)
                    if event.key == K_RIGHT:
                        self.__refresh_list(self.__girl_on)
                    if event.key == K_RETURN:
                        if self.__same_list(self.SpriteList, self.__boy_on):
                            character = 'data/boy_char.png'
                            self.keepgoing = False
                        if self.__same_list(self.SpriteList, self.__girl_on):
                            character = 'data/girl_char.png'
                            self.keepgoing = False
            for x in self.SpriteList:
                x.update()
            self.SpriteList.draw(self.screen)
            pygame.display.update()
        return character

    def __menu_link(self,img):
        return BasicSprite(self, img,1)        

    def __refresh_list(self, new_list):
        self.SpriteList.empty()
        for link in new_list:
            self.SpriteList.add(link)

    def __same_list(self, list1, list2):
        x = len(list1); count = 0
        for i in list2:
            if i in list1:
                count+=1
        if count == x:
            return True

class WorldMap(Scene):
    '''Takes a specific world map image and blits onto screen. '''
    def __init__(self,img):
        Scene.__init__(self,img)


    def main_loop(self):
        while self.keepgoing:
            self.screen.blit(self.img,(0,0))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
                    if event.key == K_RETURN:
                        self.keepgoing = False
            for x in self.SpriteList:
                x.update()
            self.SpriteList.draw(self.screen)
            pygame.display.update()
        return True


#---------------------------------------------------------------#
#                   Mission Scene creator functions             #
#---------------------------------------------------------------#

def car_mission():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ["Hi there! My name is Henry Ford, and I'm making",
                       "Model T automobiles with this new technique:",
                       "the assembly line!", "",
                       "This allows for mass production, so my Model T's can",
                       "be cheap enough for anyone who wants one to afford it.",
                       "", "",
                       "Unfortunately, the villain has stolen the parts I ",
                       "ordered. If you help me find them, I'll let you test",
                       "drive one of my Model T's. How does that sound?", "",
                       "There are eight parts: wheels, axle, windshield, bolts,",
                       "engine, body, seats, and steering wheel.",
                       "Come talk to me again once you've found everything",
                       "to take one of my Model T's for a spin."
                       ]
    sc.main_loop()

def plane_mission():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Hello! We are the Wright brothers,',
                       'and we invented the first airplane.',
                       "Today, December 17th, 1903, we're building our plane.",
                       'But first we need your help!',
                       'The villain stole all the parts of our plane,',
                       'and we cannot find them.  Can you help us?',
                       'When you find all the parts, your inventory will be'
                       'full.',
                       'Come see us then to move on to the puzzle challenge!',''
                       ]
    sc.main_loop()

def rocket_mission():
    img = 'data/Rocket_Info.png'
    sc = MissionScene(img, (255,255,255))
    sc.mission_text = ['Welcome to JPL. I am Charlie Elachi, director at JPL,',
                       'and I need your help.  Normally I would take you on a',
                       'tour of our lab, but the shuttle is about to launch',
                       'and the correct flight sequence is not programmed.',
                       'I only have T-minus ten minutes to figure out the',
                       'correct flight sequence. The villain went on my',
                       'computer and changed the sequence.',
                       'He even removed all the buttons and hid them!',
                       'Can you help me find all the scattered red buttons?',
                       'After you find all the parts, let me know.',
                       'Then you can try to enter the correct launch sequence.',
                       'We are all counting on you!'
                       ]
    sc.main_loop()



#-----------------------------------------------------------------------#
#                         Car Information                               #
#-----------------------------------------------------------------------#

# These function definitions provide information about each part that is
# picked up

def car_wheel_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Oh good, you found the wheels!',
                       'It would be hard to move that big chunk of metal ',
                       'without them.',''
                       ]
    sc.main_loop()

def car_axle_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['That is an axle!',
                       'Wheels are not much use without them.','',''
                       ]
    sc.main_loop()

def car_windshield_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Goodness, you found the windshield.',
                       'This will help shield us from the wind and make ',
                       'travel much more comfortable.',''
                       ]
    sc.main_loop()

def car_bolts_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Oh my, almost forgot the bolts!',
                       'These are very handy for putting parts together.','','',
                       ]
    sc.main_loop()

def car_engine_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['The engine!',
                       'I would say this is the most crucial part.',
                       'This is the part of the car that does the work and',
                       'allows the car to move at all!'
                       ]
    sc.main_loop()

def car_body_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['This is the car body!',
                       'This protects all the other parts and makes the',
                       'automobile nicer to look at.','',
                       ]
    sc.main_loop()

def car_seat_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['The seats! Those are very useful!',
                       'They make the riders comfortable, and the ride',
                       'more pleasant.','',
                       ]
    sc.main_loop()

def car_steering_info():
    img = 'data/Ford_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Oh yes, the steering wheel is very important.',
                       'The driver needs some way of controlling the direction',
                       'of the car.','',
                       ]
    sc.main_loop()

#-----------------------------------------------------------------------#
#                       Plane Information                               #
#-----------------------------------------------------------------------#

# These function definitions provide information about the different plane
# parts that are picked up by the Actor.

def plane_wing_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['This is one of the wings of our plane.',
                       'Our plane has two wings, so it is called a biplane.',
                       'Two wings can provide greater lift for the plane.',
                       '',
                       ]
    sc.main_loop()

def plane_wing_info_2():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Thank you! This is the second wing of our plane.','','','',
                       ]
    sc.main_loop()

def plane_engine_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['This is one of the engines of our plane.',
                       'The engine drives the propeller.','','',
                       ]
    sc.main_loop()

def plane_elevator_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ["You're amazing!",
                       'This is the elevator.',
                       'It changes the pitch of the plane up and down.','',
                       ]
    sc.main_loop()

def plane_fuselage_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ["You're doing great!",
                       'This is called the fuselage.',
                       'It is the body of the plane.',
                       'It holds everything together.',
                       ]
    sc.main_loop()

def plane_propeller_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Well done!',
                       'This is the propeller.',
                       'It generates thrust so the plane can fly.','',
                       ]
    sc.main_loop()

def plane_rudder_info():
    img = 'data/Wright_Info.png'
    sc = MissionScene(img, (0,0,0))
    sc.mission_text = ['Most excellent!',
                       'We really needed this rudder.',
                       'It allows us to navigate, or change the direction, of',
                       'our plane.'
                       ]
    sc.main_loop()

