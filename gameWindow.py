import pygame
import os 
from pathlib import Path


"""
    Date: 12th October, 2019
    Author: Jose Guerrero
    Description: Python tutorial catered for beginners to the world of programming
    Prequisites: Willingness to learn and have fun while doing so. 
"""
# This line is a comment which means the computer will skip it when it is running this file 
# We use these comments to tell other people what we are doing in our code 

print("Let the games begin")
print(os.getcwd())


# Let us tell the game library to get ready for us (this is called initialization)
pygame.init()

# We make a display object with size 800 length and 600 height in pixels 
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# We are giving our screen a title 
pygame.display.set_caption('Fast and Deivi')

# Defining some colors for use in the game
black = (0,0,0)
white = (255, 255, 255)  # these represent colors for red blue green which can can take values from 0 to 255

# Used for checking if the game has stopped
crashed = False

# Clock used to keep track of the game events
clock = pygame.time.Clock()

# Lets load an image for our game 
spaceshipImg = pygame.image.load('c:/Users/eseujgo/Desktop/Game/racecar.png').convert()

# This is a function that will display our spaceship at a x and y position
def spaceShip(x,y):
    gameDisplay.blit(spaceshipImg, (x,y)) 
    
x = (displayWidth) * 0.45
y = (displayHeight) * 0.5 

while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    gameDisplay.fill(white)
    spaceShip(x,y)
        
    pygame.display.update()
    clock.tick(60)

# If we exit the loop means program ended then we close the game library
pygame.quit()
quit()
print('Goodbye') 

