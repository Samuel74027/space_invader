###################################################################
#                                                                 #
#               Program 1 - By Yen-Lin Lee                        #
#                last revised: 10/18/21                           #
#           This program can prints out user's favorite number    #        
#                                                                 #
#                                                                 #
###################################################################
#Import library
import pygame, math, sys


# Screen constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
BLACK = (0, 0, 0)
#Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invader')


pygame.init()

#Game image constants
background = pygame.image.load('./picture/starfield.png')
invader = pygame.image.load('./picture/invader.png')
spaceship_image = pygame.image.load('./picture/spaceship.png')
SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 55,40
START_X, START_Y = (SCREEN_WIDTH - SPACESHIP_WIDTH)/2, (SCREEN_HEIGHT)/2
spaceship = pygame.transform.rotate(spaceship_image, 180)
spaceship_position = pygame.Rect(START_X, START_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


# Starting Coordinate

def shipControl(event):
    if event == pygame.K_d:
        spaceship_position.x += 3 
        print("Player moved right!")
    elif event == pygame.K_a:
        spaceship_position.x -= 3
        print("Player moved left!")
    elif event == pygame.K_w:
        spaceship_position.y += 3
        print("Player moved up!")
    elif event == pygame.K_s:
        spaceship_position.y -= 3
        print("Player moved down!")

# Game loop
running = True
while running:
    # redraw game Screen
    screen.blit(background, (0, 0))
    screen.blit(spaceship, (spaceship_position.x, spaceship_position.y))
    #input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            shipControl(event.key)
    pygame.display.update()