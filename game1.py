import pygame
from player import Player
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game 1")


ninja = Player((100, 200))

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((125, 15, 255))
    pygame.draw.circle(screen, (0, 255, 0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2),200)
    ninja.draw(screen)
    pygame.display.update()