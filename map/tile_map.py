import collections
from tmx_loader import TmxLoader
from tile_type import TileType

class TileMap:
    def __init__(self):
        self.tiles = {}
        print 'loading tmx now'
        tmx_loader = TmxLoader('assets/tmx/robots.tmx')

        self.height = tmx_loader.data.height
        self.width = tmx_loader.data.width
        print 'map width: %d, height: %d' % (self.height, self.width)

        for tile in tmx_loader.tiles:
            key = tile.coords
            self.tiles.setdefault(key, []) # make it a list if needed
            self.tiles[key].append(tile)

        # print the map info
        ordered_dict = collections.OrderedDict(sorted(self.tiles.items()))
        for key in ordered_dict:
            print key
            for value in self.tiles[key]:
                print (value.type)

    def get_tiles(self, position):
        return self.tiles[position]

    def tile_blocked(self, position):
        tiles_in_position = self.tiles.get(position)

        if tiles_in_position is not None:
            for tile in self.tiles.get(position):
                if tile.type == "COLLISION":
                    return True
        return False

    def blocked(self, x, y):
        if ((x < 0) or (y < 0) or (x > self.width - 1) or (y > self.height - 1)):
            return True
        else:
            print 'coords %d, %d: blocked? %r' %(x, y, self.tile_blocked((x,y)))
            return self.tile_blocked((x,y))