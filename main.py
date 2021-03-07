import pygame,sys
from pygame.locals import *
from player import Player
from bomb import Bomb
from explosion import Explosion

pygame.init()

WINDOW_SIZE = (640,480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Bomberman")

#map
def load_map(path):
    f = open('map' + path + '.txt','r')
    data = f.read()
    f.close()

    data = data.split("\n")
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

main_map = load_map('1')

TILE_SIZE = 64
TILE_COLOR = (18,10,143)

fps = pygame.time.Clock()

player = Player(50,50,32,32)

bomb_list = []
def put_bomb():
    bomb_list.append(Bomb(player.rect.x,player.rect.y))

explosion_list = []

loop = True
while loop:
    window.fill((210,180,240))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                put_bomb()

        player.direction(event)
    
    #draw map
    y = 0
    for row in main_map:
        x = 0
        for tile in row:
            if tile == '1':
                pygame.draw.rect(window,TILE_COLOR,(x * TILE_SIZE,10 + (y * TILE_SIZE),TILE_SIZE,TILE_SIZE))

            x += 1
        y += 1

    #draw bomb
    for bomb in bomb_list:
        bomb.draw(window)

    #update bombs
    for bomb in bomb_list:
        bomb.update()
        
        if bomb.time_out: 
            bomb_list.remove(bomb)
            explosion_list.append(Explosion(bomb.rect.x,bomb.rect.y))

    #draw explosion
    for explosion in explosion_list:
        explosion.draw(window)

    #update explosions
    for explosion in explosion_list:
        explosion.update()

        if explosion.time_out == True:
            explosion_list.remove(explosion)
            

    player.draw(window)
    player.update()
    pygame.display.update()
    fps.tick(60)


