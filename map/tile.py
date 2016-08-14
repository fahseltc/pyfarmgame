import pygame
from tile_type import TileType
import sys
sys.path.append('../')
import CONSTANTS


class Tile:
    def __init__(self, coords, position, image, type_in):
        self.coords = coords
        self.position = position
        if image is not None:
            self.image = self.scale_image(image)
        else:
            self.image = None;
        self.type = type_in

    def scale_image(self, image):
        return pygame.transform.scale(image, (image.get_width() * CONSTANTS.TILE_SCALING, image.get_height() * CONSTANTS.TILE_SCALING))