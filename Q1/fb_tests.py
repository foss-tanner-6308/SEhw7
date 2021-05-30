import unittest
from fb import *


class TestCase(unittest.TestCase):
    def test_3s_and_5s(self):
        self.assertEqual(fb_3_5(15), "FizzBuzz")

    def test_3s(self):
        self.assertEqual(fb_3(9), "Fizz")


if __name__ == "__main__":
    unittest.main()
