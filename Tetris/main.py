import pygame
from settings import FPS, WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400  
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.time.Clock().tick(FPS)