import pygame
import os 
import random
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
pygame.display.set_caption('Duck Dodger')

# Crashing sound
# crashSound = pygame.mixer.Sound("crash.wav");

# Defining some colors for use in the game
black = (0,0,0)
white = (255, 255, 255)  # these represent colors for red blue green which can can take values from 0 to 255
red = (200, 0, 0)
brightRed = (255, 0, 0)
green = (0, 200, 0)
brightGreen = (0, 255, 0)
blockColor = (50, 200, 250) 

# Clock used to keep track of the game events
clock = pygame.time.Clock()

# Lets load an image for our game spaceship and for the game icon
spaceshipImg = pygame.image.load(str(os.getcwd()) + '/spaceship.jpg')
gameIcon = pygame.image.load(str(os.getcwd()) + '/spaceshipIcon.jpg')
# Lets choose a size for the spaceship  
shipLength = 25

# Pausing variable
pause = False 

def ducksDodged(count):
    """ Keeps track of ducks being dodged """
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged:" + str(count), True, black)
    gameDisplay.blit(text,(0,0))
    
def ducks(duckX, duckY, duckW, duckH, color):
    """ Creates a rectangular obstacle for game """
    pygame.draw.rect(gameDisplay, color, [duckX, duckY, duckW, duckH])

def spaceShip(x,y):
    """ This is a function that will display our spaceship at a x and y position
"""
    gameDisplay.blit(spaceshipImg, (x,y)) 
    
def drawDucks(duckSize):
   """ This function draws ducks of different sizes using shapes """
   pass #TODO drawduck 

def textObjects(text, font):
    """ Creates the objects to draw for our screen """
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
   # pygame.mixer.Sound.play(crashSound)
   # pygame.mixer.music.stop()
    
    largeText = pygame.font.SysFont("comicsansms", 115)
    textSurf, textRect = textObjects("You Crashed", largeText)
    textRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(textSurf, textRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Play Again", 150, 450, 100, 50, green, brightGreen, gameLoop)
        button("Quit", 550, 450, 100, 50, red, brightRed, quitGame)
        
        pygame.display.update()
        clock.tick(15)
        
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if (x+w) > mouse[0] > x and y+h > mouse[1] > y: 
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = textObjects(msg, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        gameDisplay.blit(textSurf, textRect)
        
def quitGame():
    pygame.quit()
    quit()
    
def unPause():
    global pause
    # pygame.mixer.music.unpause()
    pause = False 
    
def paused():
    # pygame.mixer.music.pause()
    
    largeText = pygame.font.SysFont("comicsansms", 115)
    textSurf, textRect = textObjects("Paused", largeText)
    textRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(textSurf, textRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        
        button("Continue", 150, 450, 100, 50, green, brightGreen, unpause)
        button("Quit", 550, 450, 100, 50, red, brightRed, quitGame)
        
        pygame.display.update()
        clock.tick(15)

def gameIntro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        textSurf, textRect = textObjects("Duck Dodger", largeText)
        textRect.center = ((displayWidth/2), (displayHeight/2))
        gameDisplay.blit(textSurf, textRect)
        
        button("GO!", 150, 450, 100, 50, green, brightGreen, gameLoop)
        button("Quit", 550, 450, 100, 50, red, brightRed, quitGame)
        
        pygame.display.update()
        clock.tick(15)
        

def gameLoop():
    """  This a function for the game loop (to keep running)
"""
    global pause
    
    # pygame.mixer.music.load('jazz.wav')
    # pygame.mixer.music.play(-1)
    
    duckStartX = random.randrange(0, displayWidth)
    duckStartY = -600
    duckSpeed = 4
    duckWidth = 50
    duckHeight = 50
    
    duckCount =  1
    
    dodged = 0
    # This is the intial positioning of the sprite(the name of an image for 2D games)    
    x = (displayWidth) * 0.45
    y = (displayHeight) * 0.5 
    
    # Used for checking if the game has stopped
    gameExit = False

    # This the distance traveled and the speed 
    xDistanceToMove = 0
    shipSpeed = 0 
    x_change = 0 

    while not gameExit:
        
        # Here we are checking if someone pressed the close button on our game window to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        ducks(duckStartX, duckStartY, duckWidth, duckHeight, blockColor)
 
 
        
        duckStartY += duckSpeed
        spaceShip(x,y)
        ducksDodged(dodged)
 
        if x > displayWidth - shipLength or x < 0:
            crash()
 
        if duckStartY > displayHeight:
            duckStartY = 0 - duckHeight
            duckStartX = random.randrange(0,displayWidth)
            dodged += 1
            duckSpeed += 1
            duckWidth += (dodged * 1.2)
 
        if y < duckStartY+duckHeight:
            print('y crossover')
 
            if x > duckStartX and x < duckStartX + duckWidth or x+shipLength > duckStartX and x + shipLength < duckStartX+duckWidth:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

gameIntro()
gameLoop()
print("Goodbye my Friend!")
quitGame()