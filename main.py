import pygame
pygame.init()
from player import Player
from obstacle import Obstacle
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

cat = Player('Cat', 300, 200)
crate_image = pygame.image.load("Object/Crate.png")
stone_image = pygame.image.load("Object/Stone.png")
obstacle_group = pygame.sprite.Group()
crate1 = Obstacle('crate',crate_image, 100, HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + crate_image.get_size()[0], HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + 2 *crate_image.get_size()[0], HEIGHT, obstacle_group)
crate3 = Obstacle('crate',crate_image, 100 + 2 *crate_image.get_size()[0], HEIGHT, obstacle_group)
# crate3 = Obstacle('crate',crate_image, 100 + 2 *crate_image.get_size()[0], HEIGHT - crate_image.get_size()[1], obstacle_group)
stone1 = Obstacle('stone',stone_image, 700, HEIGHT, obstacle_group)
stone2 = Obstacle('stone',stone_image, 700 + stone_image.get_size()[0] , HEIGHT, obstacle_group)


scroll = 0
scroll_count = 1
FPS = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    screen.fill("lightgreen")  
    CLOCK.tick(FPS)

    if cat.rect.right >= scroll_count * WIDTH:
        scroll = -100
        scroll_count += .2
    

    elif cat.rect.left < (scroll_count - 1) * WIDTH and  cat.rect.left > 0:
        scroll_count -= .2
        scroll = 100
    else:
        scroll = 0

    cat.draw(screen)
    cat.move(obstacle_group)
    obstacle_group.draw(screen)
    obstacle_group.update(scroll)
    pygame.display.update()
    clock.tick(FPS)

