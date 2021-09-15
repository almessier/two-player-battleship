from player import Player


class Game:
    def __init__(self):
        self.user = Player()
        self.opp = Player()

    def run_game(self):
        self.display_rules()
        self.place_ships(self.user)
        self.place_ships(self.opp)
        self.take_turn(self.user)
        self.take_turn(self.opp)

    def display_rules(self):
        print('rules')

    def place_ships(self, user):
        self.display_grid(user)

    def display_grid(self, user):
        user.board.print_grid(user.board.grid)

    def take_turn(self, user):
        pass
