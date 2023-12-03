import unittest
import random
from .fenwick_tree import FenwickTree

class NaiveFenwick:
    def __init__(self, sz):
        self.data = [0]*sz
    def query(self, a, b):
        return sum(self.data[a:b+1])
    def assign(self, i, v):
        self.data[i] = v
    def inc(self, i, v):
        self.data[i] += v

def randint(sz):
    return random.randint(0, sz-1)

class FenwickTreeTest(unittest.TestCase):
    def test_manual(self):
        tree = FenwickTree(10)
        tree[0] = 5
        tree[1] = 4
        self.assertEqual(tree.query(0, 1), 9)
        self.assertEqual(tree[:2], 9)
        self.assertEqual(tree[0], 5)
        t2 = FenwickTree([1, 2, 3, 4])
        self.assertEqual(t2[1:], 9)

    def test_fuzz(self):
        for sz in [1, 10, 100, 1000]:
            with self.subTest(sz=sz):
                random.seed(0)
                real = FenwickTree(sz)
                naive = NaiveFenwick(sz)
                for _ in range(1000):
                    pos = randint(sz)
                    delta = random.randint(-1000, 1000)
                    real.inc(pos, delta)
                    naive.inc(pos, delta)
                    l, r = sorted([randint(sz), randint(sz)])
                    self.assertEqual(real.query(l, r), naive.query(l, r))
                    self.assertEqual(real.query(0, sz-1), naive.query(0, sz-1))


if __name__ == '__main__':
    unittest.main()