from ship import Ship


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.tag = 'SUB'
        self.length = 3
        self.health = 3
