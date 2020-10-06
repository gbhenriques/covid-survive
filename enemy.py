import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/covid.png")
        self.image = pygame.transform.scale(self.image, [35, 35])
        self.rect = pygame.Rect(540, 360, 25, 25)

        self.rect.x = 1080 + random.randint(1, 400)
        self.rect.y = random.randint(150, 600)

        self.speed = 5 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/covid2.png")
        self.image = pygame.transform.scale(self.image, [35, 35])
        self.rect = pygame.Rect(540, 360, 25, 25)

        self.rect.x = 0 - random.randint(1, 400)
        self.rect.y = random.randint(150, 600)

        self.speed = 5 + random.random() * 2

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 1080:
            self.kill()