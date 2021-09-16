from ship import Ship


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'battleship'
        self.tag = 'BAT'
        self.x_pos = 0
        self.y_pos = 0
        self.length = 4
