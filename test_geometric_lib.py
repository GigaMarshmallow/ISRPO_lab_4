import unittest
import math

from rectangle import area as rect_area, perimeter as rect_perimeter
from triangle import area as tri_area, perimeter as tri_perimeter
from square import area as sq_area, perimeter as sq_perimeter
from circle import area as cir_area, perimeter as cir_perimeter

class RectangleTestCase(unittest.TestCase): 
    def test_ractangle_area(self):
       res = rect_area(10, 10)
       self.assertEqual(res, 100)

    def test_perimeter(self):
        res = rect_perimeter(15, 20)
        self.assertEqual(res, 70)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
       res = tri_area(10, 10)
       self.assertEqual(res, 50)

    def test_triangle_perimeter(self):
        res = tri_perimeter(5, 6, 7)
        self.assertEqual(res, 18)

class CircleTestCase(unittest.TestCase): 
    def test_circle_area(self):
       res = cir_area(3)
       self.assertAlmostEqual(res, 9 * math.pi)

    def test_circle_perimeter(self):
        res = cir_perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
       res = sq_area(10)
       self.assertEqual(res, 100)

    def test_square_perimeter(self):
        res = sq_perimeter(5)
        self.assertEqual(res, 20)