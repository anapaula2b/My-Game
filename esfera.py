import pygame
import random

class Esfera(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/esfera.png')
        self.image = pygame.transform.scale(self.image, [60, 60])
        self.rect = self.image.get_rect()

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(2, 400)

        self.speed = 1 + random.random() * 4

        
    def update(self, *args):
        self.rect.x -= self.speed 

        if self.rect.right < 0: 
            self.kill()
    