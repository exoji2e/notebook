import unittest
from . import dinitz

class FlowTest(unittest.TestCase):
    def test_small_bipartite(self):
        net = dinitz.Dinitz(8)
        S = 0
        T = 7
        for i in range(3):
            net.add_edge(S, i+1, 1)
            net.add_edge(i+4, T, 1)

        net.add_edge(1, 4, 1)
        net.add_edge(1, 5, 1)
        net.add_edge(1, 6, 1)
        net.add_edge(2, 4, 1)
        net.add_edge(3, 5, 1)
        self.assertEqual(net.max_flow(S, T), 3)



if __name__ == '__main__':
    unittest.main()