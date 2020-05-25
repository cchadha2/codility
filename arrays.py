from collections import Counter

def solution(A):
    for x, occ in Counter(A).items():
        if occ % 2:
            return x

