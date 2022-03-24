import unittest
from datetime import date
from Battery.nubbinBattery import NubbinBattery
from Battery.spindlerBattery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def nubbinBatteryTestCaseTrue(self):
        current_date = date.fromisoformat("2021-04-05")
        last_service_date = date.fromisoformat("2020-07-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def nubbinBatteryTestCaseFalse(self):
        current_date = date.fromisoformat("2021-04-05")
        last_service_date = date.fromisoformat("2020-07-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def spindlerBatteryTestCaseTrue(self):
        current_date = date.fromisoformat("2021-04-05")
        last_service_date = date.fromisoformat("2020-07-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def spindlerBatteryTestCaseFalse(self):
        current_date = date.fromisoformat("2021-04-05")
        last_service_date = date.fromisoformat("2020-07-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

