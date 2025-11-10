from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale_by(self.image,  0.3)
        self.rect = self.image.get_rect(topleft=pos)
        self.velovity = 5
        self.gravity = 9.8
        self.direction = "right"

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.direction == "left", False)
        screen.blit(img, self.rect)

    def move(self, keys, width, height):
        dy = 0
        if self.rect.bottom + dy >= height:
            self.gravity = 0
            dy = height - self.rect.bottom
        if keys[pygame.K_UP]:
            self.gravity = -10        
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.x += 10
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.x -= 10
        self.gravity += 1
        dy += self.gravity
        self.rect.y += dy