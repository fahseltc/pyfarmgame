import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

TILE_SCALING = 5 # move to constants

class TmxLoader:
    def __init__(self, path):
        self.tmx_data = load_pygame(path)
        self.tile_width = self.tmx_data.tilewidth
        self.tile_height = self.tmx_data.tileheight
        self.tiles = []
        self.parse_map_data()

    def parse_map_data(self):
        for layer in self.tmx_data.layers:
            for x, y, image in layer.tiles():
                self.make_tile(x, y, image)

    def make_tile(self, x, y, image):
        tile_position = (x * self.tile_width * TILE_SCALING, y * self.tile_height * TILE_SCALING)
        self.tiles.append(Tile((x, y), tile_position, image))

class Tile:
    def __init__(self, coords, position, image):
        self.coords = coords
        self.position = position
        self.image = self.scale_image(image)

    def scale_image(self, image):
        return pygame.transform.scale(image, (image.get_width() * TILE_SCALING, image.get_height() * TILE_SCALING))
