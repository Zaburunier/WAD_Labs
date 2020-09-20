import math
import sys


def NumInput(argName, index):
    try:
        arg = float(sys.argv[index])
        if (arg == 0.0 and index == 1):
            print("Коэффициент", argName, "не может принимать нулевое значение!")
            raise ValueError
        print("Коэффициент", argName, "прочитан из командной строки и равен", arg)
        return arg
    except:
        print("Ошибка чтения коэффициента", argName, "из командной строки. Требуется ручной ввод...")
        print("Введите коэффициент ", argName, ": ", sep = '', end = '')
        # Вводим до тех пор, пока не получим корректное (численное) значение
        while (True):
            inputNum = input()
            try:
                num = float(inputNum)
                if (num == 0.0 and index == 1):
                    print("Коэффициент A не может принимать нулевое значение!")
                    raise ValueError
                return num
            except:
                print("Произошла ошибка ввода. Введите коэффициент ", argName, " ещё раз: ", sep = '', end = '')


def PrintEquation(a, b, c):
    print("Решаем уравнение ", sep = '', end = '')
    print(a, "*(x^4)", sep = '', end = '')
    if (b < 0):
        print(" - ", sep = '', end = '')
        print(-b, "*(x^2)", sep = '', end = '')
    else:
        print(" + ", sep = '', end = '')
        print(b, "*(x^2)", sep = '', end = '')
    if (c < 0):
        print(" - ", sep = '', end = '')
        print(-c, " = 0", sep = '', end = '')
    else:
        print(" + ", sep = '', end = '')
        print(c, " = 0...", sep = '', end = '')
    pass


def SolveEquation(a, b, c):
    # print("\n\nДелаем замену y = x^2...")
    d = b * b - 4 * a * c;
    # print("D = ", d, sep = '')
    bRoots = list()
    if (d > 0):
        # Дискриминант положительный, два различных действительных корня
        bRoots.append((-b + math.sqrt(d)) / (a * 2))
        bRoots.append((-b - math.sqrt(d)) / (a * 2))
    elif (d == 0):
        # Дискриминант нулевой, два совпадающих действительных корня
        bRoots.append(-0.5 * (b / a))
    else:
        # Дискриминант отрицательный, два различных комплексных корня
        compRootRealPart = -0.5 * (b / a)
        compRootImaginaryPart = 0.5 * math.sqrt(-d) / a
        bRoots.append(complex(compRootRealPart, compRootImaginaryPart))
        bRoots.append(complex(compRootRealPart, -compRootImaginaryPart))
    # print("Полученные корни: ")
    # print(bRoots)
    # print("Переходим к исходному уравнению...")
    roots = list()
    for r in bRoots:
        if (type(r) is float):
            if (r > 0):
                # Для каждого действительного положительного значения есть два корня исходного уравнения
                roots.append(math.sqrt(r))
                roots.append(-math.sqrt(r))
            elif (r == 0):
                # Для каждого нуля корень - сам ноль
                roots.append(0)
            else:
                # Для каждого действительного отрицательного значения есть комплексный корень исходного уравнения
                roots.append(complex(0, math.sqrt(-r)))
        elif (type(r) is complex):
            # Для каждого комплексного значения есть два комплексных корня исходного уравнения
            sqrSum = math.sqrt(r.real * r.real + r.imag * r.imag)
            compRootRealPart = math.sqrt(0.5 * (sqrSum + r.real))
            compRootImaginaryPart = math.sqrt(0.5 * (sqrSum - r.real))
            roots.append(complex(compRootRealPart, compRootImaginaryPart))
            roots.append(complex(-compRootRealPart, -compRootImaginaryPart))

    # В последнюю очередь проверяем на дубликаты и избавляемся
    rootsCopy = list(roots)
    roots = list()
    for r in rootsCopy:
        if (r not in roots):
            roots.append(r)
    return roots


def PrintRoots(roots):
    print("\nОтвет: ")
    for root in roots:
        if (type(root) is complex):
            if (root.real == 0.0):
                print("Комплексное число: ", root.imag, "j", sep = "")
            else:
                print("Комплексное число: ", root.real, " + ", root.imag, "j", sep = "")
        else:
            print("Действительное число:", root)
    pass

if __name__ == '__main__':
    print("Забурунов Леонид Вячеславович, группа РТ5-51Б")
    print("Программа предназначена для решения уравнения вида [A * x^4 + B * x^2 + C = 0]")
    print("Вам будет предложено ввести численные коэффициенты A, B и C, после чего программа выдаст результат\n")
    a = NumInput('A', 1)
    b = NumInput('B', 2)
    c = NumInput('C', 3)
    print()
    PrintEquation(a, b, c)
    PrintRoots(SolveEquation(a, b, c))

