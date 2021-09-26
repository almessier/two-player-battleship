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
        self.score = 0
        self.ships = self.create_ships()

    def create_ships(self):
        des = Destroyer()
        sub = Submarine()
        bat = Battleship()
        air = AircraftCarrier()
        ships = [des, sub, bat, air]
        return ships

    def pick_location(self, i, start_end_type, placement_type):
        if placement_type == 'attack':
            location = str(
                input('Where would you like to attack? Grid goes from A1 to T20. You can also type OCEAN to view your ocean grid or TARGET to view your target grid: '))
        else:
            location = str(input(
                f'Where would you like to place your {self.ships[i].name}\'s {start_end_type} location? It is {self.ships[i].length} units long. Grid goes from A1 to T20: '))
        return location
