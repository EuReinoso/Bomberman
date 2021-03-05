import pygame,sys
from pygame.locals import *
from player import Player

pygame.init()

WINDOW_SIZE = (820,640)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bomberman")

loop = True

fps = pygame.time.Clock()

player = Player(50,50,20,20)

while loop:
    window.fill((0,0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player.direction(event)
        

    player.draw(window)
    player.update()
    pygame.display.update()
    fps.tick(60)