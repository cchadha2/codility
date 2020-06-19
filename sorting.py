# Distinct
def solution(A):
    n = len(A)
    if not n:
        return 0
    A.sort()
    result = 1
    for x in range(1, n):
        if A[x] != A[x - 1]:
            result += 1
    return result

# MaxProductOfThree
def solution(A):
    A.sort()
    return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

print(solution([-5, 5, -5, 4]))

# NumberOfDiscIntersections
def solution(A):
    circle_endpoints = []
    for i, a in enumerate(A):
        circle_endpoints += [(i-a, True), (i+a, False)]
    circle_endpoints.sort(key=lambda x: (x[0], not x[1]))

    intersections, active_circles = 0, 0

    for _, is_beginning in circle_endpoints:
        if is_beginning:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1
        if intersections > 10E6:
            return -1

    return intersections


A = [1, 5, 2, 1, 4, 0]

print(solution(A))

# Triangle
def solution(A):
    A.sort()
    n = len(A)
    for triplet in range(n, -1, -1):
        try:
            a, b, c = A[triplet - 3 : triplet]
        except ValueError:
            return 0
        if a + b > c and a + c > b and b + c > a:
            return 1
    else:
        return 0

A = [10, 2, 5, 1, 8, 20]

print(solution(A))

print(solution([10, 50, 5, 1]))
