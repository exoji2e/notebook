import unittest
from segment_tree import SegmentTree

class SegmentTreeTest(unittest.TestCase):
    def test(self):
        t1 = SegmentTree([1, 2, 3], func=min)
        self.assertEqual(1, t1[0:3])
        t2 = SegmentTree([4, 3, 2, 1], func=lambda x, y: x + y)
        self.assertEqual(7, t2[:2])
        self.assertEqual(10, t2[:])
        self.assertEqual(3, t2[2:])
        t2[1] = 10
        self.assertEqual(14, t2.query(0, 1))
        t2.inc(2, 1)
        self.assertEqual(17, t2.query(0, 2))

if __name__ == '__main__':
    unittest.main()