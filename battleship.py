from ship import Ship


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.tag = 'BAT'
        self.length = 4
        self.health = 4
