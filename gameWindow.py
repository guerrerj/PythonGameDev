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
print('This is the directory: {0}'.format(os.getcwd()))


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
red = (255, 0, 0)

# Clock used to keep track of the game events
clock = pygame.time.Clock()

# Lets load an image for our game 
spaceshipImg = pygame.image.load(str(os.getcwd()) + '/racecar.png').convert()
# Lets choose a size for the spaceship  
shipLength = 75

# This is a function that will display our spaceship at a x and y position
def spaceShip(x,y):
    gameDisplay.blit(spaceshipImg, (x,y)) 

# This a function for the game loop (to keep running)
def gameLoop():
    # This is the intial positioning of the sprite(the name of an image for 2D games)    
    x = (displayWidth) * 0.45
    y = (displayHeight) * 0.5 
    
    # Used for checking if the game has stopped
    gameExit = False

    # This the distance traveled and the speed 
    xDistanceToMove = 0
    shipSpeed = 0 

    while not gameExit:
        
        # Here we are checking if someone pressed the close button on our game window to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            # Here we are checking to see if any buttons were pressed on keyboard to move the spaceship
            # We do this by changing the value of the xDistanceToMove and telling the ship to go there
            
            # Checking the down key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xDistanceToMove = -5
                elif event.key == pygame.K_RIGHT:
                    xDistanceToMove = 5
                    
            # Checking the left and right keys 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xDistanceToMove = 0
        
        # Here we are changing the x variable to the new x position so we can tell the spaceship to move there
        x = x + xDistanceToMove
        
        # Here we are changing the background of the game and the spaceship at its current location        
        gameDisplay.fill(white)
        spaceShip(x,y)
        
        # We quit the game if spaceship goes outside screen
        if x > displayWidth - shipLength or x < 0:
            gameExit = True 
        # Here we are showing the changes to our game screen        
        pygame.display.update()
        clock.tick(60)

# Lets run the game loop, we have to call the function
gameLoop()

# If we exit the loop means program ended then we close the game library
print('Goodbye') 
pygame.quit()
quit()


