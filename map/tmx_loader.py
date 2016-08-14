import pygame
from pytmx.util_pygame import load_pygame
import sys
sys.path.append('../')
import CONSTANTS
from tile import Tile
from tile_type import TileType

# https://github.com/bitcraft/pyscroll
# https://github.com/bitcraft/PyTMX

class TmxLoader:
    def __init__(self, path):
        self.data = load_pygame(path)
        self.tile_width = self.data.tilewidth
        self.tile_height = self.data.tileheight
        self.tiles = []
        self.parse_map_data()

    def parse_map_data(self):
        for layer in self.data.layers:
            if layer.name == 'collision_layer':
                for x, y, image in layer.tiles():
                    self.make_tile(x, y, None, TileType.COLLISION)
                    print 'making a collision tile (%d, %d)' % (x, y)
            else:
                for x, y, image in layer.tiles():
                    self.make_tile(x, y, image, TileType.NORMAL)
                    print 'making a tile (%d, %d)' % (x, y)

    def make_tile(self, x, y, image, type_in):
        tile_position = (x * self.tile_width * CONSTANTS.TILE_SCALING + CONSTANTS.EXTRA_WIDTH / 2,
                         y * self.tile_height * CONSTANTS.TILE_SCALING + CONSTANTS.EXTRA_HEIGHT / 2)
        self.tiles.append(Tile((x, y), tile_position, image, type_in))


    def make_rect(self, x, y):
        # Make a rectangle, offset to be centered in viewport
        return pygame.Rect(
            (x * CONSTANTS.TILE_SIZE[0] + CONSTANTS.EXTRA_WIDTH / 2,
             y * CONSTANTS.TILE_SIZE[1] + CONSTANTS.EXTRA_HEIGHT / 2),
             CONSTANTS.TILE_SIZE)