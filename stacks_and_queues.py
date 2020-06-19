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
