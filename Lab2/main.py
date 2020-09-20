from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.quadrate import Quadrate
import numpy as np

if __name__ == '__main__':
    print("Забурунов Леонид Вячеславович, группа РТ5-51Б. Лабработа #2")
    print("Программа проверяет функционал созданных по заданию лабораторной работы модулей.")
    print("Вам будет предложено ввести данные для прямоугольника, круга и квадрата. Ввод для каждого объекта осуществляется в одну строку, через пробел.")
    print("Введите данные прямоугольника: ")
    rctg = Rectangle(input().split())
    print("Введите данные круга: ")
    crc = Circle(input().split())
    print("Введите данные квадрата: ")
    qdr = Quadrate(input().split())
    print('Итоги ввода: ', rctg, crc, qdr, sep = '3\n')
    print('\n', np.ones((3, 20), float))

