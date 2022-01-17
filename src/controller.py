# FARM MOORE!
# Made with love by Nick Reyes, Luca DiGrigoli, and Adam Acevedo
# 2021, CS110 <3
# Credit to Prof. Moore for his likeness and image. You Rock!

import sys
import pygame
import random
import time
import json
#import microwave
from src import newbutton
from src import cursormode
from src import plant
from src import customer

class Controller:
    def __init__(self, width=1200, height=800):
        """
        Initializes the controller object to create a a screen and GUI for the program to run on
        args:
            self - Controller, the object created by the class
            width - int, the number for the with of the screen
            height - int, the number for the height of the screen
        return: None
        """
        #Initializes pygame related 
        pygame.init()
        pygame.font.init()
        
        #Creates the screen
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        #Background images for the main  menu and gameplay display
        self.menuBackground = pygame.image.load('assets/MenuBack.jpg')
        self.gardenBackground = pygame.image.load('assets/GardenBack.png')
        self.background = pygame.Surface((1200, 800))
        self.exitBack = pygame.image.load('assets/exitBack.png')
        self.exitback = pygame.transform.scale(self.exitBack, (1200, 800))
        
        #Sets the game state to MAIN MENU so the display is set to the main menu
        self.state = "MAIN MENU"

        #Creates an object that tracks what the user last clicked on
        self.cursor = cursormode.Cursormode()

        #Creating buttons for the main menu screen
        self.exitButton = newbutton.NewButton((128,0,32), 750, 400, 200, 50, 'Exit Game')
        self.startButton = newbutton.NewButton((63,122,77), 750, 300, 200, 50, 'Start Farming!')

        #Creating buttons for the gameplay screen
        self.seedButton = newbutton.NewButton((144,238,144), 50, 50, 100, 100, 'Seeds')
        self.waterButton = newbutton.NewButton((46,139,87), 200, 50, 100, 100, 'Water')
        self.gameExit = newbutton.NewButton((140,0,35), 1125, 50, 50, 50, 'Exit')

        #creating button for the quit screen
        self.quitButton = newbutton.NewButton((255,127,80), 450, 500, 200, 50, 'Quit game')

        #Creating the plant plots
        self.plot1 = plant.Plant(150,250,200,200, self.screen)
        self.plot2 = plant.Plant(400,250,200,200,self.screen)
        self.plot3 = plant.Plant(150,500,200,200, self.screen)
        self.plot4 = plant.Plant(400,500,200,200, self.screen)

        #Adding the plants to a sprite group
        self.plots = pygame.sprite.Group()
        self.plots.add(self.plot1)
        self.plots.add(self.plot2)
        self.plots.add(self.plot3)
        self.plots.add(self.plot4)

        self.customers = 0

        myfont = pygame.font.SysFont('New York', 30)

        #Top bar and Icon settings
        pygame.display.set_caption("Farm Moore!")
        icon = pygame.image.load('assets/Icon.png')
        pygame.display.set_icon(icon)


        #Setting the screen and retrieving the font name
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font_name = pygame.font.get_default_font()
        self.clock = pygame.time.Clock()

        self.scores = open("src/past_players.json", "r")
        self.entry = json.load(self.scores)
        self.scores.close()
        
        

    def mainLoop(self):
        """
        Will produce the various "screens" of the game and change the display should the state of the game change
        args: self - controller, the GUI made by the controller class
        return: None
        """
        while True:
          #Main Menu
          if(self.state == "MAIN MENU"):
            self.mainMenu()

          #Gameplay screen
          elif(self.state == "GAME"):
            self.gamePlay()
          
          #Exit screen
          elif(self.state == "EXIT"):
            self.exitScreen()
    
    def mainMenu(self):
        """
        Sets the game to the main menu display and draws its associated buttons, will also cease drawing the buttons should the game state change
        args: self - controller, screen created by the controller class
        return: None
        """
        while self.state == "MAIN MENU":

            #begin updates and checks
            for event in pygame.event.get():
              
              pos = pygame.mouse.get_pos()

              #If user X's out, the program closes
              if event.type == pygame.QUIT:
                sys.exit()

              #Checking if the mouse is hovering over the buttons
              if event.type == pygame.MOUSEMOTION:
                  if self.exitButton.isOver(pos):
                    self.exitButton.color = (100,49,62)
                  else:
                    self.exitButton.color = (128,0,32)
                  if self.startButton.isOver(pos):
                    self.startButton.color = (11,102,35)
                  else:
                    self.startButton.color = (63,122,77)

              #Checking if the mouse has clicked over any of the menu buttons
              if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exitButton.isOver(pos):
                  pygame.quit()
                  print("See you space farmer...")
                  sys.exit()
                elif self.startButton.isOver(pos):
                  self.state = "GAME"

            #Blitting image onto the beckground and drawing buttons onto screen
            self.screen.blit((self.menuBackground),(0,0))
            self.startButton.draw(self.screen,(0,0,0))
            self.exitButton.draw(self.screen,(0,0,0))
  
            #Updating the display
            pygame.display.flip()
            



    def gamePlay(self):
        """
        Sets the game to the gameplay display and create and destroys associated sprites depending on state
        args: self - controller, screen object created by class
        return: None
        """
        #Establishing variables for later use

        #For the JSON
        self.plants_sold = 0
        self.currency = 0
        start_time = time.time()

        #For simulating plant growth
        growth_time1 = 0
        growth_time2 = 0
        growth_time3 = 0
        growth_time4 = 0
        watered1 = False
        watered2 = False
        watered3 = False
        watered4 = False
        customer_served = False

        while self.state == "GAME":
          
          #Creating a currency display that updates; needs to be here so that it can update as the currency does
          self.currencyButton = newbutton.NewButton((252,186,3),600,50,200,50, str(self.currency))

          #Growth simulation 
          if watered1:
            growth_time1_ms = pygame.time.get_ticks() - growth_start1
            growth_time1 = growth_time1_ms / 1000
            if growth_time1 >= 10.0 and self.plot1.plant_state != 4:
              self.plot1.plant_state = 3
              growth_time1 = 0
              watered1 = False
            elif growth_time1 >= 5.0:
              self.plot1.plant_state = 2
            
          if watered2:
            growth_time2_ms = pygame.time.get_ticks() - growth_start2
            growth_time2 = growth_time2_ms / 1000
            if growth_time2 >= 10.0 and self.plot2.plant_state != 4:
              self.plot2.plant_state = 3
              growth_time2 = 0
              watered2 = False
            elif growth_time2 >= 5.0:
              self.plot2.plant_state = 2
          
          if watered3:
            growth_time3_ms = pygame.time.get_ticks() - growth_start3
            growth_time3 = growth_time3_ms / 1000
            if growth_time3 >= 10.0 and self.plot3.plant_state != 4:
              self.plot3.plant_state = 3
              growth_time3 = 0
              watered3 = False
            elif growth_time3 >= 5.0:
              self.plot3.plant_state = 2
          
          if watered4:
            growth_time4_ms = pygame.time.get_ticks() - growth_start4
            growth_time4 = growth_time4_ms / 1000
            if growth_time4 >= 10.0 and self.plot4.plant_state != 4:
              self.plot4.plant_state = 3
              growth_time4 = 0
              watered4 = False
            elif growth_time4 >= 5.0:
              self.plot4.plant_state = 2

          #begins updates and checks
          for event in pygame.event.get():

            #update mouse position
            pos = pygame.mouse.get_pos()

            #If the user X's out, the display and program closes
            if event.type == pygame.QUIT:
              pygame.quit()
              print("See you space farmer...")
              sys.exit()

            #Checking if the mouse is hovering over the seed and water buttons
            if event.type == pygame.MOUSEMOTION:
              if self.seedButton.isOver(pos): 
                self.seedButton.color = (46,139,87)
              else:
                self.seedButton.color = (144,238,144)

              if self.waterButton.isOver(pos):
                self.waterButton.color = (50,82,123)
              else:
                self.waterButton.color = (120,144,216)

            #Checking if the cursor clicked over any buttons
            if event.type == pygame.MOUSEBUTTONDOWN:

              #Seed button checks
              if self.seedButton.isOver(pos):
                print("clicked seed.")

                #Selectes or deselects seed based on what you already have selected
                if self.cursor.cursorMode is not 'SEED':
                  self.cursor.modeSeed()
                  print(self.cursor.cursorMode)
                elif self.cursor.cursorMode is 'SEED':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)

              #Water button checks
              elif self.waterButton.isOver(pos):   
                print("clicked water")

                #Selects or deselects water based on what you already have selected
                if self.cursor.cursorMode is not 'WATER':
                  self.cursor.modeWater()
                  print(self.cursor.cursorMode)
                elif self.cursor.cursorMode is 'WATER':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
              


              #Plot button click check (upper left plot)
              elif tuple(self.plots)[0].isOver(pos):
                print("clicked plot")

                #If the seed is selected and the empty plot is clicked, plants a plant
                if self.cursor.cursorMode is 'SEED' and self.plot1.plant_state is 0:
                  self.plot1.plant()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #If a plant is planted and water is selected, the plant will begin growing
                elif self.cursor.cursorMode  is 'WATER' and self.plot1.plant_state is 1:
                  watered1 = True
                  growth_start1 = pygame.time.get_ticks()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #Selects or deselects the plant based on what you have selected
                elif self.plot1.plant_state is 4 and self.cursor.cursorMode is not 'PLANT1':
                  self.cursor.modePlant1()
                  print(self.cursor.cursorMode)
                elif self.plot1.plant_state is 4 and self.cursor.cursorMode is 'PLANT1':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
              
              #Plot button click check (upper right plot)
              elif tuple(self.plots)[1].isOver(pos):
                print("clicked plot")

                #If the seed is selected and the empty plot is clicked, plants a plant
                if self.cursor.cursorMode is 'SEED' and self.plot2.plant_state is 0:
                  self.plot2.plant()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #If a plant is planted and water is selected, the plant will begin growing
                elif self.cursor.cursorMode  is 'WATER' and self.plot2.plant_state is 1:
                  watered2 = True
                  growth_start2 = pygame.time.get_ticks()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #Selects or deselects the plant based on what you have selected
                elif self.plot2.plant_state is 4 and self.cursor.cursorMode is not 'PLANT2':
                  self.cursor.modePlant2()
                  print(self.cursor.cursorMode)
                elif self.plot2.plant_state is 4 and self.cursor.cursorMode is 'PLANT2':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
              
              #Plot button click check (lower left plot)
              elif tuple(self.plots)[2].isOver(pos):
                print("clicked plot")

                #If the seed is selected and the empty plot is clicked, plants a plant
                if self.cursor.cursorMode is 'SEED' and self.plot3.plant_state is 0:
                  self.plot3.plant()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #If a plant is planted and water is selected, the plant will begin growing
                elif self.cursor.cursorMode  is 'WATER' and self.plot3.plant_state is 1:
                  watered3 = True
                  growth_start3 = pygame.time.get_ticks()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #Selects or deselects the plant based on what you have selected
                elif self.plot3.plant_state is 4 and self.cursor.cursorMode is not 'PLANT3':
                  self.cursor.modePlant3()
                  print(self.cursor.cursorMode)
                elif self.plot3.plant_state is 4 and self.cursor.cursorMode is 'PLANT3':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
              
              #Plot button click check (lower right plot)
              elif tuple(self.plots)[3].isOver(pos):
                print("clicked plot")

                #If the seed is selected and the empty plot is clicked, plants a plant
                if self.cursor.cursorMode is 'SEED' and self.plot4.plant_state is 0:
                  self.plot4.plant()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #If a plant is planted and water is selected, the plant will begin growing
                elif self.cursor.cursorMode  is 'WATER' and self.plot4.plant_state is 1:
                  watered4 = True
                  growth_start4 = pygame.time.get_ticks()
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
                #Selects or deselects the plant based on what you have selected
                elif self.plot4.plant_state is 4 and self.cursor.cursorMode is not 'PLANT4':
                  self.cursor.modePlant4()
                  print(self.cursor.cursorMode)
                elif self.plot4.plant_state is 4 and self.cursor.cursorMode is 'PLANT4':
                  self.cursor.modeNull()
                  print(self.cursor.cursorMode)
                
              #Customer click checks
              elif self.local.isOver(pos):
                if self.cursor.cursorMode is '':
                  print("Hello! One plant please!")
                
                elif self.cursor.cursorMode is 'SEED':
                  print("Hey, not seeds! A plant please!")
                  self.cursor.modeNull()

                elif self.cursor.cursorMode is 'WATER':
                  print("I have water at home! One plant please!")
                  self.cursor.modeNull()

                #If the upper left plant is selected, it will be sold to the customer
                elif self.cursor.cursorMode is 'PLANT1' or 'PLANT2' or 'PLANT3' or 'PLANT4':
                  #Resets and gets rid of plant
                  if self.cursor.cursorMode is 'PLANT1':
                    tuple(self.plots)[0].plant_state = 0
                    self.cursor.modeNull()
                  elif self.cursor.cursorMode is 'PLANT2':
                    tuple(self.plots)[1].plant_state = 0
                    self.cursor.modeNull()
                  elif self.cursor.cursorMode is 'PLANT3':
                    tuple(self.plots)[2].plant_state = 0
                    self.cursor.modeNull()
                  elif self.cursor.cursorMode is 'PLANT4':
                    tuple(self.plots)[3].plant_state = 0
                    self.cursor.modeNull()
                  
                  #Customer gives player score and leaves
                  if self.local.final_image_choice is self.local.spaceMoore:
                    print("That's one small step for Moore, one giant step for Moorekind")
                  else:
                    print("Thanks!")
                  self.currency += random.randint(1,50)
                  self.plants_sold += 1
                  self.local.leave(25)
                  customer_served = True

              #Exit button click checks
              elif self.gameExit.isOver(pos):
                finish_time_sec = time.time() - start_time
                self.game_time_min = finish_time_sec / 60
                self.state = "EXIT"

            
            
  
            #Blitting background image and drawing buttons in order to update screen
            self.screen.blit((self.gardenBackground),(0,0))
            self.seedButton.draw(self.screen,(0,0,0)) 
            self.waterButton.draw(self.screen,(0,0,0))
            self.currencyButton.draw(self.screen,(0,0,0))
            self.gameExit.draw(self.screen,(0,0,0))
            for item in self.plots:
              item.drawPlant()

            #Checks if the customer has left; if so creates a new customer and if not it continues drawing the customer
            if self.customers == 0:
              self.local = customer.Customer("Steve", 1000, 0, 100, 100, self.screen)
              self.customers = 1
            if self.customers != 0:
              self.local.drawCustomer()
              self.local.enter(25)
            
            #Gets the customer to leave if a plant has been sold
            if customer_served:
              self.local.leave(25)
              if self.local.on_screen is False:
                self.local.arrived = False
                self.local.kill()
                customer_served = False
                self.customers = 0
            
            self.clock.tick(60)
            pygame.display.flip()

    def exitScreen(self):
        """
        no idea here, just another screen template if we need it
        args: self - controller, screen object created by class
        return: None
        """
        while self.state == "EXIT":
            for event in pygame.event.get():

              pos = pygame.mouse.get_pos()

              #Exits the game if the exit button is selected
              if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quitButton.isOver(pos):
                  pygame.quit()
                  print("See you space farmer...")
                  username = input("Please enter a username to record/update your score: ")
                  self.entry[username] = (str(self.game_time_min), str(self.currency), str(self.plants_sold))
                  self.scores = open("src/past_players.json", "w")
                  json_print = json.dump(self.entry, self.scores)
                  self.scores.close()

                  #Displays information held in the JSON file
                  print("\n#### Previous Player Scores ####")

                  file_ptr = open("src/past_players.json", "r")
                  file_ldr = json.load(file_ptr)
                  for key in tuple(file_ldr.keys()):
                    print(f"Player: {key}")
                    print(f" -Game Time: {file_ldr[key][0]} minutes")
                    print(f" -Currency: {file_ldr[key][1]} Moorebucks")
                    print(f" -Plants sold: {file_ldr[key][2]} plants\n")
                  file_ptr.close()
                  sys.exit()

              self.screen.blit((self.exitBack),(0,0))
              self.quitButton.draw(self.screen,(0,0,0))
            pygame.display.flip()

