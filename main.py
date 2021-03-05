import pygame,sys
from pygame.locals import *
from player import Player
from bomb import Bomb

pygame.init()

WINDOW_SIZE = (820,640)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bomberman")

loop = True

fps = pygame.time.Clock()

player = Player(50,50,30,30)

bomb_list = []
def put_bomb():
    bomb_list.append(Bomb(player.rect.x,player.rect.y))

while loop:
    window.fill((0,0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                put_bomb()

        player.direction(event)
        
    
    #draw bombs
    for bomb in bomb_list:
        bomb.draw(window)

    #update bombs
    for bomb in bomb_list:
        bomb.update()
        if bomb.time_out: 
            bomb_list.remove(bomb)

    player.draw(window)
    player.update()
    pygame.display.update()
    fps.tick(60)


