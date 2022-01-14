import pygame
import time
import random

class Customer(pygame.sprite.Sprite):
    def __init__(self, name, x, y, width, height, win):
        """
        Creates customer sprite object in the store screen
        args:
            name - str, will be the name of a given customer
            image - file, will be the image that displays the customer on the screen
            x - int, the x coordinate for the customer sprite's location
            y - int, the y coordinate for the customer sprite's location
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = win
        self.arrived = False
        self.on_screen = True
        self.count = 0

        self.spaceMoore = pygame.image.load('assets/spacemoore.jpg').convert_alpha()
        self.bwMoore = pygame.image.load('assets/bwmoore.png').convert_alpha()
        self.stevenLesse = pygame.image.load('assets/stevenlesse.jpg').convert_alpha()
        self.glitchMoore = pygame.image.load('assets/glitchmoore.png').convert_alpha()
        self.godMoore = pygame.image.load('assets/godmoore.png').convert_alpha()
        self.normalMoore = pygame.image.load('assets/Icon.png').convert_alpha()
        selected = random.randint(0, 5)
        if selected == 0:
          self.final_image_choice = self.bwMoore
        elif selected == 1:
          self.final_image_choice = self.stevenLesse
        elif selected == 2:
          self.final_image_choice = self.glitchMoore
        elif selected == 3:
          self.final_image_choice = self.godMoore
        elif selected == 4:
          self.final_image_choice = self.spaceMoore
        elif selected == 5:
          self.final_image_choice = self.normalMoore


    def drawCustomer(self): #Call this to create Customer on game screen
        """
        Draws the customer on the game screen; will likely be called every loop
        args: self - Customer, object created by the class
        return: None
        """
        size = (self.width, self.height)
        surface = pygame.Surface(size)
        scale = pygame.transform.scale((self.final_image_choice), (self.width, self.height))
        self.win.blit(scale,(self.x, self.y))

    def enter(self, speed):
        """
        Tells the customer sprite where to go after they enter the store
        args:
            self - Customer, sprite object created by class
            speed - int, how fast the sprite will enter the store
        return: None
        """
        if self.y < 600 and self.count == 0:
          self.y += speed
        if self.y > 599 and self.count == 0:
          self.count += 1
          self.arrived = True 
          print("Hello, I would like one of your finest plants!")

    def leave(self, speed):
        """
        Tells the customer to leave the screen so that it will be eventually killed
        args:
            self - Customer, the object created by the class
            speed - int, how quickly the customer will leave the screen
        return: None
        """
        if self.y > -400:
            self.y -= speed
        elif self.y < 0:
          self.on_screen = False



    def isOver(self, pos):
        """
        Checks the position of the mouse to see if the button was clicked on
        args:
            self - Customer, object created by the class
            pos - tuple, position (x, y coordinate) of the mouse in a screen
        return:
            True - if mouse clicks over the button
            False - any other occurence
        """
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y+ self.height:
                return True
        return False
