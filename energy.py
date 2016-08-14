class Energy:
    def __init__(self):
        self.amount = 0
        self.turn_threshold = 10
        self.energy_per_turn = 1
        self.can_take_turn = False

    def gain(self):
        if not (self.can_take_turn):
            self.amount += self.energy_per_turn
        return self.check()

    def check(self):
        if (self.amount >= self.turn_threshold):
            self.amount %= self.turn_threshold
            self.can_take_turn = True
        else:
            self.can_take_turn = False
        return self.can_take_turn

    def spend_turn(self):
        self.can_take_turn = False
