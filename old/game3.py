import pygame
pygame.init()


WIDTH = 600
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))


running = True
x = 100
y = 100

FPS = 60
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         y -= 10
        #     elif event.key == pygame.K_DOWN:
        #         y += 10
        #     if event.key == pygame.K_LEFT:
        #         x -= 10
        #     elif event.key == pygame.K_RIGHT:
        #         x += 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x + 50 < WIDTH:
        x += 10
    elif keys[pygame.K_LEFT] and x > 0:
        x -= 10
    elif keys[pygame.K_UP] and y > 0:
        y -= 10
    elif keys[pygame.K_DOWN] and y  + 50< HEIGHT:
        y += 10
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, "green", (x, y, 50, 50), 3)
    pygame.display.update()