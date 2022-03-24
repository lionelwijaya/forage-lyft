
from Engine.capuletEngine import CapuletEngine
from Engine.sternmanEngine import SternmanEngine
from Engine.willoughbyEngine import WilloughbyEngine
from Battery.nubbinBattery import NubbinBattery
from Battery.spindlerBattery import SpindlerBattery
from car import Car

class CarFactory:
    @staticmethod
    def createCalliope(currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        engine = CapuletEngine(currentMileage, lastServiceMileage)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        car = Car(engine, battery)
        return car

    @staticmethod
    def createGlissade(currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        engine = WilloughbyEngine(currentMileage, lastServiceMileage)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        car = Car(engine, battery)
        return car

    @staticmethod
    def createPalindrome(currentDate, lastServiceDate, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        car = Car(engine, battery)
        return car

    @staticmethod
    def createRorschach(currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        engine = WilloughbyEngine(currentMileage, lastServiceMileage)
        battery = NubbinBattery(currentDate, lastServiceDate)
        car = Car(engine, battery)
        return car

    @staticmethod
    def createThovex(currentDate, lastServiceDate, currentMileage, lastServiceMileage):
        engine = CapuletEngine(currentMileage, lastServiceMileage)
        battery = NubbinBattery(currentDate, lastServiceDate)
        car = Car(engine, battery)
        return car