import pygame

pygame.init()

class Player:
    def __init__ (self,x,y,width,height):

        self.rect = pygame.Rect(x,y,width,height)

        self.color = (255,0,0)

        self.vel = 3

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def update(self):
        self.move()

    def draw(self, window):
        pygame.draw.rect(window,self.color,self.rect)

    def move(self):
        if self.right:
            self.rect.x += self.vel
        if self.left:
            self.rect.x -= self.vel
        if self.up:
            self.rect.y -= self.vel
        if self.down:
            self.rect.y += self.vel

    def direction(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_UP:
                self.up = True
            if event.key == pygame.K_DOWN:
                self.down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_UP:
                self.up = False
            if event.key == pygame.K_DOWN:
                self.down = False