from collections import Counter

# CyclicRotation
def solution(A, K):
    if not A:
        return A
    for _ in range(K):
        A.insert(0, A.pop())
    return A

# OddOccurerencesInArray 
def solution(A):
    for x, occ in Counter(A).items():
        if occ % 2:
            return x

