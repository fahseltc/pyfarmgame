import CONSTANTS
import pygame
import os
from game_loop import GameLoop

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,0)

pygame.init()
pygame.display.set_caption(CONSTANTS.TITLE)
gameloop = GameLoop()
clock = pygame.time.Clock()

gameloop.start()
