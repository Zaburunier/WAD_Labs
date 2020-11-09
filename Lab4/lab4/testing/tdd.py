from lab4.strategy.strategies import NaturalStrategy, DiscreteStrategy, RealStrategy, StringStrategy
from lab4.factory.context_union import SetUnionContext
from lab4.factory.context_intersection import SetIntersectionContext
from lab4.factory.context_difference import SetDifferenceContext
import unittest


class UnionTesting(unittest.TestCase):
    set1 = { 18, 324.7, "123x", -7, 6.13871245 }
    set2 = { "Hello, unittest world!", "hey", -7.62, 1, 18 }

    # Проверка для RealStrategy
    def testFloat(self):
        context = SetUnionContext(RealStrategy())
        unionSet = context.ExecuteOperation(self.set1, self.set2)
        # Строка не должна входить в итоговое множество, а действительное число - должно
        self.assertNotIn("123x", unionSet)
        self.assertIn(-7.62, unionSet)

    # Проверка для DiscreteStrategy
    def testDiscrete(self):
        context = SetUnionContext(DiscreteStrategy())
        unionSet = context.ExecuteOperation(self.set1, self.set2)
        # Единица должна остаться как часть множества целых чисел
        self.assertIn(1, unionSet)

    # Проверка для NaturalStrategy
    def testNatural(self):
        context = SetUnionContext(NaturalStrategy())
        unionSet = context.ExecuteOperation(self.set1, self.set2)
        # В двух множествах заданы всего два различных натуральных числа
        self.assertEqual(set([1, 18]), unionSet)

    # Проверка для StringStrategy
    def test_str(self):
        context = SetUnionContext(StringStrategy())
        unionSet = context.ExecuteOperation(self.set1, self.set2)
        # Остаются только те строки, которые начинаются с символа "H/h"
        self.assertTrue(unionSet == set(["hey", "Hello, unittest world!"]))




if __name__ == '__main__':
    unittest.main()