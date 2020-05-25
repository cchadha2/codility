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

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(6, [1, 2]))
print(solution(0, []))
print(solution(2, [2,2,2,2]))
print(solution(3, [1, 3, 1, 3, 2, 1, 3]))

# MaxCounters
def solution(N, A):
    count = [0] * N
    max_count = 0
    for val in A:
        if val == N + 1:
            count = [max_count] * N
            continue
        count[val - 1] += 1
        max_count = max(count[val - 1], max_count)
    return count

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
print(solution(1, []))
print(solution(3, [1, 2]))
print(solution(5, [2, 2]))
