import pygame,sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (820,640)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bomberman")

loop = True

while loop:
    window.fill((0,0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()