from union_find import UnionFind
import unittest

class UnionFindTest(unittest.TestCase):
    def test(self):
        uf = UnionFind(10)
        self.assertEqual(uf.union(0, 1), True)
        self.assertEqual(uf.union(1, 2), True)
        self.assertEqual(uf.union(3, 4), True)
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertEqual(uf.find(1), uf.find(2))
        self.assertEqual(uf.find(3), uf.find(4))
        self.assertEqual(uf.union(0, 2), False)

if __name__ == '__main__':
    unittest.main()