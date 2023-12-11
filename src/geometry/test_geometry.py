import unittest
from . import geometry

class GeometryTest(unittest.TestCase):
    def test_line_intersect(self):
        segment_tests = [
            (((0,0),(3,3)), ((2,2), (4,4)), True), # same line overlap
            (((0,0),(3,3)), ((3,3), (4,4)), True), # same line touch
            (((0,0),(2,2)), ((3,3), (4,4)), False), # same line no overlap
            (((0,0),(3,3)), ((3,0), (0,3)), True), # orthogonal regular
            (((0,0),(3,3)), ((6,0), (0,6)), True), # orthogonal touch
            (((0,0),(3,3)), ((7,0), (0,7)), False), # orthogonal outside
        ]
        for s1, s2, res in segment_tests:
            self.assertEqual(geometry.is_segment_intersection(s1, s2), res)


if __name__ == '__main__':
    unittest.main()