import pygame
from random import choice, randint

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./Ball/Ball.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400, randint(100, 300)))
        self.dx = choice([-7, 7])
        self.dy = choice([-6, 6])
    
    def movement(self, paddle):
        if paddle:
            self.dx *= -1

        if (self.rect.top <= 6 or self.rect.bottom >= 394) and self.rect.left > 0 and self.rect.right < 800:
            self.dy *= -1
            
        self.rect.x += self.dx
        self.rect.y += self.dy
    
    def reset_game(self, reset):
        if reset:
            self.rect.center = (400, randint(100, 300))

    def update(self, paddle=False, reset=False):
        self.movement(paddle)
        self.reset_game(reset)