from lab4.factory.context_abstract import SetContext


# Контекст работы с операций объединения множеств
class SetUnionContext(SetContext):

    def __init__(self, initialStrategy = None):
        self.strategy = initialStrategy

    def SetStrategy(self, newStrategy):
        SetContext.SetStrategy(self, newStrategy)

    def GetStrategy(self):
        SetContext.GetStrategy(self)

    def ExecuteOperation(self, set1, set2):
        filteredSet1 = self.strategy.filteredSet(set1)
        filteredSet2 = self.strategy.filteredSet(set2)
        return filteredSet1 | filteredSet2