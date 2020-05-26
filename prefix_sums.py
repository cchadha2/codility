# CountDiv
def solution(A, B, K):
    return (B - (A - A % K)) // K if A % K else (B - A) // K + 1
