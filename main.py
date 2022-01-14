#import your controller
import pygame
from src import controller

def main():
	main_window = controller.Controller()
	main_window.mainLoop()
	pygame.init()
	team = {"lead":"Nicholas Reyes", "backend":"Adam Acevedo", "frontend":"Luca DiGrigoli"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:", team["frontend"])
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ###### 
main()
