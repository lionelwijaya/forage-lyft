import Engine

class WilloughbyEngine(Engine):

    def __init__(self, currentMileage, lastServiceMileage):
        self.currentMileage = currentMileage
        self.lastServiceMileage = lastServiceMileage

    def needs_service(self):
        return self.currentMileage - self.lastServiceMileage > 60000