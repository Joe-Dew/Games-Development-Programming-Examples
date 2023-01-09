import pygame
import random
import battleV2
import menu

pygame.init()

surface = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Pokemon Showdown!")

white = (255, 255, 255)
black = (0, 0, 0)

def battle():
    battleV2.setup()

advance = False
tile_proceed = False
running = True
while running:
    if not advance:
        advance = menu.start_menu(surface)

    if not tile_proceed and advance:
        tile_proceed, advance = menu.intermediate(surface)
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()