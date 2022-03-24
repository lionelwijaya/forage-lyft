
from Engine.capuletEngine import CapuletEngine
from Engine.sternmanEngine import SternmanEngine
from Engine.willoughbyEngine import WilloughbyEngine
from Battery.nubbinBattery import NubbinBattery
from Battery.spindlerBattery import SpindlerBattery
from Tire.carriganTire import CarriganTire
from Tire.octoprimeTire import OctoprimeTire
from car import Car

class CarFactory:
    @staticmethod
    def createCalliope(currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireWear):
        engine = CapuletEngine(currentMileage, lastServiceMileage)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        tire = CarriganTire(tireWear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def createGlissade(currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireWear):
        engine = WilloughbyEngine(currentMileage, lastServiceMileage)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        tire = OctoprimeTire(tireWear)        
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def createPalindrome(currentDate, lastServiceDate, warning_light_is_on, tireWear):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(currentDate, lastServiceDate)
        tire = CarriganTire(tireWear)        
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def createRorschach(currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireWear):
        engine = WilloughbyEngine(currentMileage, lastServiceMileage)
        battery = NubbinBattery(currentDate, lastServiceDate)
        tire = OctoprimeTire(tireWear)   
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def createThovex(currentDate, lastServiceDate, currentMileage, lastServiceMileage, tireWear):
        engine = CapuletEngine(currentMileage, lastServiceMileage)
        battery = NubbinBattery(currentDate, lastServiceDate)
        tire = CarriganTire(tireWear)   
        car = Car(engine, battery, tire)
        return car