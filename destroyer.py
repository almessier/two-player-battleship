from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'destroyer'
        self.length = 2
