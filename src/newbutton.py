import pygame

class NewButton:
  def __init__(self, color, x, y, width, height, text=''):
    """
    Creates a button with text inside of it without a sprite
    args:
      self - NewButton, object created by the class
      color - tuple, RGB values for the color of the button
      x - int, x-coordinate of the button
      y - int, y-coordinate of the button
      width - int, width of the rectangle of the button
      height - int, height of the rectangle of the button
      text - str, the text displayed inside of the button
    return: None
    """
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text

  def draw(self,win,outline=None): #Call this to draw the button on the screen
    """
    Draws the button onto the display created by pygame
    args:
      self - NewButton, object created by the class
      win - pygame window, display created by pygame
      outline - None/int, the thickness of the outline of the button
    return: None
    """
    #If we do not give an outline to the button, will create an outline-less button
    if outline is not None:
      pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
    pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
    
    #Setting the text for the button
    if self.text != '':
      font = pygame.font.SysFont('New York', 45)
      text = font.render(self.text, 1, (0,0,0))
      win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

  def isOver(self, pos): #Pos = mouse position in a tuple of (x,y) coordinates. Tuple is a fun word.
    """
    Detects if the mouse is over the button
    args:
      self - NewButton, object created by the class
      pos - tuple, contains x and y coordinates of the cursor
    return: None
    """
    if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
      if pos[1] > self.y and pos[1] < self.y + self.height:
        return True
    else:    
      return False
