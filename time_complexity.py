# FrogJmp

# O(n) complexity
def solution(X, Y, D):
    for i, x in enumerate(range(X, Y + 1 + D, D)):
        if x > Y:
            return i


print(solution(10, 85, 30))

# Takes too long
# print(solution(10, 1000000000, 2)) 

# O(1) complexity
def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1

print(solution(10, 85, 30))

# PermMissingElem

# O(n)
def solution(A):
    n = len(A) + 1
    expected = n * (n + 1) // 2
    return expected - sum(A)

print(solution([1]))
print(solution([]))
print(solution([2, 3, 1, 5]))

# TapeEquilibrium

# O(n)
def solution(A):
    head = A[0]
    tail = sum(A[1:])
    minimum = abs(head - tail)
    for idx in range(1, len(A) - 1):
        head += A[idx]
        tail -= A[idx]
        minimum = min(abs(head - tail), minimum)
    return minimum

print(solution([3, 1, 2, 4, 3]))

