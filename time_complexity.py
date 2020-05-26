# FrogJmp
def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1


# PermMissingElem
def solution(A):
    n = len(A) + 1
    expected = n * (n + 1) // 2
    return expected - sum(A)


# TapeEquilibrium
def solution(A):
    head = A[0]
    tail = sum(A[1:])
    minimum = abs(head - tail)
    for idx in range(1, len(A) - 1):
        head += A[idx]
        tail -= A[idx]
        minimum = min(abs(head - tail), minimum)
    return minimum
