from lab_python_oop.shape import Shape
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import Color


class Quadrate(Rectangle):
    shapeType = "Квадрат"

    @classmethod
    def GetType(cls):
        return Shape.GetType(cls)

    def __init__(self, argsList):
        print("Записываем cторону...")
        self.dim = Shape.CheckNumValue(argsList[0] if len(argsList) >= 1 else '.')
        print("Записываем цвет...")
        self.color = Color(argsList[1] if len(argsList) >= 2 else '0')
        print("Запись для квадрата завершена!")


    def Square(self):
        return self.dim * self.dim

    def __repr__(self):
        return Shape.__repr__(self) + "\nСторона: {}".format(self.dim)