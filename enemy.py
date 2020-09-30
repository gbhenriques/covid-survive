import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/covid.png")
        self.image = pygame.transform.scale(self.image, [25, 25])
        self.rect = pygame.Rect(540, 360, 25, 25)

        self.rect.x = 1080 + random.randint(1, 400)
        self.rect.y = random.randint(100, 600)

        self.speed = 5 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()