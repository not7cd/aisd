import sys
import logging
import timeit
import random
import matplotlib.pyplot as plt

from straight_selection import solution as solution

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_sorted(f):
    A = [9, 4, 2, 5, 8, 7, 8]
    logger.info(f)
    B = f(A)
    if all(B[i] <= B[i + 1] for i in range(len(B) - 1)):
        pass
    else:
        raise Exception(B)


def time_test_gen():
    for n in range(10, 500, 10):
        A = [random.random() for _ in range(n)]
        logger.debug(A)
        timer = timeit.Timer(f"solution({A})", setup="from __main__ import solution")
        l, t = timer.autorange()
        yield (n, t / l)


def test_timeit():
    x = []
    y = []
    for case in time_test_gen():
        logger.info(case)
        print(*case, sep=",")
        x.append(case[0])
        y.append(case[1])

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":

    test_sorted(solution)
    test_timeit()

    # print("All done!")2
