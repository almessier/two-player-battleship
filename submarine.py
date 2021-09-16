from ship import Ship


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'submarine'
        self.tag = 'SUB'
        self.start_pos_x = 0
        self.start_pos_y = 0
        self.length = 3
