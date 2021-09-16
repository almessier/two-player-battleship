from game_board import GameBoard
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import AircraftCarrier


class Player:
    def __init__(self):
        self.name = 'Player'
        self.board = GameBoard()
        self.target_board = GameBoard()
        self.ships = self.create_ships()

    def create_ships(self):
        des = Destroyer()
        sub = Submarine()
        bat = Battleship()
        air = AircraftCarrier()
        ships = [des, sub, bat, air]
        return ships

    def prompt_x(self, i, type):
        x_letter = str(input(
            f'Which x axis value from A to T would you like to place your {self.ships[i].name}\'s {type} location? It is {self.ships[i].length} units long: '))
        return x_letter

    def prompt_y(self, i, type):
        y_value = int(input(
            f'Which y axis value from 1 to 20 would you like to place your {self.ships[i].name}\'s {type} location? It is {self.ships[i].length} units long: '))
        return y_value

    def attack(self):
        pass
