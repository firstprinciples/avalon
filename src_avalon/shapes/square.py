from src_avalon.shapes.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def _make_shape(self):
        super()._make_shape()
        self._shape = "Square"

    @property
    def shape(self):
        return self._shape
