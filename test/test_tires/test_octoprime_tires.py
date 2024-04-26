import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
  def test_tires_true_needs_service(self):
    tires = OctoprimeTires([1, 1, 0.7, 0.3])
    self.assertTrue(tires.needs_service())
  
  def test_tires_false_needs_service(self):
    tires = OctoprimeTires([0.5, 0.9, 0.6, 0.1])
    self.assertFalse(tires.needs_service())

if __name__ == '__main__':
  unittest.main()
