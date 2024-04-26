import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
  def test_tires_true_needs_service(self):
    tires = CarriganTires([0.9, 0.1, 0, 0.8])
    self.assertTrue(tires.needs_service())
  
  def test_tires_false_needs_service(self):
    tires = CarriganTires([0.5, 0.1, 0.8, 0.8])
    self.assertFalse(tires.needs_service())

if __name__ == '__main__':
  unittest.main()
