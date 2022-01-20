###################################################################
#                                                                 #
#               Program 1 - By Yen-Lin Lee                        #
#                last revised: 10/18/21                           #
#           This program can prints out user's favorite number    #        
#                                                                 #
#                                                                 #
###################################################################
#Import library
import pygame
import math

# Screen constants
XMODE, YMODE = 800, 600
BLACK = (0, 0, 0)

pygame.init()

#Game image constants
background = pygame.image.load('./picture/starfield.png')
invader = pygame.image.load('./picture/invader.png')

#Setup Screen
screen = pygame.display.set_mode((XMODE, YMODE))

# Game loop
running = True
while running:
    # redraw game Screen
    screen.fill((BLACK))
    screen.blit(background, (0, 0))
    screen.blit(invader, (100, 100))
    #input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()