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
        self.animation_state = 'Idle'
        self.frame_index = 0
        self.animate_time=0
        self.direction =  1
        self.yspeed = 0
        self.jump_state = False
        self.is_grounded = False
            


    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.direction == -1, False)
        surface.blit(img , self.rect)
        pygame.draw.rect(surface, "red", self.rect, 4)
        self.animate()

    def animate(self):
        if pygame.time.get_ticks() - self.animate_time > 150:
            self.frame_index += 1
            self.animate_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.all_images[self.animation_state]):
                self.frame_index = 0
            self.image = self.all_images[self.animation_state][self.frame_index]
    
    def move(self, group):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        
        # Handle horizontal movement input
        if keys[pygame.K_LEFT]:
            self.change_animation("Walk")
            self.direction = -1
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.change_animation("Walk")
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not self.jump_state:
            self.change_animation("Idle")

        
        self.rect.x += dx
        collided_obstacles = pygame.sprite.spritecollide(self, group, False)
        for obstacle in collided_obstacles:
            if obstacle.type == "crate" or obstacle.type == "stone":
                # Collision from right (moving left)
                if dx < 0:
                    self.rect.left = obstacle.rect.right
                # Collision from left (moving right)
                elif dx > 0:
                    self.rect.right = obstacle.rect.left

        # ========== JUMP INPUT ==========
        if keys[pygame.K_UP] and self.is_grounded:
            self.yspeed = -15
            self.jump_state = True
            self.change_animation("Jump")
            self.is_grounded = False
        
        # ========== GRAVITY ==========
        if not self.is_grounded:
            self.yspeed += 1
        dy = self.yspeed
        
        
        self.rect.y += dy
        
        # Check collision after Y movement
        self.is_grounded = False
        collided_obstacles = pygame.sprite.spritecollide(self, group, False)
        for obstacle in collided_obstacles:
            if obstacle.type == "crate" or obstacle.type == "stone":
                # Collision from above (falling down)
                if dy > 0:
                    self.rect.bottom = obstacle.rect.top
                    self.yspeed = 0
                    self.jump_state = False
                    self.is_grounded = True
                # Collision from below (jumping up)
                elif dy < 0:
                    self.rect.top = obstacle.rect.bottom
                    self.yspeed = 0

        # ========== GROUND COLLISION ==========
        if self.rect.bottom >= 640:
            self.rect.bottom = 640
            self.yspeed = 0
            self.jump_state = False
            self.is_grounded = True

    def change_animation(self, new_animation):
        if self.animation_state != new_animation:
            self.animation_state = new_animation
            self.frame_index = 0
            self.animate_time = pygame.time.get_ticks()
