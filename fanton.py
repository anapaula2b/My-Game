import pygame

class Fanton(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/fanton.png')
        self.image = pygame.transform.scale(self.image, [95, 100])
        self.rect = pygame.Rect(150, 250, 200, 200)

        self.speed = 0
        self.acceleration = 0.7

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2

        if self.rect.top < 0 :
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
    