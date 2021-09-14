from game_board import GameBoard
from destroyer import Destroyer
from submarine import Submarine
from battleship import Battleship
from aircraft_carrier import AircraftCarrier


class Player:
    def __init__(self):
        self.name = 'Player'
        self.board = GameBoard()
        self.des = Destroyer()
        self.sub = Submarine()
        self.bat = Battleship()
        self.air = AircraftCarrier()

    def place_des(self):
        pass

    def place_sub(self):
        pass

    def place_bat(self):
        pass

    def place_air(self):
        pass

    def attack(self):
        pass
