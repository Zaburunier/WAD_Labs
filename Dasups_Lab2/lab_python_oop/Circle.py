from lab_python_oop.GeometricShape import GeometricShape
from lab_python_oop.Colour import ShapeColour
from math import pi


class Circle(GeometricShape):
    shapeType = "круг"

    def __init__(self, radius):
        self.radius = GeometricShape.checkType(radius)
        # self.colour = ShapeColour.checkString(colour)

    def square(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return GeometricShape.__repr__(self) + "\nРадиус = {}".format(self.radius)