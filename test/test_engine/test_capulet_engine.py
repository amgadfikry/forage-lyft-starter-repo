import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        capulet_engine = CapuletEngine(50001, 20000)
        self.assertTrue(capulet_engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        capulet_engine = CapuletEngine(40000, 20000)
        self.assertFalse(capulet_engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
