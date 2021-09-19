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
            start_pos = self.place_ship_starting_location(user, i)
            self.place_ship_ending_location(user, i, start_pos)

    # Prompts user for starting x and y location of the ship then displays an updated grid
    def place_ship_starting_location(self, user, i):
        start_pos = self.get_position(user, i, 'starting')
        user.board.grid[start_pos[1]][start_pos[0]] = user.ships[i].tag
        self.display_grid(user)
        user.board.grid[start_pos[1]][start_pos[0]] = '[ ]'
        return start_pos

    # Prompts user for an ending x and y location of the ship, validates it, then displays an updated grid
    def place_ship_ending_location(self, user, i, start_pos):
        valid = False
        while (valid == False):
            end_pos = self.get_position(user, i, 'ending')
            valid = self.validate_ship_length(user, i, start_pos, end_pos)
        self.spawn_ship(user, i, start_pos, end_pos)
        self.display_grid(user)

    # Prompts user for x and y location of the ship
    def get_position(self, user, i, type):
        pos = self.convert_to_x_y(
            list(user.pick_location(i, type, 'placement')))
        return pos

    # Converts user input into usable grid coordinates
    def convert_to_x_y(self, pos):
        pos[0] = self.convert_to_x_value(pos[0])
        if len(pos) == 3:
            pos[1] = int(str(pos[1]) + str(pos[2]))
            pos.pop(2)
        pos[1] = self.convert_to_y_value(pos[1])
        return pos

    # Compares starting x and y locations to the ending locations to make sure theyre valid
    def validate_ship_length(self, user, i, start_pos, end_pos):
        # Checks if the length of the ship in the x axis directions is valid
        if start_pos[1] == end_pos[1] and (start_pos[0] == end_pos[0] + (user.ships[i].length - 1) or start_pos[0] == end_pos[0] - (user.ships[i].length - 1)):
            return True
        # Checks if the length of the ship in the y axis directions is valid
        elif start_pos[0] == end_pos[0] and (start_pos[1] == end_pos[1] + (user.ships[i].length - 1) or start_pos[1] == end_pos[1] - (user.ships[i].length - 1)):
            return True
        else:
            print('Invalid location, try again.')
            return False

    # Creates the ship on the grid
    def spawn_ship(self, user, i, start_pos, end_pos):
        if start_pos[0] == end_pos[0] and start_pos[1] > end_pos[1]:
            direction = 'up'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            self.assign_coordinates_to_grid(user, i, start_pos, direction)
        elif start_pos[0] == end_pos[0] and start_pos[1] < end_pos[1]:
            direction = 'down'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            self.assign_coordinates_to_grid(user, i, start_pos, direction)
        elif start_pos[1] == end_pos[1] and start_pos[0] > end_pos[0]:
            direction = 'left'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            self.assign_coordinates_to_grid(user, i, start_pos, direction)
        else:
            direction = 'right'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            self.assign_coordinates_to_grid(user, i, start_pos, direction)

    # Assigns the x and y coordinates of the ship to the user's current ship object
    def assign_coordinates_to_ship(self, user, i, start_pos, direction):
        if direction == 'up':
            user.ships[i].x_positions.append(start_pos[0])
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    start_pos[1] - num)
        elif direction == 'down':
            user.ships[i].x_positions.append(start_pos[0])
            for num in range(user.ships[i].length):
                user.ships[i].y_positions.append(
                    start_pos[1] + num)
        elif direction == 'left':
            user.ships[i].y_positions.append(start_pos[1])
            for num in range(user.ships[i].length):
                user.ships[i].x_positions.append(
                    start_pos[0] - num)
        else:
            user.ships[i].y_positions.append(start_pos[1])
            for num in range(user.ships[i].length):
                user.ships[i].x_positions.append(
                    start_pos[0] + num)

    # Assigns the x and y coordinates of the ship to the user's grid
    def assign_coordinates_to_grid(self, user, i, start_pos, direction):
        if direction == 'up' or direction == 'down':
            for pos in user.ships[i].y_positions:
                user.board.grid[pos][start_pos[0]] = user.ships[i].tag
        else:
            for pos in user.ships[i].x_positions:
                user.board.grid[start_pos[1]][pos] = user.ships[i].tag

    def take_turn(self, user):
        self.display_target_grid(user)
        attack_pos = self.convert_to_x_y(
            list(user.pick_location(0, '', 'attack')))

    def convert_to_x_value(self, input):
        alphabet = 'ABCDEFGHIJKLMNOPQRST'
        num = 0
        for letter in alphabet:
            if letter == input:
                x_value = num
                return x_value
            num += 1

    def convert_to_y_value(self, input):
        return int(input) - 1
