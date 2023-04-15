from abc import ABC, abstractmethod


class ShapesBase(ABC):
    def __init__(self, dimensions=2):
        self._dimensions = dimensions
        self._make_shape()

    @abstractmethod
    def _make_shape(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def shape(self):
        pass
