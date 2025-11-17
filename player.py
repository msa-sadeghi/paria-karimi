from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frames = []
        for i in range(10):
            img = pygame.image.load(f"images/Idle/Idle__00{i}.png")
            img = pygame.transform.scale_by(img,  0.3)
            self.frames.append(img)

        self.current_frame =  0
        self.image = self.frames[self.current_frame]        
        self.rect = self.image.get_rect(topleft=pos)
        self.velovity = 5
        self.gravity = 9.8
        self.direction = "right"
        self.last_time = 0

    def animation(self):
        if pygame.time.get_ticks() - self.last_time > 100:
            self.last_time =  pygame.time.get_ticks()
            self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]


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