import pygame
import time
import random

class Plant(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, win):
    """
    Will create a plant object for the player to place on a plot
    args:
      self
      x - int, the x-coordinate for the rectangle
      y - int, the y-coordinate for the rectangle
      img_file - the image file needed for the sprite
    return: None
    """
    pygame.sprite.Sprite.__init__(self)

    #Setting parameters for the image on the screen
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.win = win
    self.plant_state = 0
    self.watered = False

    #Loading every possible picture for the plant buttons
    self.emptyPlot_img = pygame.image.load('assets/emptyPlot.png').convert_alpha()
    self.planted_img = pygame.image.load('assets/planted.png').convert_alpha()
    self.growing_img = pygame.image.load('assets/growing.png').convert_alpha()
    self.lilac_img = pygame.image.load('assets/finishedLilac.png').convert_alpha()
    self.pumpkin_img = pygame.image.load('assets/finishedPump.png').convert_alpha()
    self.sunflower_img = pygame.image.load('assets/finishedSun.png').convert_alpha()
    self.peashooter_img = pygame.image.load('assets/finishedPea.png').convert_alpha()
    self.tulip_img = pygame.image.load('assets/finishedTulip.png').convert_alpha()
  
  def plant(self):
    """
    Method for planting a seed (mostly here to make it easier to look at)
    args: self - Plant, object create by the class
    return: None
    """
    self.plant_state = 1
   
  def drawPlant(self): #Call this to draw the button on the screen
    """
    For drawing and redrawing plant plots for every update
    args: self - Plant, object created by the class
    return: None
    """
    size = (self.width, self.height)
    surface = pygame.Surface(size)
    
    #Sets the image for each stage of growth
    if self.plant_state == 0:
      image_choice = self.emptyPlot_img
    elif self.plant_state == 1:
      image_choice = self.planted_img
    elif self.plant_state == 2:
      image_choice = self.growing_img
    
    #Sets the image for the final stage of growth, but chooses a new image at random each time
    elif self.plant_state == 3:

      #Making sure the image doesn't update further by making 4 the final stage
      self.plant_state += 1

      #Randomly choosing an image for the final plant state
      selected = random.randint(0, 4)
      if selected == 0:
        self.final_image_choice = self.lilac_img
      elif selected == 1:
        self.final_image_choice = self.pumpkin_img
      elif selected == 2:
        self.final_image_choice = self.sunflower_img
      elif selected == 3:
        self.final_image_choice = self.peashooter_img
      elif selected == 4:
        self.final_image_choice = self.tulip_img
      
    #Choosing and blitting images based on plant state
    if self.plant_state == 4:
      scale = pygame.transform.scale(self.final_image_choice, (self.width, self.height))
    else:
      scale = pygame.transform.scale(image_choice, (self.width, self.height))
    self.win.blit(scale,(self.x, self.y))

  def isOver(self, pos):
    """
    Checks the position of the mouse to see if the button was clicked on
    args:
      self - Plant, object created by the class
      pos - tuple, position (x, y coordinate) of the mouse in a screen
    return:
      True - if mouse clicks over the button
      False - any other occurence
    """
    if pos[0] > self.x and pos[0] < self.x + self.width:
      if pos[1] > self.y and pos[1] < self.y+ self.height:
        return True
    return False
      
