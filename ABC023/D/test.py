from main import *
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solve([(5, 6), (12, 4), (14, 7), (21, 2)]), 23)

if __name__ == '__main__':
    unittest.main()
