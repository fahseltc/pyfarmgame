import CONSTANTS
import pygame
import os
import GAME_GLOBALS
from map.tile_map import TileMap
from game_loop import GameLoop

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,0)

pygame.init()
pygame.display.set_caption(CONSTANTS.TITLE)
pygame.display.set_mode(CONSTANTS.resolution)
GAME_GLOBALS.tile_map = TileMap()
GAME_GLOBALS.entities = []
gameloop = GameLoop()
clock = pygame.time.Clock()

gameloop.start()
