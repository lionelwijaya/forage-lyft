import Tire

class CarriganTire(Tire):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needService(self):
        for tire in self.tireWear:
            if tire >= 0.9:
                return True
        return False