import numpy as np

from src_avalon.shapes.shapes_base import ShapesBase

class Triangle(ShapesBase):
    def __init__(self, length1, length2, angle):
        self.length1 = length1
        self.length2 = length2
        self.angle = angle
        super().__init__()

    def _make_shape(self):
        length3 = np.sqrt(self.length1**2 + self.length2**2 - 2*self.length1*self.length2 * np.cos(self.angle))
        self._perimeter = self.length1 + self.length2 + length3
        self._shape = "Triangle"
        sp = self.perimeter / 2
        self._area = np.sqrt(sp * (sp - self.length1) * (sp - self.length2) * (sp - length3) )

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def shape(self):
        return self._shape
