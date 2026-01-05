import pygame
pygame.init()
from player import Player
from obstacle import Obstacle
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

cat = Player('Cat', 200, 200)
crate_image = pygame.image.load("Object/Crate.png")
stone_image = pygame.image.load("Object/Stone.png")
obstacle_group = pygame.sprite.Group()
crate = Obstacle('crate',crate_image, 100, HEIGHT, obstacle_group)
stone = Obstacle('stone',stone_image, 700, HEIGHT, obstacle_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    screen.fill("lightgreen")  
    CLOCK.tick(FPS)
    cat.draw(screen)
    cat.move()
    obstacle_group.draw(screen)
    obstacle_group.update()
    pygame.display.update()

