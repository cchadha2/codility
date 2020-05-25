def solution(A, K):
    if not A:
        return A
    for _ in range(K):
        A.insert(0, A.pop())
    return(A)

a = [9, 3, 9, 3, 9, 7, 9, 5, 5, 4, 4, 2, 2, 1, 1, 8, 8, 10, 10, 12, 12, 13, 13, 1, 1]

def solution(A):
    for x in A:
        if A.count(x) % 2:
            return x 
 
print(solution(a))

from collections import Counter

def solution(A):
    for x, occ in Counter(A).items():
        if occ % 2:
            return x
    
print(solution(a))