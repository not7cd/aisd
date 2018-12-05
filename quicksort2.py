from quicksort import partition
from straight_selection import solution as straight_selection


def solution(A):
    m = 1
    left = 0
    right = len(A) - 1
    s = [(0, 0)]
    while left < right:
        i, j = partition(A, left, right)
        _jl = j - left
        _ri = right - i
        if _jl < m and _ri < m:
            left, right = s.pop()
        elif _jl < m and _ri >= m:
            left = i
        elif _jl >= m and _ri < m:
            right = j
        elif _jl >= m and _ri >= m:
            if _jl >= _ri:
                s.append((left, j))
                left = i
            else:
                s.append((i, right))
                right = j
    return A


if __name__ == "__main__":
    test_A = [4, 9, 2, 0, 8, 8, 7, 6, 3, 2, 2]
    solution(test_A)
    print(test_A)

    test_B = [9, 4, 2, 5, 8, 7, 8]
    solution(test_B)
    print(test_B)
