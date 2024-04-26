import unittest
import datetime
from battary.nubbin_battery import NubbinBattary

class TestNubbinBattery(unittest.TestCase):
  def test_true_need_service(self):
    current_date = datetime.date(2020, 1, 1)
    last_service_date = datetime.date(2015, 1, 1)
    nubbin_battery = NubbinBattary(current_date, last_service_date)
    self.assertTrue(nubbin_battery.need_service())

  def test_false_need_service(self):
    current_date = datetime.date(2019, 1, 1)
    last_service_date = datetime.date(2016, 1, 1)
    nubbin_battery = NubbinBattary(current_date, last_service_date)
    self.assertFalse(nubbin_battery.need_service())

if __name__ == '__main__':
  unittest.main()