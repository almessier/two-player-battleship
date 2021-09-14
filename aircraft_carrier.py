from ship import Ship


class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'aircraft carrier'
        self.length = 5
