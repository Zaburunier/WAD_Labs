from lab_python_fp.gen_random import genRandom
from types import GeneratorType


class UniqueIterator:
    def __init__(self, **kwargs):
        self.currentIndex = 0
        self.usedElements = set()
        # Насколько правильно использован kwargs?
        self.ignoreCase = kwargs.get("ignoreCase")
        data = kwargs.get("data")
        if isinstance(data, GeneratorType):
            # Если на вход получен генератор, то необходимо создать коллекцию
            self.data = list()
            for generatorElement in data:
                self.data.append(generatorElement)
        else:
            self.data = data
        self.length = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.currentIndex >= self.length:
                raise StopIteration
            else:
                currentElement = self.data[self.currentIndex]
                self.currentIndex = self.currentIndex + 1
                if isinstance(currentElement, str) and self.ignoreCase == True:
                    condition = currentElement.lower()
                else:
                    condition = currentElement
                if (condition) not in self.usedElements:
                    self.usedElements.add(condition)
                    return currentElement

# Простой генератор латинского алфавита на основе ASCII-таблицы
# Значения выбрасываются по парам из строчной и прописной букв
def genAlphabet():
    index = 65
    while index <= 90:
        yield chr(index)
        yield chr(index + 32)
        index = index + 1


if __name__ == "__main__":
    randomGenerator = genRandom(10, -13, 3)
    alphabetGenerator = genAlphabet()
    for i in UniqueIterator(data = alphabetGenerator, ignoreCase = True):
        print(i)
