import pygame
pygame.init()
from player import Player
from obstacle import Obstacle
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

cat = Player('Cat', 300, 200)
crate_image = pygame.image.load("Object/Crate.png")
stone_image = pygame.image.load("Object/Stone.png")
obstacle_group = pygame.sprite.Group()

crate_width = crate_image.get_width()
stone_width = stone_image.get_width()
crate1 = Obstacle('crate',crate_image, 100, HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + crate_width, HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + 2 * crate_width, HEIGHT, obstacle_group)
stone1 = Obstacle('stone',stone_image, 700, HEIGHT, obstacle_group)
stone2 = Obstacle('stone',stone_image, 700 + stone_width , HEIGHT, obstacle_group)


scroll = 0
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    screen.fill("lightgreen")  
    cat.move(obstacle_group)
    if cat.rect.right > WIDTH - 200:
        scroll = -5
        cat.rect.right = WIDTH - 200
    elif cat.rect.left < 200:
        cat.rect.left = 200
        scroll = 4
    else:
        scroll = 0
    cat.draw(screen)
    obstacle_group.update(scroll)
    obstacle_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

