# FrogRiverOne
def solution(X, A):
    n = len(A)
    frog, covered = 0, [False] * (X)
    for idx in range(n):
        covered[A[idx] - 1] = True
        while covered[frog]:
            frog += 1
            if frog == X:
                return idx
    return -1


# MaxCounters
def solution(N, A):
    count = [0] * N
    max_count = 0
    last_max = False
    for val in A:
        if val == N + 1 and last_max == False:
            count = [max_count] * N
            last_max = True
            continue
        if val <= N:
            count[val - 1] += 1
            max_count = max(count[val - 1], max_count)
            last_max = False
    return count


# MissingInteger
def solution(A):
    filtered = [elem for elem in A if elem > 0]
    if not filtered:
        return 1
    count = [False] * 1000000
    for elem in filtered:
        if count[elem - 1]:
            continue
        count[elem - 1] = True
    return count.index(False) + 1


# PermCheck
def solution(A):
    maximum = max(A)
    if len(A) < maximum:
        return 0
    count = [False] * maximum
    for elem in A:
        if count[elem - 1]:
            return 0
        count[elem - 1] = True
    return 1 if all(count[:maximum]) else 0
