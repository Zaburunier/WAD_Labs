from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square



if __name__ == '__main__':
    rctg = Rectangle(float(input()), 17.2, "Кутой")
    print(rctg)
    crc = Circle(10.5)
    print(crc)
    sqre = Square(10.5)
    print(sqre)