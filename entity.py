import GAME_GLOBALS
from random import randint

from action import Action, NothingAction, WalkAction, WalkTowardsAction
from energy import Energy
from direction import Direction

class Entity:
    def __init__(self, x_init, y_init, game):
        self.x = x_init
        self.y = y_init
        self.game = game
        self.energy = Energy()
        self.next_action = NothingAction()

    needs_input = False


    def get_action(self):
        self.determine_next_action()
        return self.next_action

    def clear_action(self):
        self.next_action = NothingAction()

    def determine_next_action(self):
        #if self.next_action != NothingAction:
        #    return
        val = randint(0,3)
        if (val == 0):
            self.next_action = WalkAction(self, Direction.UP)
        elif (val == 1):
            self.next_action = WalkAction(self, Direction.DOWN)
        elif (val == 2):
            self.next_action = WalkAction(self, Direction.LEFT)
        elif (val == 3):
            self.next_action = WalkAction(self, Direction.RIGHT)
        else:
            self.next_action = WalkTowardsAction(self, self.game.player)

    def set_next_action(self, action):
        self.next_action = action

    def needs_action(self):
        if isinstance(self.next_action, NothingAction):
            return True
        else:
            return False


