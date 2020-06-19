# Brackets
def solution(S):
    if not S:
        return 1
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for elem in S:
        if elem in brackets:
            stack.append(elem)
        if elem in brackets.values():
            if stack:
                if elem == brackets[stack.pop()]:
                    continue
                else:
                    return 0
            else:
                return 0
    return 0 if stack else 1

S = "{[()()]}"
print(solution(S))

S = "([)()]"
print(solution(S))

S = "{{(([[["
print(solution(S))

S = "]]}}))"
print(solution(S))

# Fish
def solution(A, B):
    alive = [0]
    for fish, size in enumerate(A[1:], 1):
        print(f"fish currently alive: {alive}")
        direction = B[fish]
        while alive:
            prev_size, prev_direction = A[alive[-1]], B[alive[-1]]
            if prev_direction > direction:
                if A[fish] < prev_size:
                    # Get eaten by previous fish.
                    print(f"{fish} is being eaten by {alive[-1]}")
                    break
                else:
                    # Eat the previous fish.
                    dead = alive.pop()
                    print(f"{fish} is eating {dead}")
                    continue
            if prev_direction <= direction:
                print(f"{fish} does not meet {alive[-1]}")
                alive.append(fish)
                # prev_size, prev_direction = size, direction
                break
        else:
            alive.append(fish)
    print(f"fish left alive: {alive}")
    return len(alive)


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))

A = [4, 3, 2, 1, 5]
B = [1, 0, 0, 0, 0]
print(solution(A, B))

A = [0, 1]
B = [1, 1]
print(solution(A, B))

A = [5, 4, 1, 1, 2, 8, 5]
B = [0, 1, 1, 1, 0, 1, 0]
print(solution(A, B))

# Nesting
def solution(S):
    if not S:
        return 1
    stack = []
    brackets = {"(": ")"}
    for elem in S:
        if elem in brackets:
            stack.append(elem)
        if elem in brackets.values():
            if stack:
                if elem == brackets[stack.pop()]:
                    continue
                else:
                    return 0
            else:
                return 0
    return 0 if stack else 1

S = "(()(())())"
print(solution(S))

S = "())"
print(solution(S))

# StoneWall
def solution(H):
    stack = []
    num_blocks = 0

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()
        if stack and stack[-1] == height:
            continue
        else:
            stack.append(height)
            num_blocks += 1
    return num_blocks

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))


H = [2, 3, 2, 1]
print(solution(H))

H = [1, 2, 3, 3, 2, 1]
print(solution(H))

H = [1, 1, 1]
print(solution(H))
