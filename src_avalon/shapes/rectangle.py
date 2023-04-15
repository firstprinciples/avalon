from src_avalon.shapes.shapes_base import ShapesBase


class Rectangle(ShapesBase):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def _make_shape(self):
        self._area = self.length * self.width
        self._perimeter = 2 * (self.length + self.width)
        self._shape = "Rectangle"

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def shape(self):
        return self._shape
