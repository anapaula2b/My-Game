import pygame


class Tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/raiolaser.png')
        self.image = pygame.transform.scale(self.image, [50, 25])
        self.rect = self.image.get_rect()

        self.speed = 6

        
    def update(self, *args):
        self.rect.x += self.speed 

        if self.rect.left < 0: 
            self.kill()