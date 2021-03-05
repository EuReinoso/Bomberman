import pygame
from pygame.locals import *

class Bomb:
    def __init__(self,x,y):

        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(x,y,self.width,self.height)

        self.color = (255,0,0)


    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

