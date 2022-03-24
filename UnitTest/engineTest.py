import unittest
from Engine.capuletEngine import CapuletEngine
from Engine.sternmanEngine import SternmanEngine
from Engine.willoughbyEngine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def capuletEngineTestCaseTrue(self):
        currentMilleage = 40000
        lastServiceMilleage = 0
        engine = CapuletEngine(currentMilleage, lastServiceMilleage)
        self.assertTrue(engine.needService())

    def capuletEngineTestCaseFalse(self):
        currentMilleage = 25000
        lastServiceMilleage = 0
        engine = CapuletEngine(currentMilleage, lastServiceMilleage)
        self.assertFalse(engine.needService())

    def sternmanEngineTestCaseTrue(self):
        warningLightIsOn = True
        engine = SternmanEngine(warningLightIsOn)
        self.assertTrue(engine.needService())

    def sternmanEngineTestCaseFalse(self):
        warningLightIsOn = False
        engine = SternmanEngine(warningLightIsOn)
        self.assertFalse(engine.needService())

    def willougbyEngineTestCaseTrue(self):
        currentMilleage = 75000
        lastServiceMilleage = 0
        engine = WilloughbyEngine(currentMilleage, lastServiceMilleage)
        self.assertTrue(engine.needService())

    def willougbyEngineTestCaseFalse(self):
        currentMilleage = 55000
        lastServiceMilleage = 0
        engine = WilloughbyEngine(currentMilleage, lastServiceMilleage)
        self.assertFalse(engine.needService())        