from ship import Ship


class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'aircraft carrier'
        self.tag = 'AIR'
        self.x_pos = 0
        self.y_pos = 0
        self.length = 5
