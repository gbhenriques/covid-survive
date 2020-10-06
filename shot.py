import pygame

class Shot(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/seringaD.png")
        self.image = pygame.transform.scale(self.image, [60, 60])
        self.rect = self.image.get_rect()

        self.speed = 15

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 1080:
            self.kill()

class Shot2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("img/seringaE.png")
        self.image = pygame.transform.scale(self.image, [60, 60])
        self.rect = self.image.get_rect()

        self.speed = 15

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()