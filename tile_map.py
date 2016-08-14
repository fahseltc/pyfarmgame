import CONSTANTS

from random import randint


class TileMap:

    level1 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             ]



    def __init__(self):
        self.width = CONSTANTS.WIDTH
        self.height = CONSTANTS.HEIGHT

        self.matrix = {}

        for y in range(0, CONSTANTS.HEIGHT):
            for x in range(0, CONSTANTS.WIDTH):
                print '%d, %d' % (x, y)
                self.matrix[x,y] = self.level1[y][x]#randint(0,2)

    def blocked(self, x, y):
        if ((x < 0) or (y < 0) or (x > self.width - 1) or (y > self.height - 1)):
            return True
        if(self.matrix[x,y] == 0):
            return True
        return False



