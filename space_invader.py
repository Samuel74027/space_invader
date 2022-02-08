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


pygame.init()

#Game image constants
background = pygame.image.load('./picture/starfield.png')
invader = pygame.image.load('./picture/invader.png')
spaceship_image = pygame.image.load('./picture/spaceship.png')
SPACESHIP_WIDTH, SPACESHIP_LENGTH = 55, 40
spaceship = pygame.transform.scale(spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_LENGTH))
spaceship.blit(spaceship, (0,0))

def gameControl():
   for event in pygame.event.get():
       spaceship.blit
       if event.type == pygame.key.get_pressed() and spaceship.x > 0:
           spaceship.x -= 3
       if event.type == pygame.key.get_pressed():
            spaceship.x += 3
        
# Game loop
running = True
while running:
    # redraw game Screen
    screen.fill((BLACK))
    screen.blit(background, (0,0))
    gameControl()
    #input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()