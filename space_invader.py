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
import random

# Screen constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
BLACK = (0, 0, 0)
#Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invader')


pygame.init()

#Game image constants
random_x = random.randint(0,SCREEN_WIDTH - 55)
random_y = random.randint(0,SCREEN_HEIGHT - 40)
background = pygame.image.load('./picture/starfield.png')
invader_image = pygame.image.load('./picture/invader.png')
invader_image = pygame.transform.scale(invader_image, (55, 40))
spaceship_image = pygame.image.load('./picture/spaceship.png')
SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 55,40
spaceship_image = pygame.transform.scale(spaceship_image, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH))
START_X, START_Y = (SCREEN_WIDTH - SPACESHIP_WIDTH)/2, (SCREEN_HEIGHT)/2

class Element():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Spaceship(Element):
    def __init__(self, img, x, y):
        super().__init__(x, y)
        self.img = img
    def move(self, event):
        if event == pygame.K_d:
            self.x += 3
        elif event == pygame.K_a:
            self.x -= 3
        elif event == pygame.K_w:
            self.y += 3
        elif event == pygame.K_s:
            self.y -= 3
    def stop_move(self, event):
        if event == pygame.K_d or event == pygame.K_a:
            self.x = 0

class Block(Element):
    BLOCK_LIST = []
    XSPEED = 5
    YSPEED = 3
    def __init__(self, x, y):
        super().__init__(x, y)
    def add_block(self):
        RED = random.randint(0, 255)
        GREEN = random.randint(0, 255)
        BLUE = random.randint(0, 255)
        new_block = pygame.Surface((50, 50))
        new_block.fill((RED, GREEN, BLUE))
        self.BLOCK_LIST.append(new_block)
        return self.BLOCK_LIST
    def move_block(self):
        for block in self.BLOCK_LIST:
            block.get_rect().top += self.YSPEED
            block.get_rect().left += self.XSPEED
            screen.blit(block)


spaceship = Spaceship(spaceship_image, START_X, START_Y)
# Starting Coordinate


delta_x = 0
def Invader(img, x, y):
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    # redraw game Screen
    screen.blit(background, (0, 0))
    screen.blit(invader_image, (random_x, random_y))
    block = pygame.Surface((50, 50))
    block.fill((255, 0, 0))
    screen.blit(block, (random_x, random_y))
    #input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            spaceship.move(event.key)
        if event.type == pygame.KEYUP:
            spaceship.stop_move(event.key)

    pygame.display.update()

# add boundaries and moving opponent to the screen, make the countrol system into the function and make the code organize
