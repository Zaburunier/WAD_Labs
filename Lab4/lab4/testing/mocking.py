import unittest
from unittest.mock import patch
from lab4.factory.context_difference import SetDifferenceContext
from lab4.strategy.strategies import DiscreteStrategy, NaturalStrategy


# Для примера с подстановкой функции
def mock_setdiff(set1, set2):
    return set1 - set2


class DiffTesting(unittest.TestCase):
    set1 = set([13, -6.1847356, "Hello, mock-object world!", -2,  4, "Lab4"])
    set2 = set([4, -1.4142])

    # Демонстрация затрат времени при тестировании без заглушек
    def testWithoutMocks(self):
        context = SetDifferenceContext(DiscreteStrategy())
        diffSet = context.ExecuteOperation(self.set1, self.set2)
        self.assertIn(1, diffSet)

    # Демонстрация работы с mock-объектом при задании возвращаемого значения функции
    @patch("lab4.factory.context_difference.SetDifferenceContext.ExecuteOperation", return_value = 13)
    def testWithPatch_return(self, ExecuteOperation):
        self.assertEqual(SetDifferenceContext(NaturalStrategy()).ExecuteOperation(self.set1, self.set2), 13)

    # Демонстрация работы с mock-объектом при задании подменяющей функции
    @patch("lab4.factory.context_difference.SetDifferenceContext.ExecuteOperation", side_effect = mock_setdiff)
    def testWithPatch_side(self, ExecuteOperation):
        self.assertTrue(
            SetDifferenceContext(NaturalStrategy()).ExecuteOperation(self.set1, self.set2) >
                        set([]))
