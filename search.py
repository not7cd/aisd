# pythonic?
def solution(A, x):
    for i, elt in enumerate(A):
        if x == A:
            return i
    else:
        return None


# basic
def alt_solution(A, x):
    i = 0
    N = len(A)
    while True:
        if A[i] == x or i == N:
            break
        i += 1

    if A[i] == x:
        return i
    else:
        return None
