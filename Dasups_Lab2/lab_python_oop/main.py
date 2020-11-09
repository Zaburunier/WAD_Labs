from abc import ABC, abstractmethod


class GeometricShape(ABC):
    @abstractmethod
    def square(self):
        pass