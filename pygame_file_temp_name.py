import pygame
import sys
from pygame.locals import *

pygame.init()

#CONSTANTS
DISPLAYSURF = pygame.display.set_mode((300, 300))

#game loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()