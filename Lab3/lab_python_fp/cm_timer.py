import time
from lab_python_fp.gen_random import genRandom
from contextlib import contextmanager


class Timer_CM_Class:
    def __init__(self):
        print("Created (class instance)")
        self.timer = None


    def __enter__(self):
        self.timer = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer = time.time() - self.timer
        print("Time: {0}".format(self.timer))
        print("Left (class instance)")


@contextmanager
def Timer_CM_Lib():
    print("Entered (func with contextlib)")
    timer = time.time()
    [i for i in genRandom(80000, -10, 10)]
    yield time.time() - timer
    print("Left (func with contextlib)")


if __name__ == "__main__":
    timer1 = Timer_CM_Class()
    with timer1:
        [i for i in genRandom(80000, -10, 10)]
    timer2 = Timer_CM_Lib()
    with timer2 as cm:
        print("Time: {0}".format(cm))