from abc import ABC, abstractmethod
from lab_python_oop.Colour import ShapeColour


class GeometricShape(ABC):
    @abstractmethod
    def square(self):
        pass

    @classmethod
    def GetShapeType(cls) -> object:
        return cls.shapeType

    def checkType(measure):
        if isinstance(measure, (float, int)) is True:
            # 1. При вещественном типе вернётся целочисленный
            return measure
        else:
            print("Ошибка получения величины. Введите значение ещё раз")

    def __repr__(shapeObj):
        return "Полученная фигура - это {} с площадью {}.".format(shapeObj.GetShapeType(), shapeObj.square())



