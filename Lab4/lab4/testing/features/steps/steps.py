from lab4.factory.context_intersection import SetIntersectionContext
from lab4.strategy.strategies import DiscreteStrategy
from behave import given, when, then

#Преобразуем строку из сценария теста в множество с элементами разного типа
def SetParser_BDD(str):

    def isfloat(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def isint(str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    # Удаляем фигурные скобки и запятые, после чего разбиваем строку на множество
    result = set(str[1:-1].replace(',', '').split())
    # Теперь необходимо произвести преобразование элементов обратно к своему типу
    newResult = set()
    for element in result:
        if element.startswith("\"") or element.startswith("\'"):
            # Если мы попали в строковый элемент, то убираем лишние кавычки
            newResult.add(element[1:-1])
        elif isint(element):
            # Если мы попали в целое число, то преобразуем его обратно в целое число
            newResult.add(int(element))
        elif isfloat(element):
            # Если мы попали в число с плавающей точкой, то преобразуем его обратно в число
            newResult.add(float(element))
    return newResult



@given("I have sets {set1} and {set2}")
def initialSets(context, set1, set2):
    context.set1 = SetParser_BDD(set1)
    context.set2 = SetParser_BDD(set2)


@when("I intersect them with discrete numbers strategy")
def operation(context):
    operationContext = SetIntersectionContext(DiscreteStrategy())
    context.result = operationContext.ExecuteOperation(context.set1, context.set2)


@then("I expect the result to be {expectedResult}")
def result(context, expectedResult):
    assert SetParser_BDD(expectedResult) == context.result
