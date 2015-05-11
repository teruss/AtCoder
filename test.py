from main import *
import unittest
import old
from random import *

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(5, solve(3, 5, 3, [(1, 2), (2, 1), (2, 5), (3, 2), (3, 5)]))
    def test_old(self):
        self.assertEqual(old.solve(3, 5, 3, [(1, 2), (2, 1), (2, 5), (3, 2), (3, 5)]), solve(3, 5, 3, [(1, 2), (2, 1), (2, 5), (3, 2), (3, 5)]))   

    def test_random(self):
        R = randint(1, 5)
        C = randint(1, 5)
        K = randint(1, R * C)
        N = randint(1, K)
        rc = []
        for i in range(N):
            r = randint(1, R)
            c = randint(1, C)
            while (r, c) in rc:
                r = randint(1, R)
                c = randint(1, C)
            rc.append((r, c))
        print R, C, K, N, rc
        self.assertEqual(old.solve(R, C, K, rc), solve(R, C, K, rc))

    @unittest.skip("skip")
    def test_forever(self):
        while True:
            self.test_random()

    def test_y(self):
        R = 4
        C = 4
        K = 1
        rc = [(2, 3)]
        self.assertEqual(7, solve(R, C, K, rc))

    def test_x(self):
        R = 17
        C = 43
        K = 2
        rc = [(47, 15), (21, 21), (5, 17), (23, 16), (32, 49), (4, 5), (11, 7), (45, 27), (19, 49), (46, 6), (9, 9), (23, 2), (37, 8), (1, 41), (10, 33), (10, 31), (46, 50), (26, 44), (14, 9), (47, 29), (27, 43), (49, 47), (45, 45), (29, 36), (11, 19), (31, 17), (22, 44), (19, 5), (3, 9)]
        self.assertEqual(402, solve(R, C, K, rc))
                
if __name__ == '__main__':
    unittest.main()
