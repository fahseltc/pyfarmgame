import collections
from tmx_loader import TmxLoader
from tile_type import TileType

class TileMap:
    def __init__(self):
        self.tiles = {}
        print 'loading tmx now'
        tmx_loader = TmxLoader('../assets/tmx/map.tmx')

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
                pass
                print (value.type)

    def get_tiles(position):
        return self.tiles[position]

    def tiled_blocked(position):
        for tile in self.tiles[position]:
            if tile.type == TileType.BLOCKED:
                return true
        return false