from pygame.sprite import Sprite
import pygame

class Obstacle(Sprite):
    def __init__(self,type, image, x,y, group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(bottomleft=(x,y))
        group.add(self)
        self.type = type

    def update(self, scroll):
        self.rect.x += scroll