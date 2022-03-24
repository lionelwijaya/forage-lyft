import unittest
from Tire.carriganTire import CarriganTire
from Tire.octoprimeTire import OctoprimeTire

class TestTire(unittest.TestCase):
    def carriganTireCaseTrue(self):
        tireWear = [1, 0.3, 0.1, 1]
        tires = CarriganTire(tireWear)
        self.assertTrue(tires.needService())

    def carriganTireCaseFalse(self):
        tireWear = [0, 0.1, 0, 0.2]
        tires = CarriganTire(tireWear)
        self.assertFalse(tires.needService())

    def octoprimeTireCaseTrue(self):
        tireWear = [1, 1, 0.8, 1]
        tires = OctoprimeTire(tireWear)
        self.assertTrue(tires.needService())

    def octoprimeTireCaseFalse(self):
        tireWear = [0.1, 0.1, 0.2, 0.2]
        tires = OctoprimeTire(tireWear)
        self.assertFalse(tires.needService())        