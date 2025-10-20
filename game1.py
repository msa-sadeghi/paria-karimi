import pygame
from player import Player
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game 1")

RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (0, 0, 255)

current = RED_COLOR
ninja = Player((100, 80))
FPS = 60
clock = pygame.time.Clock()
running = True
while running == True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
    screen.fill(current)

    keys = pygame.key.get_pressed()
    ninja.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
    ninja.draw(screen)
    pygame.display.update()