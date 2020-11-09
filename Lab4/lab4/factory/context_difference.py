from lab4.factory.context_abstract import SetContext
import random


# Контекст работы с операций разности множеств
class SetDifferenceContext(SetContext):

    def __init__(self, initialStrategy = None):
        self.strategy = initialStrategy

    def SetStrategy(self, newStrategy):
        SetContext.SetStrategy(self, newStrategy)

    def GetStrategy(self):
        SetContext.GetStrategy(self)

    def ExecuteOperation(self, set1, set2):

        # Для демонстрации необходимости mock-объектов
        def genRandom(amountOfNums, minNum, maxNum):
            for i in range(amountOfNums):
                yield random.randint(minNum, maxNum)

        set1 = set([i for i in genRandom(1000000, -5, 5)])
        filteredSet1 = self.strategy.filteredSet(set1)
        filteredSet2 = self.strategy.filteredSet(set2)
        return filteredSet1 - filteredSet2
