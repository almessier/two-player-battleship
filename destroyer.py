from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.tag = 'DES'
        self.length = 2
        self.health = 2
