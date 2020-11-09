class ShapeColour:
    @staticmethod
    def checkString(colourStr):
        if isinstance(colourStr, str) is True:
            return colourStr
        else:
            return "Название цвета должно быть строкой!"

    def __init__(self, colourValue):
        self.colour = ShapeColour.checkString(colourValue)

    @property
    def colour(self):
        return self.colour

    @colour.setter
    def colour(self, colourValue):
        colourValue = self.checkString(colourValue)
        self.colour = colourValue
