import unittest
from . import bfs

class BfsTest(unittest.TestCase):
    def test_bfs(self):
        adj = [[1], [3], [], [2]]
        self.assertEqual(bfs.bfs(0, adj), [0, 1, 3, 2])


if __name__ == '__main__':
    unittest.main()