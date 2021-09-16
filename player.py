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
        self.des = Destroyer()
        self.sub = Submarine()
        self.bat = Battleship()
        self.air = AircraftCarrier()

    def prompt_x(self):
        x_value = int(input(
            'What x axis value from A to T would you like to place your destroyer?'))
        return x_value

    def prompt_y(self):
        y_value = int(input(
            'What y axis value from 1 to 20 would you like to place your destroyer?'))
        return y_value

    def place_des(self):
        x_value = self.prompt_x()
        y_value = self.prompt_y()

    def place_sub(self):
        pass

    def place_bat(self):
        pass

    def place_air(self):
        pass

    def attack(self):
        pass
