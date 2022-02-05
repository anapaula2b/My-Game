import pygame

class Sum(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/fanton.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(150, 250, 200, 200)

        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 2
        if keys[pygame.K_a]:
            self.rect.x -= 1
        
        if keys[pygame.K_w]:
            self.rect.y -= 1
        if keys[pygame.K_s]:
            self.rect.y += 1

        if self.rect.top < 0 :
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
    