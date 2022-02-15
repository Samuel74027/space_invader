###################################################################
#                                                                 #
#               Program 1 - By Yen-Lin Lee                        #
#                last revised: 10/18/21                           #
#           This program can prints out user's favorite number    #
#                                                                 #
#                                                                 #
###################################################################
#Import library
from ast import Num
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
    def update(self):
        screen.blit(self.img, (self.x, self.y))

class Block():
    BLOCK_LIST = []
    X_LIST = []
    Y_LIST = []
    COLOR_LIST = []
    XSPEED = 5
    YSPEED = 3
    num_of_blocks = 8
    def __init__(self):
        pass
    def create_block(self):
        i = 0
        for i in range(self.num_of_blocks):
            RED = random.randint(0, 255)
            GREEN = random.randint(0, 255)
            BLUE = random.randint(0, 255)
            color = (RED,GREEN,BLUE)
            self.COLOR_LIST.append(color)
            new_block = pygame.Surface((50, 50))
            new_block.fill((RED, GREEN, BLUE))
            self.BLOCK_LIST.append(new_block)
            block_x = random.randint(0,SCREEN_WIDTH - 55)
            block_y = random.randint(0,SCREEN_HEIGHT - 40)
            self.X_LIST.append(block_x)
            self.Y_LIST.append(block_y)
    def move_block(self):
        for i in range(self.num_of_blocks):
            self.X_LIST[i] += self.XSPEED
            self.Y_LIST[i] += self.YSPEED
            if self.Y_LIST[i] < 0 or self.Y_LIST[i] > SCREEN_HEIGHT:
                self.Y_LIST[i] -= self.YSPEED
            if self.X_LIST[i]  < 0 or self.X_LIST[i]  > SCREEN_WIDTH:
                self.X_LIST[i] -= self.XSPEED
    def update(self):
        for i in range(self.num_of_blocks):
            screen.blit(self.BLOCK_LIST[i], (self.X_LIST[i], self.Y_LIST[i]))
                
 
class Invader():
    Invader_list = []
    InvaderX = []
    InvaderY = []
    XCHANGE = 5
    YCHANGE = 50
    def __init__(self, numOfInvaders):
        self.numOfInvaders = numOfInvaders
    def create_invader(self):
        for invader in range(self.numOfInvaders):
            x = 0
            self.Invader_list.append(invader_image)
            self.InvaderX.append(x)
            self.InvaderY.append(0)
            x += 100
    def move(self):
        for i in range(len(self.Invader_list)):
            if i == 0:
                pass
            else:
                pygame.time.delay(50)
            self.InvaderX[i] += self.XCHANGE
            if self.InvaderX[i] <= 0:
                self.XCHANGE = 5
                self.InvaderY[i] += self.YCHANGE
            elif self.InvaderX[i] >= SCREEN_WIDTH:
                self.XCHANGE = -5
                self.InvaderY[i] += self.YCHANGE
    def update(self):
        for i in range(self.numOfInvaders):
            screen.blit(self.Invader_list[i], (self.InvaderX[i], self.InvaderY[i]))
    
invaders = Invader(2)
invaders.create_invader()  
               
blocks = Block()
blocks.create_block()
spaceship = Spaceship(spaceship_image, START_X, START_Y)
# Starting Coordinate


delta_x = 1
block_x = 0
def Invader(img, x, y):
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    # redraw game Screen
    screen.blit(background, (0, 0))
    block = pygame.Surface((50, 50))
    invaders.move()
    invaders.update()
    #input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            spaceship.move(event.key)
            print('move up')
        if event.type == pygame.KEYUP:
            spaceship.stop_move(event.key)
    spaceship.update()
    pygame.display.update()

# add boundaries and moving opponent to the screen, make the countrol system into the function and make the code organize
