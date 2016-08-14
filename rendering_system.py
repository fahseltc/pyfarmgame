import CONSTANTS
import pygame
from pygame.locals import *
import utils

from player import Player

class RenderingSystem:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(CONSTANTS.resolution)

        if pygame.font:
            self.font = pygame.font.Font(None, 24)
            self.bigfont = pygame.font.Font(None, 100)

    def render(self, entities, tile_map):
        self.screen.fill(CONSTANTS.BLACK)

        # Draw the map
        for y in range(0, tile_map.height):
            for x in range(0, tile_map.width):
                rect = self.make_rect(x,y)
                tile = tile_map.matrix[x,y]
                color = CONSTANTS.WHITE
                if(tile == 0):
                    color = CONSTANTS.WHITE
                    char = '#'
                elif(tile == 1):
                    color = CONSTANTS.GREEN
                    char = '.'
                elif(tile == 2):
                    color = CONSTANTS.BLUE
                    char = '.'

                text = self.bigfont.render(char, 1, CONSTANTS.WHITE)
                textpos = text.get_rect(centerx=rect.x + 32, centery=rect.y + 32)
                self.screen.blit(text, textpos)

                # tile outlines
                #pygame.draw.rect(self.screen, color, rect, 1)


                # text = self.font.render("(%d, %d)" %(x, y), 1, (140,140,140))
                # textpos = text.get_rect(centerx=rect.x + 32, centery=rect.y + 32)
                # self.screen.blit(text, textpos)

        # Draw the entities
        for entity in entities:
            color = CONSTANTS.RED
            if (isinstance(entity, Player)):
                color = CONSTANTS.WHITE
                char = '@'
                text = self.bigfont.render(char, 1, CONSTANTS.BLUE)
                rect = self.make_rect(entity.x,entity.y)
                textpos = text.get_rect(centerx=rect.x + 32, centery=rect.y + 32 - 2)
                self.screen.blit(text, textpos)
            else:
                rect = self.make_rect(entity.x, entity.y)
                #pygame.draw.rect(self.screen, color, rect, 0) rectangle
                char = 'g'
                text = self.bigfont.render(char, 1, CONSTANTS.GREEN)
                rect = self.make_rect(entity.x,entity.y)
                textpos = text.get_rect(centerx=rect.x + 32, centery=rect.y + 32 - 2)
                self.screen.blit(text, textpos)


            #dist = utils.grid_distance((entity.x, entity.y), (10,10))
            #print 'distance to (10,10): %f' % dist
            #pygame.draw.line(self.screen, color, self.coords_to_screen(entity.x, entity.y), self.coords_to_screen(10, 10))

    def make_rect(self, x, y):
        # Make a rectangle, offset to be centered in viewport
        return pygame.Rect(
            (x * CONSTANTS.TILE_SIZE[0] + CONSTANTS.EXTRA_WIDTH / 2,
             y * CONSTANTS.TILE_SIZE[1] + CONSTANTS.EXTRA_HEIGHT / 2),
             CONSTANTS.TILE_SIZE)

    def coords_to_screen(self, x, y):
        return (x * CONSTANTS.TILE_SIZE[0] + (CONSTANTS.EXTRA_WIDTH / 2) + CONSTANTS.TILE_SIZE[0]/2, y * CONSTANTS.TILE_SIZE[1] + (CONSTANTS.EXTRA_HEIGHT / 2) + CONSTANTS.TILE_SIZE[1]/2)