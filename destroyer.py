from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'destroyer'
        self.tag = 'DES'
        self.length = 2
