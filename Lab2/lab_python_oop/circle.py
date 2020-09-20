from lab_python_oop.shape import Shape
from lab_python_oop.color import Color
from math import pi as PI


class Circle(Shape):
    shapeType = "Круг"

    @classmethod
    def GetType(cls):
        return Shape.GetType(cls)

    def __init__(self, argsList):
        print("Записываем радиус...")
        self.radius = Shape.CheckNumValue(argsList[0] if len(argsList) >= 1 else '.')
        print("Записываем цвет...")
        self.color = Color(argsList[1] if len(argsList) >= 2 else '0')
        print("Запись для круга завершена!")

    def Square(self):
        return PI * self.radius * self.radius

    def __repr__(self):
        return Shape.__repr__(self) + "\nРадиус: {}".format(self.radius)