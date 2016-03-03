import pygame
from pygame.locals import *

pygame.init()

width = 640
height = 480

GREEN = (0, 168, 42)
WHITE = (0, 0, 0)

screen = pygame.display.set_mode((width,height))
keys = {K_a:0, K_d:0, K_w:0, K_s:0, }

X = 0
Y = 1
playerPos = [320, 240]
playerSize = 10
playerSpeed = 3
player = pygame.Surface((playerSize, playerSize))
player.fill(GREEN)

xMinMargin = 5
xMaxMargin = width - playerSize
yMinMargin = 5
yMaxMargin = height - playerSize

while True:
    screen.fill(WHITE)
    screen.blit(player, playerPos)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = playerSpeed
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.QUIT:             #The user quit
            pygame.quit()

    xMaxMargin = width - playerSize
    yMaxMargin = height - playerSize
    
    xUpdated = playerPos[X] - keys[K_a] + keys[K_d]
    yUpdated = playerPos[Y] - keys[K_w] + keys[K_s]
    if xMinMargin <= xUpdated <= xMaxMargin:
        playerPos[X] = xUpdated
    if yMinMargin <= yUpdated <= yMaxMargin:
        playerPos[Y] = yUpdated

    pygame.display.flip()
