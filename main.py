import pygame
pygame.init()
from player import Player
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()

cat = Player('Cat', 200, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    screen.fill("lightgreen")  
    CLOCK.tick(FPS)
    cat.draw(screen)
    pygame.display.update()

