from ship import Ship


class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Aircraft Carrier'
        self.tag = 'AIR'
        self.length = 5
        self.health = 5
