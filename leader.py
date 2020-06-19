# Dominator
def solution(A):
    n = len(A)
    if not n:
        return -1
    size = 0
    for elem in A:
        if size == 0:
            size += 1
            value = elem
        else:
            if value != elem:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for elem in A:
        if (elem == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
        for idx, candidate in enumerate(A):
            if candidate == leader:
                return idx
    return leader

A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))

# EquiLeader
def solution(A):
    n = len(A)
    size = 0
    for elem in A:
        if size == 0:
            size += 1
            value = elem
        else:
            if value != elem:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= n // 2:
        # The candidate is not the leader
        return 0
    else:
        leader = candidate
    equi = 0
    leader_count_so_far = 0
    for idx, elem in enumerate(A):
        if elem == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (idx + 1) / 2 and leader_count - leader_count_so_far > (n - idx - 1) / 2:
            equi += 1
    return equi

A = [4, 3, 4, 4, 4, 2]
print(solution(A))

print(solution([4, 4, 2, 5, 3, 4, 4, 4] ))
