resolution = (800, 800)
TITLE = "Squares N' Numbers"

TILE_PIXEL_SIZE = 32
TILE_SIZE = (TILE_PIXEL_SIZE, TILE_PIXEL_SIZE) # pixel dimensions in each visual tile
HALF_TILE_SIZE = TILE_SIZE[0] / 2
TILE_SCALING = 1#TILE_SIZE[0] / 16 # tiles are really 16x16, but x4 makes them 64 pixels each
WIDTH  = 20 #resolution[0] / TILE_SIZE[0]
HEIGHT  = 10 #resolution[1] / TILE_SIZE[1]

EXTRA_WIDTH = resolution[0] - WIDTH * TILE_SIZE[0]
EXTRA_HEIGHT = resolution[1] - HEIGHT * TILE_SIZE[1]


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

