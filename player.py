from entity import Entity

class Player(Entity):
    def __init__(self, x, y, game):
        Entity.__init__(self, x, y, game)

    needs_input = True

    def get_action(self):
        #self.determine_next_action()
        return self.next_action