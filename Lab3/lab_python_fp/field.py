def field(dicts, *args):
    if len(args) > 1:
        for dictionary in dicts:
            for arg in args:
                if arg not in dictionary.keys():
                    break
            else:
                yield dictionary
    elif len(args) > 0:
        for dictionary in dicts:
            for dictKey in dictionary.keys():
                for arg in args:
                    if dictKey == arg:
                        yield dictionary.get(dictKey)


if __name__ == "__main__":
    goods = [
        { "title": "Ковёр", "price": 1000, "color": "Чёрный" },
        { "title": "Диван", "price": 5300, "color": "Белый" },
        { "title": "Шкаф-купе", "price": 6000, "color": "Белый" },
        { "price": 2000, "color": "Красный" },
        { "title": "Картина", "price": 800 },
        { "title": "Бабушкино кресло", "color": "Чёрный" }
    ]
    print("Проверка для одного аргумента:")
    genObject = field(goods, 'title')
    for i in genObject:
        print(i)
    print("Проверка для наименования и цены вместе:")
    genObject = field(goods, "title", "price")
    for i in genObject:
        print(i)
    print("Проверка для наименования и цвета вместе:")
    genObject = field(goods, "title", "color")
    for i in genObject:
        print(i)
    print("Проверка для цены и цвета вместе:")
    genObject = field(goods, "price", "color")
    for i in genObject:
        print(i)
