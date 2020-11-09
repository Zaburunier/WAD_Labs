from abc import ABC, abstractmethod


# Абстрактный класс для контекстов ("Фабрика")
class SetContext(ABC):

    #Внесение стратегии отбора элементов множества как поля класса контекста ("Мост")
    def SetStrategy(self, newStrategy):
        self.strategy = newStrategy

    def GetStrategy(self):
        return self.strategy

    @abstractmethod
    def ExecuteOperation(self, set1, set2):
        pass