def solution(A):
    for i, elt in enumerate(A):
        k = i
        for j in range(i, len(A)):
            if A[j] < A[k]:
                k = j
        A[k], A[i] = A[i], A[k]
    return A


if __name__ == "__main__":
    test_A = [9, 4, 2, 5, 8, 7, 8]

    l = solution(test_A)
    assert False #all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    print(l)
