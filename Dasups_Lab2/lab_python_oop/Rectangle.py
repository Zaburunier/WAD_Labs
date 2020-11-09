from lab_python_oop.GeometricShape import GeometricShape
from lab_python_oop.Colour import ShapeColour


class Rectangle(GeometricShape):
    shapeType = "прямоугольник"

    def __init__(self, height, width, colour):
        # print("Введите значение высоты прямоугольника:")
        self.height = GeometricShape.checkType(height)
        # print("Введите значение ширины прямоугольника:")
        self.width = GeometricShape.checkType(width)
        # print("Введите цвет прямоугольника:")
        self.colour = ShapeColour.checkString(colour)

    def square(self):
        return self.height * self.width

    def __repr__(self):
        return GeometricShape.__repr__(self) + "\nВысота = {}\nШирина = {}".format(self.height, self.width)