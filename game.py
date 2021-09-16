from player import Player


class Game:
    def __init__(self):
        self.user = Player()
        self.opp = Player()
        self.run_game()

    def run_game(self):
        self.display_rules()
        self.place_ships(self.user)
        self.place_ships(self.opp)
        self.take_turn(self.user)
        self.take_turn(self.opp)

    def display_rules(self):
        print('rules')

    def display_grid(self, user):
        user.board.print_grid(user.board.grid)

    def display_target_grid(self, user):
        user.board.print_grid(user.target_board.grid)

    def place_ships(self, user):
        self.display_grid(user)
        for index in range(len(user.ships)):
            self.place_ship_starting_location(user, index)
            self.display_grid(user)
            self.place_ship_ending_location(user)
            self.display_grid(user)

    def place_ship_starting_location(self, user, index):
        x_value = self.convert_to_x_value(user.prompt_x(index, 'starting'))
        y_value = self.convert_to_y_value(user.prompt_y(index, 'starting'))
        user.board.grid[y_value][x_value] = user.ships[index].tag

    def place_ship_ending_location(self, user):
        pass

    def take_turn(self, user):
        pass

    def convert_to_x_value(self, input):
        alphabet = 'ABCDEFGHIJKLMNOPQRST'
        num = 0
        for letter in alphabet:
            if letter == input:
                x_value = num
                return x_value
            num += 1

    def convert_to_y_value(self, input):
        return input - 1
