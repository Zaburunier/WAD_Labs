from lab_python_oop.shape import Shape
from lab_python_oop.color import Color

class Rectangle(Shape):
    shapeType = "Прямоугольник"

    @classmethod
    def GetType(cls):
        return Shape.GetType(cls)

    def __init__(self, argsList):
        print("Записываем ширину...")
        self.width = Shape.CheckNumValue(argsList[0] if len(argsList) >= 1 else '.')
        print("Записываем высоту...")
        self.height = Shape.CheckNumValue(argsList[1] if len(argsList) >= 2 else '.')
        print("Записываем цвет...")
        self.color = Color(argsList[2] if len(argsList) >= 3 else '0')
        print("Запись для прямоугольника завершена!")


    def Square(self):
        return self.width * self.height

    def __repr__(self):
        return Shape.__repr__(self) + "\nШирина: {0} \nВысота: {1}".format(self.width, self.height)