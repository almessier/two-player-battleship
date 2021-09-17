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

    # Iterates through a user's ships, getting starting and ending locations
    def place_ships(self, user):
        self.display_grid(user)
        for i in range(len(user.ships)):
            self.place_ship_starting_location(user, i)
            self.place_ship_ending_location(user, i)

    # Prompts user for starting x and y location of the ship then displays an updated grid
    def place_ship_starting_location(self, user, i):
        user.ships[i].start_pos_x = self.convert_to_x_value(
            user.prompt_x(i, 'starting'))
        user.ships[i].start_pos_y = self.convert_to_y_value(
            user.prompt_y(i, 'starting'))
        user.board.grid[user.ships[i].start_pos_y][user.ships[i]
                                                       .start_pos_x] = user.ships[i].tag
        self.display_grid(user)
        user.board.grid[user.ships[i].start_pos_y][user.ships[i]
                                                       .start_pos_x] = '[ ]'

    # Prompts user for an ending x and y location of the ship, validates it, then displays an updated grid
    def place_ship_ending_location(self, user, i):
        valid = False
        while (valid == False):
            self.get_ending_position(user, i)
            valid = self.validate_ship_length(user, i)
        self.spawn_ship(user, i)
        self.display_grid(user)

    # Prompts user for ending x and y location of the ship
    def get_ending_position(self, user, i):
        user.ships[i].end_pos_x = self.convert_to_x_value(
            user.prompt_x(i, 'ending'))
        user.ships[i].end_pos_y = self.convert_to_y_value(
            user.prompt_y(i, 'ending'))

    # Compares starting x and y locations to the ending locations to make sure theyre valid
    def validate_ship_length(self, user, i):
        # Checks if the length of the ship in the x axis directions is valid
        if user.ships[i].start_pos_y == user.ships[i].end_pos_y and (user.ships[i].start_pos_x == user.ships[i].end_pos_x + (user.ships[i].length - 1) or user.ships[i].start_pos_x == user.ships[i].end_pos_x - (user.ships[i].length - 1)):
            return True
        # Checks if the length of the ship in the y axis directions is valid
        elif user.ships[i].start_pos_x == user.ships[i].end_pos_x and (user.ships[i].start_pos_y == user.ships[i].end_pos_y + (user.ships[i].length - 1) or user.ships[i].start_pos_y == user.ships[i].end_pos_y - (user.ships[i].length - 1)):
            return True
        else:
            print('Invalid location, try again.')
            return False

    # Creates the ship on the grid
    def spawn_ship(self, user, i):
        if user.ships[i].start_pos_x == user.ships[i].end_pos_x and user.ships[i].start_pos_y > user.ships[i].end_pos_y:
            direction = 'up'
            self.assign_ship_x_y_coordinates(user, i, direction)
            self.assign_coordinates_to_grid(user, i, direction)
        elif user.ships[i].start_pos_x == user.ships[i].end_pos_x and user.ships[i].start_pos_y < user.ships[i].end_pos_y:
            direction = 'down'
            self.assign_ship_x_y_coordinates(user, i, direction)
            self.assign_coordinates_to_grid(user, i, direction)
        elif user.ships[i].start_pos_y == user.ships[i].end_pos_y and user.ships[i].start_pos_x > user.ships[i].end_pos_x:
            direction = 'left'
            self.assign_ship_x_y_coordinates(user, i, direction)
            self.assign_coordinates_to_grid(user, i, direction)
        else:
            direction = 'right'
            self.assign_ship_x_y_coordinates(user, i, direction)
            self.assign_coordinates_to_grid(user, i, direction)

    # Assigns the x and y coordinates of the ship to the user's current ship object
    def assign_ship_x_y_coordinates(self, user, i, direction):
        if direction == 'up':
            user.ships[i].x_positions.append(user.ships[i].start_pos_x)
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    user.ships[i].start_pos_y - num)
        elif direction == 'down':
            user.ships[i].x_positions.append(user.ships[i].start_pos_x)
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    user.ships[i].start_pos_y + num)
        elif direction == 'left':
            user.ships[i].y_positions.append(user.ships[i].start_pos_y)
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    user.ships[i].start_pos_y - num)
        else:
            user.ships[i].y_positions.append(user.ships[i].start_pos_y)
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    user.ships[i].start_pos_y + num)

    # Assigns the x and y coordinates of the ship to the user's grid
    def assign_coordinates_to_grid(self, user, i, direction):
        if direction == 'up' or 'down':
            for pos in user.ships[i].y_positions:
                user.board.grid[pos][user.ships[i].start_pos_x] = user.ships[i].tag
        else:
            for pos in user.ships[i].x_positions:
                user.board.grid[user.ships[i].start_pos_y][pos] = user.ships[i].tag

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
