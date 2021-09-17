from ship import Ship


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'submarine'
        self.tag = 'SUB'
        self.length = 3
