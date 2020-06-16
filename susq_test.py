def solution(A):
    total = sum(A)
    if total % 3:
        return "impossible"
    equal = total // 3
    S = ["R"] * len(A) # Default value.
    for idx, elem in enumerate(A):
        if elem == equal:
            # If sole value then default to "B".
            S[idx] = "G"
        for remaining_idx, remaining_elem in enumerate(A):
            if remaining_idx == idx:
                continue
            if elem + remaining_elem == equal:
                S[idx], S[remaining_idx] = "B", "B"
                continue
    return S

A = [3, 7, 2, 5, 4]
print(solution(A))

from itertools import combinations

def solution(A):
    total = sum(A)
    n = len(A)
    if total % 3:
        return "impossible"
    if n <= 3 and A[0] != A[-1]:
        return "impossible"
    equal = total // 3
    coloring = ["R"] * n
    result = [seq for i in range(len(A), 0, -1) for seq in combinations(A, i) if sum(seq) == equal]
    print(result)
    for counter, combination in enumerate(result):
        for elem in combination:
            if counter == 0:
                coloring[A.index(elem)] = "R"
            elif counter == 1:
                coloring[A.index(elem)] = "G"
            elif counter == 2:
                coloring[A.index(elem)] = "B"
    print(coloring)
    return "".join(coloring)


    #for combination, elem in zip(colours, result):
    #    combination = combination*len(elem)
   #     print(combination)
    # result = [x * len(seq) for x in ["R", "G", "B"] for seq in result]
    return result

#for x in solution(A):
#    print(x)
print(solution(A))
print(solution([3, 6, 9]))
print(solution([2, 2, 2]))
print(solution([1, 1]))
print(solution([1, 2, 3, 5, 17, 19, 205]))

# StackMachine
def solution(S):

    def add(x, y):
        return x + y

    def multiply(x, y):
        return x * y

    stack = []
    numbers = {str(x): x for x in range(0, 4096)}
    operators = {"+": add, "*": multiply}
    
    result = 0
    next_num = 0
    for elem in S:
        if elem in numbers:
            stack.append(elem)
        elif elem in operators:
            if stack:
                try:
                    x, y = stack.pop(), stack.pop()
                except IndexError: # Not enough elements in stack.
                    return -1
                result = operators[elem](numbers[x], numbers[y])
                if result > 4095:
                    return -1
                stack.append(str(result))
            else:
                return -1
    if not stack:
        return -1
    return numbers[stack.pop()]

print(solution("13+62*7+*"))
print(solution(""))
print(solution("11++"))
print(solution("++"))
print(solution("145+5643*9*89*8*9*9"))





