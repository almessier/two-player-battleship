from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'destroyer'
        self.tag = 'DES'
        self.start_pos_x = 0
        self.start_pos_y = 0
        self.end_pos_x = 0
        self.end_pos_y = 0
        self.length = 2
