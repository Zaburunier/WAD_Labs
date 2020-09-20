from abc import ABC, abstractmethod

class Shape(ABC):
    # Абстрактный метод вычисления площади
    @abstractmethod
    def Square(self):
        pass

    # Виртуальный метод возвращения типа
    def GetType(cls):
        return cls.shapeType.lower()

    # Виртуальный метод форматированного представления всех фигур
    def __repr__(shapeObject):
        return "Данная фигура является {0}ом, имеет {1} цвет, а её площадь равняется {2} на основании введённых числовых параметров:".format(shapeObject.GetType(), shapeObject.color.Color, shapeObject.Square())

    # Статический метод проверки корректности ввода числовых значений (для измерений)
    @staticmethod
    def CheckNumValue(num):
        try:
            # Проверяем возможность перевода в численный формат
            value = float(num)
            # Если возможно, то возвращаем полученное значение без изменений
            return value
        except ValueError:
            # Если преобразование типа невозможно, то требуем повторного ввода до тех пор, пока не получим число
            isNum = False
            while not isNum:
                print("Ошибка получения величины. Введите значение ещё раз")
                try:
                    value = float(input())
                    isNum = True
                except ValueError:
                    pass
            return value