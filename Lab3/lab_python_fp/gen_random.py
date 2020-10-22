import random


def genRandom(amountOfNums, minNum, maxNum):
    for i in range(amountOfNums):
        yield random.randint(minNum, maxNum)


if __name__ == "__main__":
    nums = genRandom(16, 3, 97)
    for i in nums:
        print(i)