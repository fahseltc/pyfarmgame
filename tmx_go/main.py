import pygame
import pyscroll
from tmx_loader import TmxLoader
from pytmx.util_pygame import load_pygame

# https://github.com/bitcraft/pyscroll
# https://github.com/bitcraft/PyTMX


RESOLUTION = (800, 800)
pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
loader = TmxLoader('../assets/tmx/map.tmx')

while True:
    screen.fill((0,0,0))

    for tile in loader.tiles:
        screen.blit(tile.image, tile.position)

    pygame.display.flip()
