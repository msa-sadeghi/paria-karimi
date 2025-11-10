import pygame
from pygame.sprite import Sprite
class Coffee(Sprite):
    def __init__(self, image_path, x,y, group):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)

    def update(self, player, score):
        if player.rect.colliderect(self.rect):
            self.kill()
            score += 1
        return score
    
    