from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.GeometricShape import GeometricShape
from lab_python_oop.Colour import ShapeColour


class Square(Rectangle):
    shapeType = "квадрат"

    def __init__(self, side):
        self.side = GeometricShape.checkType(side)
        # self.colour = ShapeColour.checkString(colour)

    def square(self):
        return self.side ** 2

    def __repr__(self):
        return GeometricShape.__repr__(self) + "\nДлина стороны квадрата = {}".format(self.side)
