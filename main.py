import CONSTANTS
import pygame
import os
from game_loop import GameLoop

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,0)


gameloop = GameLoop()
pygame.init()
pygame.display.set_caption(CONSTANTS.TITLE)
clock = pygame.time.Clock()

gameloop.start()
