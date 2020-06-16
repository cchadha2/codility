# CountDiv
def solution(A, B, K):
    return (B - (A - A % K)) // K if A % K else (B - A) // K + 1

# GenomicRangeQuery
def solution(S, P, Q):
    result = []
    for idx, _ in enumerate(P):
        slc = S[P[idx]:Q[idx] + 1]
        if 'A' in slc:
            result.append(1)
            continue
        elif 'C' in slc:
            result.append(2)
            continue
        elif 'G' in slc:
            result.append(3)
            continue
        else:
            result.append(4)
    return result

print(solution("CAGCCTA",  [2, 5, 0], [4, 5, 6]))

# MinAvgTwoSlice
def solution(A):
    min_avg_value = (A[0] + A[1]) / 2
    min_avg_pos = 0

    for index in range(0, len(A) - 2):
        # Try the next 2-element slice]
        two_slice = (A[index] + A[index + 1]) / 2
        three_slice = (A[index] + A[index + 1] + A[index + 2]) / 3
        if two_slice < min_avg_value:
            min_avg_value = two_slice
            min_avg_pos = index
        # Try the next 3-element slice
        if three_slice < min_avg_value:
            min_avg_value = three_slice
            min_avg_pos = index
    last_two_slice = (A[-1] + A[-2]) / 2
    # Try the last 2-element slice
    if last_two_slice < min_avg_value:
        min_avg_value = last_two_slice
        min_avg_pos = len(A) - 2
    return min_avg_pos

A = [4, 2, 2, 5, 1, 5, 8]
res = solution(A)
print(res)

# PassingCars
def solution(A):
    n = len(A)
    maximum = 10**9
    sums = [0] * n
    counter = 0
    scaler = 1
    start = A[0]

    sums[0] = start
    for idx in range(1, n):
        sums[idx] += sums[idx - 1] + A[idx]
        if (sums[idx] - sums[idx - 1]) == 1 and not start:
            counter += scaler * 1
        else:
            scaler += 1
        if counter > maximum:
            return -1
    return counter

A = [0, 1, 0, 1, 1]
print(solution(A))

A = [0]
print(solution(A))

A = [1]
print(solution(A))

A = [0, 0]
print(solution(A))

A = [1, 1]
print(solution(A))

A = [1, 0]
print(solution(A))
