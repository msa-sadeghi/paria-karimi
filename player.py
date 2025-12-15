import pygame
from pygame.sprite import Sprite
import os
class Player(Sprite):
    def __init__(self,type, x, y):
        super().__init__()
        self.type = type
        self.animations = os.listdir(f"{self.type}")
        self.all_images = {}
        for animation in self.animations:
            self.all_images[animation] = []
            images_list = os.listdir(f"{self.type}/{animation}")
            for image in images_list:
                img = pygame.image.load(f"{self.type}/{animation}/{image}")
                img = pygame.transform.scale_by(img, 0.3)
                self.all_images[animation].append(img)
        self.image = self.all_images['Idle'][0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)