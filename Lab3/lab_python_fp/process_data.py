import json
from lab_python_fp.print_result import printResult_decorator
from lab_python_fp.unique import UniqueIterator
from lab_python_fp.cm_timer import Timer_CM_Class
from lab_python_fp.field import field
from lab_python_fp.gen_random import genRandom

@printResult_decorator
def f1(dataFile):
    # Правомерно ли с точки зрения задания модифицировать исходный регистр?
    return sorted(vocation.capitalize() for vocation in UniqueIterator(data = field(dataFile, "job-name"), ignoreCase = True))


@printResult_decorator
def f2(sortedData):
    return list(filter(lambda x : "Программист" in x, sortedData))


@printResult_decorator
def f3(filteredData):
    return list(map(lambda x : x + " с опытом Python.", filteredData))


@printResult_decorator
def f4(modifiedData):
    return list(str(info[0]) + " Зарплата: " + str(info[1]) + "!" for info in zip(modifiedData,genRandom(len(modifiedData), 100000, 200000)))


if __name__ == "__main__":
    data = list()
    with open("d:\\study\\5_Семестр\\РИП\\Lab3\\data_light.json", 'r', encoding = 'utf8') as data_file:
        data = json.load(data_file)
    with Timer_CM_Class():
        f4(f3(f2(f1(data))))