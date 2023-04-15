import unittest
import numpy as np

from src_avalon.shapes.circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.radius = 5
        self.circle = Circle(self.radius)

    def test_area(self):
        expected_area = np.pi * self.radius**2
        self.assertEqual(self.circle.area, expected_area)

    def test_perimeter(self):
        self.expected_perimeter = 2 * np.pi * self.radius
        self.assertEqual(self.circle.perimeter, self.expected_perimeter)
