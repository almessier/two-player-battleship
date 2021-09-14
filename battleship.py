from ship import Ship


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'battleship'
        self.length = 4
