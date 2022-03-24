import Tire

class OctoprimeTire(Tire):
    def __init__(self, tireWear):
        self.tireWear = tireWear

    def needService(self):
        return sum(self.tireWear) >= 3.0