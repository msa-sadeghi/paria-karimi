from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale_by(self.image,  0.3)
        self.rect = self.image.get_rect(topleft=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        # self.rect.x
        # self.rect.y