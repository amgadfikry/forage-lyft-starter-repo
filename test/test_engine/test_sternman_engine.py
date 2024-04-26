import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        sternman_engine = SternmanEngine(True)
        self.assertTrue(sternman_engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        sternman_engine = SternmanEngine(False)
        self.assertFalse(sternman_engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
