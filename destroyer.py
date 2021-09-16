from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'destroyer'
        self.tag = 'DES'
        self.x_pos = 0
        self.y_pos = 0
        self.length = 2
