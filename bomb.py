import pygame
from pygame.locals import *

class Bomb:
    def __init__(self,x,y):

        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(x,y,self.width,self.height)

        self.color = (255,0,0)

        self.time = 120
        self.tick = 0

        self.time_out = False

    def update(self):
        self.explode()

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

    def explode(self):
        self.tick += 1

        if self.tick == self.time:
            self.time_out = True

