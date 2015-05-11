from main import *
import unittest

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(23, solve([(5, 6), (12, 4), (14, 7), (21, 2)]))
    def test_case2(self):
        self.assertEqual(105, solve([(100, 1), (100, 1), (100, 1), (100, 1), (100, 1), (1, 30)]))
                
if __name__ == '__main__':
    unittest.main()
