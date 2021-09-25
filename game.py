from player import Player


class Game:
    def __init__(self):
        self.user = Player()
        self.opp = Player()
        self.run_game()

    # Handles the logic for the flow of the game
    def run_game(self):
        self.display_rules()
        play_status = True
        while(play_status == True):
            self.place_ships(self.user)
            self.place_ships(self.opp)
            while(True):
                self.take_turn(self.user, self.opp)
                if self.user.score == len(self.user.ships):
                    self.display_score(self.user, self.opp)
                    break
                self.take_turn(self.opp, self.user)
                if self.opp.score == len(self.opp.ships):
                    self.display_score(self.opp, self.user)
                    break
            self.display_victory()
            play_status = self.play_again()

    def display_rules(self):
        print('Each player places four ships on their own 20 x 20 grid. Take turns blindly attacking your opponent\'s grid until you sink all of their ships.')
        print('All grid coordinate prompts will be handled with LetterNumber inputs. (A1, A2, etc)')

    def display_grid(self, user):
        user.board.print_grid(user.board.grid)

    def display_target_grid(self, user):
        user.board.print_grid(user.target_board.grid)

    def display_victory(self):
        print('You have won the battle!')

    # Iterates through a user's ships, getting starting and ending locations
    def place_ships(self, user):
        self.display_grid(user)
        for i in range(len(user.ships)):
            valid_end = False
            while valid_end == False:
                start_pos = self.place_ship_starting_location(user, i)
                valid_end = self.place_ship_ending_location(user, i, start_pos)

    # Prompts user for starting x and y location of the ship then displays an updated grid
    def place_ship_starting_location(self, user, i):
        start_pos = self.get_position(
            user, i, 'ocean', 'starting', 'placement')
        user.board.grid[start_pos[1]][start_pos[0]] = user.ships[i].tag
        self.display_grid(user)
        user.board.grid[start_pos[1]][start_pos[0]] = '[ ]'
        return start_pos

    # Prompts user for an ending x and y location of the ship, validates it, then displays an updated grid
    def place_ship_ending_location(self, user, i, start_pos):
        valid = False
        while (valid == False):
            end_pos = self.get_position(
                user, i, 'ocean', 'ending', 'placement')
            valid_length = self.validate_ship_length(
                user, i, start_pos, end_pos)
            valid_collision = self.spawn_ship(
                user, i, start_pos, end_pos, 'validate')
            if valid_length == False or valid_collision == False:
                self.clear_ship_coordinates(user, i)
                valid = False
                print('Invalid input, going back to placing starting location.')
                return False
            else:
                valid = True
                self.spawn_ship(user, i, start_pos, end_pos, 'spawn')
        self.display_grid(user)
        return True

    # Prompts user for x and y location of the ship
    def get_position(self, user, i, grid_type, start_or_end_type, placement_type):
        valid = False
        while (valid == False):
            pos_check = False
            while (pos_check == False):
                pos = list(user.pick_location(
                    i, start_or_end_type, placement_type))
                pos_check = self.validate_position_input(user, pos)
                if pos_check == False:
                    print('Invalid input, try again.')
            pos = self.convert_to_x_y(pos)
            grid_check = self.validate_within_grid(user, pos)
            if start_or_end_type == 'starting' or placement_type == 'attack':
                collision_check = self.validate_no_start_collision(
                    user, pos, grid_type)
            else:
                # Defaults collision check to True when looking for ending position since the program is going to validate that later
                collision_check = True
            if grid_check == True and collision_check == True:
                valid = True
            else:
                print('Invalid input, try again.')
        return pos

    def clear_ship_coordinates(self, user, i):
        user.ships[i].x_positions.clear()
        user.ships[i].y_positions.clear()

    def validate_no_collisions(self, user, i, start_pos, direction):
        if direction == 'up' or direction == 'down':
            for pos in user.ships[i].y_positions:
                for j in range(len(user.ships)):
                    if user.board.grid[pos][start_pos[0]] == user.ships[j].tag:
                        return False
            return True
        else:
            for pos in user.ships[i].x_positions:
                for j in range(len(user.ships)):
                    if user.board.grid[start_pos[1]][pos] == user.ships[j].tag:
                        return False
            return True

    def validate_position_input(self, user, pos):
        if len(pos) > 3 or len(pos) < 2:
            return False
        valid_x = self.validate_x(pos)
        valid_y = self.validate_y(user, pos)
        if valid_x == False:
            return False
        if valid_y == False:
            return False
        return True

    def validate_x(self, pos):
        alphabet = 'ABCDEFGHIJKLMNOPQRST'
        for letter in alphabet:
            if pos[0].upper() == letter:
                return True
        return False

    def validate_y(self, user, pos):
        if len(pos) == 3:
            if pos[1].isdigit() == True and pos[2].isdigit() == True:
                pos[1] = int(str(pos[1]) + str(pos[2]))
                pos.pop(2)
            else:
                return False
        else:
            if pos[1].isdigit() != True:
                return False
        for i in range(user.board.side_length):
            if int(pos[1]) == int(i + 1):
                return True
        return False

    # Compares starting x and y locations to the ending locations to make sure theyre valid
    def validate_ship_length(self, user, i, start_pos, end_pos):
        # Checks if the length of the ship in the x axis directions is valid
        if start_pos[1] == end_pos[1] and (start_pos[0] == end_pos[0] + (user.ships[i].length - 1) or start_pos[0] == end_pos[0] - (user.ships[i].length - 1)):
            return True
        # Checks if the length of the ship in the y axis directions is valid
        elif start_pos[0] == end_pos[0] and (start_pos[1] == end_pos[1] + (user.ships[i].length - 1) or start_pos[1] == end_pos[1] - (user.ships[i].length - 1)):
            return True
        else:
            return False

    def validate_within_grid(self, user, pos):
        for i in range(user.board.side_length):
            if pos[0] == i:
                valid_x = True
        for i in range(user.board.side_length):
            if pos[1] == i:
                valid_y = True
        if valid_x == True and valid_y == True:
            return True
        else:
            return False

    def validate_no_start_collision(self, user, pos, grid_type):
        if grid_type == 'ocean':
            for i in range(len(user.ships)):
                if user.board.grid[pos[1]][pos[0]] == user.ships[i].tag:
                    return False
        else:
            if user.target_board.grid[pos[1]][pos[0]] == 'HIT' or user.target_board.grid[pos[1]][pos[0]] == 'MIS':
                return False
        return True

    # Creates the ship on the grid
    def spawn_ship(self, user, i, start_pos, end_pos, type):
        if start_pos[0] == end_pos[0] and start_pos[1] > end_pos[1]:
            direction = 'up'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            if type == 'spawn':
                self.assign_coordinates_to_grid(user, i, start_pos, direction)
            else:
                valid = self.validate_no_collisions(
                    user, i, start_pos, direction)
                return valid
        elif start_pos[0] == end_pos[0] and start_pos[1] < end_pos[1]:
            direction = 'down'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            if type == 'spawn':
                self.assign_coordinates_to_grid(user, i, start_pos, direction)
            else:
                valid = self.validate_no_collisions(
                    user, i, start_pos, direction)
                return valid
        elif start_pos[1] == end_pos[1] and start_pos[0] > end_pos[0]:
            direction = 'left'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            if type == 'spawn':
                self.assign_coordinates_to_grid(user, i, start_pos, direction)
            else:
                valid = self.validate_no_collisions(
                    user, i, start_pos, direction)
                return valid
        else:
            direction = 'right'
            self.assign_coordinates_to_ship(
                user, i, start_pos, direction)
            if type == 'spawn':
                self.assign_coordinates_to_grid(user, i, start_pos, direction)
            else:
                valid = self.validate_no_collisions(
                    user, i, start_pos, direction)
                return valid

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

    # Assigns the x and y coordinates of the ship to the user's grid and checks for collisions
    def assign_coordinates_to_grid(self, user, i, start_pos, direction):
        if direction == 'up' or direction == 'down':
            for pos in user.ships[i].y_positions:
                user.board.grid[pos][start_pos[0]] = user.ships[i].tag
        else:
            for pos in user.ships[i].x_positions:
                user.board.grid[start_pos[1]][pos] = user.ships[i].tag

    def take_turn(self, user, opp):
        self.display_grid(user)
        self.display_target_grid(user)
        self.display_score(user, opp)
        attack_pos = self.get_position(user, 0, 'target', '', 'attack')
        self.attack_location(user, opp, attack_pos)
        self.update_score(user, opp)

    def attack_location(self, user, opp, attack_pos):
        counter = 0
        for i in range(len(opp.ships)):
            if opp.board.grid[attack_pos[1]][attack_pos[0]] == opp.ships[i].tag:
                self.assign_hit_type_to_grids(user, opp, attack_pos, 'HIT')
                self.deal_damage_to_ship(opp, i)
                self.check_for_sink(opp, i)
            else:
                counter += 1
        if counter == len(opp.ships):
            self.assign_hit_type_to_grids(user, opp, attack_pos, 'MIS')

    def assign_hit_type_to_grids(self, user, opp, attack_pos, tag):
        user.target_board.grid[attack_pos[1]][attack_pos[0]] = tag
        opp.board.grid[attack_pos[1]][attack_pos[0]] = tag

    def deal_damage_to_ship(self, opp, i):
        opp.ships[i].health -= 1

    def check_for_sink(self, opp, i):
        if opp.ships[i].health == 0:
            opp.ships[i].alive = False

    def update_score(self, user, opp):
        counter = 0
        for i in range(len(opp.ships)):
            if opp.ships[i].alive == False:
                counter += 1
        user.score = counter

    def display_score(self, user, opp):
        print(
            f'You have sunk {user.score} ships and your opponent has sunk {opp.score} ships.')

    def play_again(self):
        valid_play_again = self.validate_yes_no('play_again')
        if valid_play_again == 'y':
            self.user = Player()
            self.opp = Player()
            return True
        else:
            return False

    # Converts user input into usable grid coordinates
    def convert_to_x_y(self, pos):
        pos[0] = self.convert_to_x_value(pos[0])
        if len(pos) == 3:
            pos[1] = int(str(pos[1]) + str(pos[2]))
            pos.pop(2)
        pos[1] = self.convert_to_y_value(pos[1])
        return pos

    def convert_to_x_value(self, input):
        alphabet = 'ABCDEFGHIJKLMNOPQRST'
        num = 0
        for letter in alphabet:
            if letter == input.upper():
                x_value = num
                return x_value
            num += 1

    def convert_to_y_value(self, input):
        return int(input) - 1

    def convert_to_y_or_n(self, input):
        if input.lower() == 'yes' or input.lower() == 'y':
            return 'y'
        elif input.lower() == 'no' or input.lower() == 'n':
            return 'n'
        else:
            return 'invalid'

    def validate_yes_no(self, type):
        valid = False
        while(valid == False):
            if type == 'view_grid':
                user_input = str(
                    input('Do you want to view your ocean grid? y/n: '))
            elif type == 'done_with_grid':
                user_input = str(
                    input('Are you done viewing your ocean grid? y/n: '))
            else:
                user_input = str(input('Do you want to play again? y/n: '))
            user_question = self.convert_to_y_or_n(user_input)
            if user_question == 'invalid':
                valid = False
                print('Invalid input, try again.')
            elif user_question == 'y' or 'n':
                valid = True
                return user_question
            else:
                valid = False
