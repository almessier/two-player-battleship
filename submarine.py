from ship import Ship


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'submarine'
        self.tag = 'SUB'
        self.x_pos = 0
        self.y_pos = 0
        self.length = 3
