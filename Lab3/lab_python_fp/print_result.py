from lab_python_fp.gen_random import genRandom


def printResult_decorator(funcToPrint):
    def decorating(*args, **kwargs):
        funcResult = funcToPrint(*args, **kwargs)
        print("Function {0} returns: ".format(funcToPrint.__name__), end = '')
        if isinstance(funcResult, list):
            print()
            for listElement in funcResult:
                print(listElement)
        elif isinstance(funcResult, dict):
            print()
            for dictElement in funcResult.items():
                print("Key = {0} -> Value = {1}".format(dictElement[0], dictElement[1]))
        else:
            print(funcResult)
        print("_" * 20)
        return funcResult
    return decorating


@printResult_decorator
def func1(a = 0):
    return a


@printResult_decorator
def func2(a = 1, b = 1, c = 1):
    return [i for i in genRandom(a, b, c)]


@printResult_decorator
def func3(a = 1, b = 1, c = 1):
    valueList = genRandom(a, b, c)
    dictionary = dict()
    for num in valueList:
        dictionary[num] = num
    return dictionary


if __name__ == "__main__":
    func1(1)
    func2(6, -50, 50)
    func3(6, -10, 10)