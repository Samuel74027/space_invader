###################################################################
#                                                                 #
#               Program 1 - By Yen-Lin Lee                        #
#                last revised: 10/18/21                           #
#           You are died when your health is 0. Invader will      #
#           bounce around the screen. Try to kill all of them!    #
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
bullet_image = pygame.image.load('./picture/bullet.png')
invader_image = pygame.image.load('./picture/invader.png')
invader_image = pygame.transform.scale(invader_image, (55, 40))
spaceship_image = pygame.image.load('./picture/spaceship.png')
SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 55,40
spaceship_image = pygame.transform.scale(spaceship_image, (SPACESHIP_HEIGHT, SPACESHIP_WIDTH))
START_X, START_Y = (SCREEN_WIDTH - SPACESHIP_WIDTH)/2, (SCREEN_HEIGHT)/2

# class for spaceship
class Spaceship():
    def __init__(self, img, x, y, health):
        self.x = x
        self.y = y
        self.img = img
        self.health = health
    def move(self, event):
        delta_x = 0
        delta_y = 0
        if event == pygame.K_d:
            delta_x = 3
        elif event == pygame.K_a:
            delta_x = -3
        elif event == pygame.K_w:
            delta_y = 3
        elif event == pygame.K_s:
            delta_y = -3
        self.x += delta_x
        self.y += delta_y
    def stop_move(self, event):
        delta_x = 0
        delta_y = 0
        self.x += delta_x
        self.y = delta_y
    def update(self):
        screen.blit(self.img, (self.x, self.y))

spaceship1 = Spaceship(spaceship_image, (SCREEN_WIDTH - 55)/2, 500, 10)

# class for bullets
class Bullet():
    def __init__(self, bulletX, bulletY, img):
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.img = img
    def move(self, bulletState):
        if bulletState == True:
            delta_x = 0
            delta_y = -10
            self.bulletX += delta_x
            self.bulletY += delta_y
    def update(self):
        screen.blit(self.img, (self.bulletX, self.bulletY))

# code below are the code I developed but not used
""" class Block():
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

class Bomb():
    Bomb_list = []
    BombX = []
    BombY = []
    def __init__(self):
        pass
    def createBomb(self, bombX, bombY):
        self.Bomb_list.append(bomb_image)
        self.BombX.append(bombX)
        self.BombY.append(bombY)
    def move(self, bombState):
        if bombState == True:
            for i in range(0, len(self.Bomb_list)):
                delta_x = 0
                delta_y = 10
                self.BombY[i] += delta_y
                
    def update(self):
        for i in range(0, len(self.Bomb_list)):
            screen.blit(self.Bomb_list[i], (self.BombX[i], self.BombY[i]))

bombState = False """

# invader class
class Invader():
    Invader_list = []
    InvaderState = []
    InvaderX = []
    InvaderY = []
    xChangeList = []
    yChangeList = []
    def __init__(self, numOfInvaders):
        self.numOfInvaders = numOfInvaders
    def create_invader(self):
        for invader in range(self.numOfInvaders):
            x = random.randint(0, SCREEN_WIDTH - 55)
            y = random.randint(0, SCREEN_HEIGHT - 300)
            delta_x = 5
            delta_y = 7
            self.Invader_list.append(invader_image)
            self.InvaderX.append(x)
            self.InvaderY.append(y)
            self.xChangeList.append(delta_x)
            self.yChangeList.append(delta_y)
            self.InvaderState.append(True)
    def move(self):
        for i in range(len(self.Invader_list)):
            if self.InvaderX[i] <= 0:
                self.xChangeList[i] = 5
            elif self.InvaderX[i] >= SCREEN_WIDTH - 40:
                self.xChangeList[i] = -5
            if self.InvaderY[i] <= 0:
                self.yChangeList[i] = 7
            elif self.InvaderY[i] >= SCREEN_HEIGHT - 55:
                self.yChangeList[i] = -7
            delta_x = self.xChangeList[i]
            delta_y = self.yChangeList[i]
            self.InvaderX[i] += delta_x
            self.InvaderY[i] += delta_y
    def update(self):
        killedInvader = 0  
        for i in range(0, numOfInvaders):
            if self.InvaderState[i] == True:
                screen.blit(self.Invader_list[i], (self.InvaderX[i], self.InvaderY[i]))
                killedInvader += 1
        return killedInvader

# function for detecting collisions
def BulletCollision(bulletX, bulletY, invaderX, invaderY):
    xDifference = (bulletX - invaderX)**2
    yDifference = (bulletY - invaderY)**2
    dDifference = (xDifference + yDifference)**0.5
    if dDifference < 30:
        return True
    else:
        return False
    

def SpaceshipCollision(spaceX, spaceY, invaderX, invaderY):
    xDifference = (spaceX - invaderX)**2
    yDifference = (spaceY - invaderY)**2
    dDifference = (xDifference + yDifference)**0.5
    if dDifference < 20:
        return True
    else:
        return False

# the number of invaders can be changed using the variable "numOfInvaders" below
numOfInvaders = 5   
invaders = Invader(numOfInvaders)
invaders.create_invader()

# function for writing text on the screen
def Writetext(text, x, y, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(text, True, (255, 255, 255)) 
    textRect = text.get_rect()
    textRect.center = (x, y) 
    return (text, textRect)



bulletState = False
delta_x = 0
delta_y = 0
# Game loop
running = True
while running:
    # redraw game Screen
    screen.blit(background, (0, 0))
    block = pygame.Surface((50, 50))
    invaders.move()
    invaders.update()
    # code below are the code I developed but can't get it to work
    """ if bombState == True:
        bombs = Bomb()
        for i in range(0, numOfInvaders):
            bombs.createBomb(invaders.InvaderX[i], invaders.InvaderY[i])
        bombs.move(bombState)
        bombs.update()
        bombState = False
    else:
        bombState = True """
    # spaceship boundaries
    if spaceship1.x <= 0:
        spaceship1.x = 0
    if spaceship1.x >= SCREEN_WIDTH - 40:
        spaceship1.x = SCREEN_WIDTH - 40
    if spaceship1.y <= 0:
        spaceship1.y = 0
    if spaceship1.y >= SCREEN_HEIGHT - 55:
        spaceship1.y = SCREEN_HEIGHT - 55
    spaceship1.x += delta_x
    spaceship1.y += delta_y
    # spaceship control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                delta_x += 5
            if event.key == pygame.K_a:
                delta_x = -5
            if event.key == pygame.K_s:
                delta_y = 5
            if event.key == pygame.K_w:
                delta_y = -5
            if event.key == pygame.K_SPACE:
                bullet = Bullet(spaceship1.x + 10, spaceship1.y, bullet_image)
                bulletState = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                delta_x = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                delta_y = 0
    
    spaceship1.update()
    
    #fire bullet + detect for collisions
    if bulletState == True:
        bullet.move(bulletState)
        bullet.update()
        for i in range(0, numOfInvaders):
            if BulletCollision(bullet.bulletX, bullet.bulletY, invaders.InvaderX[i], invaders.InvaderY[i]):
                bulletState = False
                invaders.InvaderState[i] = False
    for i in range(0, numOfInvaders):
        if SpaceshipCollision(spaceship1.x, spaceship1.y, invaders.InvaderX[i], invaders.InvaderY[i]):
            spaceship1.health -= 1
                
    # print out health and points
    points = Writetext(f'Points: {numOfInvaders - invaders.update()}', 900, 50, 30)
    screen.blit(points[0], (points[1]))
    health = Writetext(f'Health: {spaceship1.health}', 900, 70, 30) 
    screen.blit(health[0], (health[1]))
    if numOfInvaders - invaders.update() == numOfInvaders:
        win = Writetext('You Win!!', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50)
        screen.blit(win[0], (win[1]))
    if spaceship1.health <= 0:
        loss = Writetext('You are died...', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50) 
        screen.blit(loss[0], loss[1]) 
        spaceship1.health = 0    
    pygame.display.update()