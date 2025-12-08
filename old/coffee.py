import pygame
from pygame.sprite import Sprite
class Coffee(Sprite):
    def __init__(self, image_path, x,y, group):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.sound = pygame.mixer.Sound("sound.wav")

    def check_collision(self, player, score):
        
        if player.rect.colliderect(self.rect):
            self.kill()
            score += 1
            self.sound.play()
        return score
    
    