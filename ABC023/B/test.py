from main import *
import unittest

class Test(unittest.TestCase):
    def test_case0(self):
        self.assertEqual(solve("b"), 0)
    def test_case1(self):
        self.assertEqual(solve("abc"), 1)
    def test_case2(self):
        self.assertEqual(solve("cabca"), 2)
    def test_case3(self):
        self.assertEqual(solve("bcabcab"), 3)
    def test_case4(self):
        self.assertEqual(solve("abcabcabc"), 4)
    def test_case5(self):
        self.assertEqual(solve("cabcabcabca"), 5)
    def test_case6(self):
        self.assertEqual(solve("bcabcabcabcab"), 6)

if __name__ == '__main__':
    unittest.main()
