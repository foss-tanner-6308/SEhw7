import unittest
from ly import *


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(lpy_1(2000), "2000 is a leap year")

    def test_two(self):
        self.assertEqual(lpy_2(60), "60 is not a leap year")


if __name__ == "__main__":
    unittest.main()