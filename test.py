from main import *
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(5, solve(3, 5, 3, [(1, 2), (2, 1), (2, 5), (3, 2), (3, 5)]))

if __name__ == '__main__':
    unittest.main()
