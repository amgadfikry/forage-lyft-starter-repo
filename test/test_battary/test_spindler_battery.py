import datetime
import unittest
from battary.spindler_battery import SpindlerBattary

class TestSpindlerBattery(unittest.TestCase):
  def test_true_need_service(self):
    current_date = datetime.date(2020, 1, 2)
    last_service_date = datetime.date(2017, 1, 1)
    spindler_battery = SpindlerBattary(current_date, last_service_date)
    self.assertTrue(spindler_battery.need_service())

  def test_false_need_service(self):
    current_date = datetime.date(2019, 1, 1)
    last_service_date = datetime.date(2018, 1, 1)
    spindler_battery = SpindlerBattary(current_date, last_service_date)
    self.assertFalse(spindler_battery.need_service())

if __name__ == '__main__':
  unittest.main()
