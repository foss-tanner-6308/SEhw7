import unittest
from ly import *


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(lpy(2000), "2000 is a leap year")


if __name__ == "__main__":
    unittest.main()