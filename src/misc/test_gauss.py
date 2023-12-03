import unittest
from .gauss import gauss
class M2:
    def __init__(self, v):
        self.v = v%2
    def __add__(self, m):
        return M2(self.v ^ m.v)
    def __mul__(self, m):
        return M2(self.v * m.v)
    def __sub__(self, m):
        return M2(self.v ^ m.v)
    def __truediv__(self, m):
        if m.v == 0:
            raise ValueError
        return M2(self.v)
    def isZ(self):
        return self.v == 0

class BootstrapTest(unittest.TestCase):
    def testMod2(self):
        A = [[M2(0), M2(1)], [M2(1), M2(1)]]
        b = [M2(0), M2(1)]
        x = gauss(A, b, monoid=M2)
        self.assertTrue(x[0].v == 1 and x[1].v == 0)

    def test_regular(self):
        A = [[1., 2., 3.], [4., 5., 6.], [7., 8., 10.,]]
        b = [13., 31., 52.]
        x = gauss(A, b)
        tol = 1e-8
        self.assertTrue(abs(x[0] - 2) < tol and abs(x[1] - 1) < tol and abs(x[2] - 3) < tol)

if __name__ == '__main__':
    unittest.main()