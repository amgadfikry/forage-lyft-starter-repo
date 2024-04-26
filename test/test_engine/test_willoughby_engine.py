import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        willoughby_engine = WilloughbyEngine(80001, 20000)
        self.assertTrue(willoughby_engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        willoughby_engine = WilloughbyEngine(70000, 20000)
        self.assertFalse(willoughby_engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
