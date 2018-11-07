import sys
import logging
import timeit
import random
from straight_selection import solution

import matplotlib.pyplot as plt

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_sorted():
    A = [9, 4, 2, 5, 8, 7, 8]
    A = solution(A)
    assert all(A[i] <= A[i + 1] for i in range(len(A) - 1))


def time_test_gen():
    for n in range(10, 300, 10):
        A = [random.random() for _ in range(n)]
        timer = timeit.Timer(
            f"solution({A})", setup="from __main__ import solution"
        )

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
    test_sorted()
    test_timeit()

    # print("All done!")
