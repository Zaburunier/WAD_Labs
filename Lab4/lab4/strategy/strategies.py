from abc import ABC, abstractmethod


# Абстрактный класс для выбора стратегий ("Стратегия")
class SetStrategy(ABC):

    @abstractmethod
    def filteredSet(self, _set):
        pass


# Далее представлены конкретные стратегии фильтрации элементов множества


class NaturalStrategy(SetStrategy):

    def filteredSet(self, _set):
        return set(filter(lambda x: isinstance(x, int) and x > 0, _set))


class DiscreteStrategy(SetStrategy):

    def filteredSet(self, _set):
        return set(filter(lambda x: isinstance(x, int), _set))


class RealStrategy(SetStrategy):

    def filteredSet(self, _set):
        return set(filter(lambda x: isinstance(x, float), _set))


class StringStrategy(SetStrategy):

    def filteredSet(self, _set):
        return set(filter(lambda x: isinstance(x, str) and x[0].upper() == 'H', _set))