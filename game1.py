import pygame
from player import Player
from coffee import Coffee
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game 1")
score = 0
font = pygame.font.Font("ARCADECLASSIC.TTF", 22)
score_text = font.render(f"score  {score}", True, "green")


RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (0, 0, 255)

current = RED_COLOR
ninja = Player((100, 80))
coffee_group = pygame.sprite.Group()
coffee1 = Coffee("coffee.png", 300, 150, coffee_group)
coffee1 = Coffee("coffee.png", 400, 250, coffee_group)
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
    score_text = font.render(f"score  {score}", True, "green")

    keys = pygame.key.get_pressed()
    ninja.move(keys, SCREEN_WIDTH, SCREEN_HEIGHT)
    ninja.draw(screen)
    coffee_group.draw(screen)
    score =  coffee_group.update(ninja, score)
    screen.blit(score_text, (10, 10))

    
    pygame.display.update()
