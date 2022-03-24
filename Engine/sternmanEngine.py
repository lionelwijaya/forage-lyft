import Engine

class SternmanEngine(Engine):

    def __init__(self, warningLightIsOn):
        self.warningLightIsOn = warningLightIsOn

    def needs_service(self):
        if self.warningLightIsOn:
            return True
        else:
            return False