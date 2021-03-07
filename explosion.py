import pygame
from pygame.locals import *

class Explosion:
    def __init__(self,x,y):
        self.radius = 10
        self.size = 20
        self.x = x
        self.y = y

        self.color = (0,255,0)

        self.body = []

        self.time = 120
        self.tick = 0
        self.time_out = False

        self.body_construct()

    def update(self):
        self.explosion_time()

    def body_construct(self):
        for i in range(self.radius):
            self.body.append(pygame.Rect(self.x + (i*self.size),self.y,self.size,self.size))
            self.body.append(pygame.Rect(self.x - (i*self.size),self.y,self.size,self.size))
            self.body.append(pygame.Rect(self.x,self.y + (i*self.size),self.size,self.size))
            self.body.append(pygame.Rect(self.x,self.y - (i*self.size),self.size,self.size))
    
    def draw(self,window):
        for rect in self.body:
            pygame.draw.rect(window,self.color,rect)

    def explosion_time(self):
        self.tick += 1

        if self.tick >= self.time:
            self.time_out = True


