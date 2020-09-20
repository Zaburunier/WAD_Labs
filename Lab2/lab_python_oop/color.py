class Color:
    # Статический метод проверки корректности ввода строки цвета
    @staticmethod
    def CheckColorValue(value):
        isNum = not value.isalpha()
        # Если введенно некорректное значение, то требуем повторного ввода до тех пор, пока не получим буквенную строку
        while isNum:
            print("Ошибка получения цвета. Введите значение ещё раз")
            value = input()
            isNum = not value.isalpha()
        return value

    def __init__(self, colorValue):
        self.color = Color.CheckColorValue(colorValue)

    # Св-во цвета
    @property
    def Color(self):
        return self.color.lower()

    @Color.setter
    def Color(self, colorValue):
        colorValue = self.CheckColorValue(colorValue)
        self.color = colorValue

