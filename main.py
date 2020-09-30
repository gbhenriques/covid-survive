import pygame
from player import Player
from enemy import Enemy
from shot import Shot
import random

# iniciar o jogo
pygame.init()
display = pygame.display.set_mode([1080, 720])
pygame.display.set_caption("COVID SURVIVE")

# objetos

objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# background

bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("img/Mapa.png")
bg.image = pygame.transform.scale(bg.image, [1080, 720])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)

gameLoop = True
timer = 0
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newShot = Shot(objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center

        # update logic
        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.5:
                newEnemy = Enemy(objectGroup, enemyGroup)

        collisions = pygame.sprite.spritecollide(player, enemyGroup, False, pygame.sprite.collide_mask)

        if collisions:
            gameLoop = False

        hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True, pygame.sprite.collide_mask)

        # Draw
        objectGroup.draw(display)
        pygame.display.update()




