def partition(A, l, r):
    pivot = (l + r) // 2
    x = A[pivot]
    i, j = l, r
    while i <= j:
        while A[i] < x:
            i += 1
        while A[j] > x:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return i, j


def solution(A):
    def quick_sort(left, right):
        i, j = partition(A, left, right)
        if left < j:
            quick_sort(left, j)
        if right > i:
            quick_sort(i, right)

    quick_sort(0, len(A) - 1)
    return A


if __name__ == "__main__":
    test_A = [4, 9, 2, 0, 8, 8, 7, 6, 3, 2]
    solution(test_A)
    print(test_A)

    test_B = [5, 4, 2, 8, 7, 8, 9]
    solution(test_B)
    print(test_B)
