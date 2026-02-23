import pygame
pygame.init()
import random
from player import Player
from obstacle import Obstacle
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))


cat = Player('Cat', 300, 200)
score_font = pygame.font.Font("ARCADECLASSIC.TTF", 22)
score_text = score_font.render(f"Score  {cat.score}", True, "white")
crate_image = pygame.image.load("Object/Crate.png")
stone_image = pygame.image.load("Object/Stone.png")
crystal_image = pygame.image.load("Object/Crystal.png")
obstacle_group = pygame.sprite.Group()

crate_width = crate_image.get_width()
stone_width = stone_image.get_width()
crystal_width = crystal_image.get_width()
crate1 = Obstacle('crate',crate_image, 100, HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + crate_width, HEIGHT, obstacle_group)
crate2 = Obstacle('crate',crate_image, 100 + 2 * crate_width, HEIGHT, obstacle_group)
stone1 = Obstacle('stone',stone_image, 700, HEIGHT, obstacle_group)
stone2 = Obstacle('stone',stone_image, 700 + stone_width , HEIGHT, obstacle_group)
crystal1 = Obstacle('crystal',crystal_image, 1000 + crystal_width , HEIGHT, obstacle_group)
crystal1 = Obstacle('crystal',crystal_image, 2000 + crystal_width , HEIGHT, obstacle_group)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
scroll = 0
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    screen.fill((r,g,b)) 
    score_text = score_font.render(f"Score  {cat.score}", True, "white")
    screen.blit(score_text, (20, 20)) 
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

