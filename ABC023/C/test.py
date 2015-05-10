from main import *
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solve(3, 5, 3, [(1, 2), (2, 1), (2, 5), (3, 2), (3, 5)]), 5)
    def test_case2(self):
        self.assertEqual(solve(7, 3, 1, [(3, 2), (3, 3), (4, 2), (4, 3)]), 0)
    def test_case3(self):
        self.assertEqual(solve(5, 5, 2, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]), 20)

if __name__ == '__main__':
    unittest.main()
