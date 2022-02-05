import pygame

class Cenarios(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/solo.jpg')
        self.image = pygame.transform.scale(self.image, [840, 130])
        self.rect = pygame.Rect(0, 350, 0, 0)
