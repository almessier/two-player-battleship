from player import Player


class Game:
    def __init__(self):
        self.user = Player()
        self.opp = Player()

    def run_game(self):
        self.display_rules()
        self.user_place_ships()
        self.opp_place_ships()

    def display_rules(self):
        print('rules')

    def user_place_ships(self):
        self.display_grid(self.user)

    def opp_place_ships(self):
        self.display_grid(self.opp)

    def display_grid(self, user):
        user.board.print_grid(user.board.grid)
