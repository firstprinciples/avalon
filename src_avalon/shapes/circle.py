import numpy as np

from src_avalon.shapes.shapes_base import ShapesBase


class Circle(ShapesBase):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def _make_shape(self):
        self._area = np.pi * self.radius**2
        self._perimeter = 2 * np.pi * self.radius
        self._shape = "Circle"

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def shape(self):
        return self._shape
