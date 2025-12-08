import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
user_text = ''
color_active = pygame.Color("lightskyblue")
color_passive = pygame.Color("gray")
color = color_passive
input_rect = pygame.Rect(150, 200, 200, 40)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False 
    pygame.draw.rect(screen, color, input_rect, 2)
    
    CLOCK.tick(FPS)
    pygame.display.update()