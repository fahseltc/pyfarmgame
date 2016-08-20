import utils
import GAME_GLOBALS
from direction import Direction
# HEY FUCK YOU
class Action:
    def __init__(self):
        pass

    def perform(self):
        pass

class NothingAction(Action):
    def __init__(self):
        Action.__init__(self)

    def perform(self):
        return False

class WalkAction(Action):
    def __init__(self, entity, direction):
        self.entity = entity
        self.direction = direction

    def perform(self):
        future_x = future_y = 0
        future_x = self.entity.x + self.direction[0]
        future_y = self.entity.y + self.direction[1]

        if not (GAME_GLOBALS.tile_map.blocked(future_x, future_y)):
            self.entity.x += self.direction[0]
            self.entity.y += self.direction[1]
            print 'entity pos (%d, %d)' % (self.entity.x, self.entity.y)
            return True
        else:
            print 'blocked'
            return False

class WalkTowardsAction(Action):
    def __init__(self, entity, target):
        self.entity = entity
        self.target = target

    def perfom(self):
        print 'eh'
        shortest_distance = utils.grid_distance((entity.x, entity.y), (target.x, target.y))

        new_dist = move_distance(Direction.UP)
        if new_dist < shortest_distance:
            result = Direction.UP
            shortest_distance = new_dist

        new_dist = move_distance(Direction.DOWN)
        if new_dist < shortest_distance:
            result = Direction.DOWN
            shortest_distance = new_dist

        new_dist = move_distance(Direction.LEFT)
        if new_dist < shortest_distance:
            result = Direction.LEFT
            shortest_distance = new_dist

        new_dist = move_distance(Direction.RIGHT)
        if new_dist < shortest_distance:
            result = Direction.RIGHT
            shortest_distance = new_dist

        action = WalkAction(self.entity, GAME_GLOBALS.tile_map, result)
        return action.perform()


    def move_distance(direction):
        return utils.grid_distance((entity.x + direction[0], entity.y + direction[1]), (target.x, target.y))
