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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, keys, width, height):
        # self.rect.x += self.velovity

        # if self.rect.x + self.rect.size[0] >= width:
        #     self.velovity = -self.velovity
        #     self.image = pygame.transform.flip(self.image, True, False)

        # if self.rect.x <= 0:
        #     self.velovity = -self.velovity
        #     self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.bottom >= height:
            self.gravity = 0


        self.rect.y += self.gravity



        # if keys[pygame.K_UP]:
        #     self.rect.y -= 10
        # elif keys[pygame.K_DOWN]:
        #     self.rect.y += 10
        # if keys[pygame.K_RIGHT]:
        #     self.rect.x += 10
        # elif keys[pygame.K_LEFT]:
        #     self.rect.x -= 10