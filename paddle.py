import pygame
from random import choice

class Paddle_Left(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Paddle/normal.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0, 160))
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 6:
            self.rect.y -= 7
        
        if keys[pygame.K_s] and self.rect.bottom < 394:
            self.rect.y += 7
    
    def update(self):
        self.movement()

class Paddle_Right(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Paddle/normal.png').convert_alpha()
        self.rect = self.image.get_rect(topright = (800, 160))
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_i] and self.rect.top > 6:
            self.rect.y -= 7
        
        if keys[pygame.K_k] and self.rect.bottom < 394:
            self.rect.y += 7
    
    def update(self):
        self.movement()