
from lab_python_fp.gen_random import genRandom


if __name__ == "__main__":
    generator = genRandom(20, -10, 10)
    data = list()
    for num in generator:
        data.append(num)
    print(data)
    # Насколько верна задумка?
    # без лямбда-выражения
    print("No lambda:")
    print(list(i[1] for i in reversed(sorted(zip([abs(num) for num in data], data)))))
    # с лямбда-выражением
    print("Lambda:")
    print(list(i[1] for i in reversed(sorted(zip(map(lambda x: abs(x), data), data)))))


