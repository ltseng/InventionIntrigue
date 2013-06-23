'''Title: Puzzles.py
    Purpose: Provides the basic puzzle class, as well as its inheritors, which
    are CarPuzzle, PlanePuzzle, and RocketPuzzle
    Authors: Sam, Vidie, Mandy

    Changes: 8 Dec [SPB] Initialized rocket counter to start at 1, so that if the
            user correctly completes on the first try, text saying 1 attempt is
            returned
'''

import pygame, random
from pygame.locals import *
from Engine import Scene, IntObj
from BasicSprite import BasicSprite

class Puzzle(Scene):
    """Puzzle scene: will start with inventory already full.
    There will be a puzzle."""
    def __init__(self, img):
        Scene.__init__(self, img)
        self.Inventory = pygame.sprite.Group()
        self.complete = False

    def main_loop(self):
        """
        Makes it so when you press RETURN, it moves to the next text block.
        """
        font = pygame.font.Font("InternationalPlayboy.ttf", 30);
        font_height = font.get_linesize()
        text = "Hold V and press M."
        siz = font.size(text)
        SCREEN_SIZE = (640, 480)
        while not self.complete:
            self.screen.blit(self.img,(0,0))
            self.screen.blit(font.render(text, True, (0,0,0)), (0,0))
            for item in self.Inventory:
                item.update()
            self.Inventory.draw(self.screen)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return False
                if event.type == KEYDOWN and event.key == K_v:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_m:
                        print "You win!"
                        self.complete = True
                    else:
                        print "You lose"
                        continue
                ##---------- CHEAT CODE ------------##
                if event.type == KEYDOWN and event.key == K_q:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_p:
                        self.complete = True
                ##-------- END CHEAT CODE ----------##
            pygame.display.update()
        return False

class CarPuzzle(Puzzle):
    """
    The snake puzzle where a car has to get to each flag that appears.
    """
    def __init__(self):
        Puzzle.__init__(self,'data/Car/car_background.png')
        
        pygame.mouse.set_visible(False)
        self.time_delay = .2

    def main_loop(self, car):
        """The car moves 20 pixels each half second"""
        clock = pygame.time.Clock
        seconds = 0
        fail = False

        flag = Flag(self)
        flag.x = random.randrange(15,625,10)
        flag.y = random.randrange(15,465,10)
        flag.update()

        start_time = pygame.time.get_ticks()

        while True:
            self.screen.blit(self.img, (0,0))
            self.SpriteList.draw(self.screen)
            time = pygame.time.get_ticks() - start_time
       
            if time/1000.0 > seconds:
                seconds += self.time_delay
                fail = car.move()
                got_flag = flag.gotten(car, self)
                if got_flag:
                    flag = Flag(self)
                    flag.x = random.randrange(15,625,10)
                    flag.y = random.randrange(15,465,10)
                    flag.update()
                

            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return False
                if event.type == KEYDOWN:
                    car.change_heading(event)
                ##---------- CHEAT CODE ------------##
                if event.type == KEYDOWN and event.key == K_q:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_p:
                        return seconds, True
                ##-------- END CHEAT CODE ----------##

            if fail:
                print "You fail"
                return seconds, False
            if len(self.Inventory) > 14:
                print "You win"
                return seconds, True
            elif len(self.Inventory) > 9:
                self.time_delay = .05
            elif len(self.Inventory) > 4:
                self.time_delay = .1

            pygame.display.update() 


class Car(BasicSprite):
    """A car is used in the car_puzzle and will be the sprite the player
    controls"""
    pics = ['data/Car/car_up.png','data/Car/car_right.png',
            'data/Car/car_down.png','data/Car/car_left.png']
    dir_x = [0, 1, 0, -1]
    dir_y = [-1, 0, 1, 0]
    
    def __init__(self, scene):
        '''Initializes position and heading of car.'''
        self.heading = 2
        BasicSprite.__init__(self, scene, self.pics[self.heading])
        
        self.dx = 320
        self.dy = 20
        self.update()

        self.step = 20

    def change_heading(self,event):
        """Changes the heading of the car and the picture"""
        if event.key == K_UP:
            self.heading = 0
        if event.key == K_RIGHT:
            self.heading = 1
        if event.key == K_DOWN:
            self.heading = 2
        if event.key == K_LEFT:
            self.heading = 3
        self.image = pygame.image.load(self.pics[self.heading]).convert_alpha()

    def move(self):
        """Updates the position of the car by self.step in the direction
        of the car's heading and checks if the car collided with the sides.
        If collision occurs, return True, else returns False."""
        self.dx = self.dir_x[self.heading] * self.step
        self.dy = self.dir_y[self.heading] * self.step
        self.update()
        if self.x < 10 or self.x > 630 or self.y < 10 or self.y > 470:
            return True
        return False

class Flag(IntObj):
    """The flag is the object the car must collide with to move on"""
    def __init__(self, scene):
        IntObj.__init__(self, scene, 'data/Car/flag.png')

    def gotten(self, car, scene):
        """Checks if the car collides with the Flag: if so, returns True
        and moves the flag to the scene's Inventory; else returns False"""
        if pygame.Rect.colliderect(self.rect, car.rect):
            self.die(scene)
            return True
        return False
    
    def update(self):
        '''Updates the location of the Flag'''
        self.rect = self.image.get_rect(center = (self.x, self.y))


class PlanePuzzle(Puzzle):
    '''Plane puzzle scene: will start with car inventory already full.'''

    def __init__(self, img):
        Puzzle.__init__(self, img)
        self.clicked = False
    
    def main_loop(self):
        '''
        Puzzle is complete when all items are placed in the correct locations.
        '''
        font = pygame.font.Font("InternationalPlayboy.ttf", 30);
        font_height = font.get_linesize()
        text1 = "Drag the parts to the correct places on the plane."
        text2 = "Then hit Enter."
        siz = font.size(text1)
        SCREEN_SIZE = (640, 480)
        start_time = pygame.time.get_ticks()
        seconds = 0
        
        while not self.complete:
            self.screen.blit(self.img,(0,0))
            self.screen.blit(font.render(text1, True, (10,0,0)), (50,0))
            self.screen.blit(font.render(text2, True, (10,0,0)), (50,40))
            for item in self.Inventory:
                item.update()
            self.Inventory.draw(self.screen)
            self.SpriteList.draw(self.screen)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return False
                if event.type == KEYDOWN and event.key == K_RETURN and \
                   len(self.Inventory) == 0:
                    seconds = (pygame.time.get_ticks() - start_time) / 1000.0
                    self.complete = True
                    print "You win!"
                if event.type == MOUSEBUTTONDOWN and not self.clicked: 
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    for item in self.Inventory:
                        if item.rect.left <= x <= item.rect.right and \
                           item.rect.top <= y <= item.rect.bottom:
                            obj = item
                            self.clicked = True
                if pygame.mouse.get_pressed()[0] == True and self.clicked: 
                    pos = pygame.mouse.get_pos()
                    obj.x = pos[0]
                    obj.y = pos[1]
                    obj.rect = obj.image.get_rect(center = (obj.x, obj.y))
                    #print pos[0], pos[1]
                if event.type == MOUSEBUTTONUP and self.clicked:
                    self.clicked = False
                ##---------- CHEAT CODE ------------##
                if event.type == KEYDOWN and event.key == K_q:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_p:
                        seconds = (pygame.time.get_ticks() - start_time)/1000.0
                        self.complete = True
                ##-------- END CHEAT CODE ----------##
            pygame.display.update()
            self.check_items()
        return seconds, False

    def check_items(self):
        '''Remove correctly placed parts from Inventory, add to SpriteList.'''
        for item in self.Inventory:
            if item.img_name == 'data/Plane/Wings.png' and \
              315 <= item.x <= 319 and 292 <= item.y <= 295:
                self.transfer(item)
            if item.img_name == 'data/Plane/Fuselage.png' and \
              345 <= item.x <= 350 and 280 <= item.y <= 281:
                self.transfer(item)
            if item.img_name == 'data/Plane/Elevator.png' and \
              484 <= item.x <= 487 and 112 <= item.y <= 115:
                self.transfer(item)
            if item.img_name == 'data/Plane/Propeller.png' and \
              207 <= item.x <= 212 and 420 <= item.y <= 423:
                self.transfer(item)
            if item.img_name == 'data/Plane/Rudder.png' and \
              477 <= item.x <= 480 and 73 <= item.y <= 77:
                self.transfer(item)
            if item.img_name == 'data/Plane/Engines_small.png' and \
              401 <= item.x <= 404 and 300 <= item.y <= 307:
                self.transfer(item)
            if item.img_name == 'data/Plane/Engines_small.png' and \
              220 <= item.x <= 223 and 203 <= item.y <= 296:
                self.transfer(item)

    def transfer(self, sprite):
        """ Remove object from screen and add to Inventory screen when picked up"""
        self.Inventory.remove(sprite)
        self.SpriteList.add(sprite)

class RocketPuzzle(Puzzle):
    '''Rocket puzzle where player has to push buttons in the correct order.'''

    def __init__(self, img):
        '''Initialize from Puzzle, create boolean that determines if order is
        correct, and initialize player order.'''
        Puzzle.__init__(self, img)
        self.order = False
        self.player_order = []
        self.correct_order = ['button6', 'button7', 'button8', 'button3',
                              'button5', 'button1', 'button2', 'button4']
        self.key_order_dict = {K_1: 'button1', K_2: 'button2', K_3: 'button3',
                               K_4: 'button4', K_5: 'button5', K_6: 'button6',
                               K_7: 'button7', K_8: 'button8'}
        button_img = ['data/Rocket/1_pressed.png', 'data/Rocket/2_pressed.png',
                      'data/Rocket/3_pressed.png', 'data/Rocket/4_pressed.png',
                      'data/Rocket/5_pressed.png', 'data/Rocket/6_pressed.png',
                      'data/Rocket/7_pressed.png', 'data/Rocket/8_pressed.png']
        butsprites = []
        
        #makes buttons BasicSprites
        for fle in button_img:
            bspr = BasicSprite(self, fle, 1)
            bspr.x = 320
            bspr.y = 240
            butsprites.append(bspr)
            
        #creates dictionary of corresponding buttons and button depression img
        self.key_butsprite_dict = dict(zip(self.key_order_dict.keys(), butsprites))
        self.SpriteList.empty()
 
        
    def main_loop(self):
        '''Puzzle is complete when all items are pressed in correct order.'''
        SCREEN_SIZE = (640, 480)
        global rocket_counter
        rocket_counter = 1

        while not self.complete:
            self.screen.blit(self.img,(0,0))            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
                    if event.key == K_RETURN and self.order:
                        #Once the player has pressed the buttons in the correct
                        #order break from the main loop to move on to trophy scene.
                        self.complete = True
                    if len(self.player_order) < 8:
                        #Gets the order the player presses the buttons.
                        #Only append if it is the correct order, and the player
                        #doesn't already have the correct sequence.
                        for key in self.key_order_dict.keys():
                            if event.key == key:
                                if self.correct_order[len(self.player_order)] == \
                                   self.key_order_dict[key]:
                                    self.player_order.append(self.key_order_dict[key])
                                    #change button depression
                                    self.SpriteList.add(self.key_butsprite_dict[key])
                                else:
                                    self.player_order = []
                                    self.SpriteList.empty()
                                    rocket_counter += 1
            if len(self.player_order) == 8:
                self.order = True

                ##---------- CHEAT CODE ------------##
                if event.type == KEYDOWN and event.key == K_q:
                    event = pygame.event.wait()
                    if event.type == KEYDOWN and event.key == K_p:
                        self.complete = True
                ##-------- END CHEAT CODE ----------##
            for sprite in self.SpriteList:
                sprite.update()
            self.SpriteList.draw(self.screen)
            pygame.display.update()
        return rocket_counter



