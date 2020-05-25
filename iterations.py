def solution(N):
    def counter(n):
        count = 0
        preceeding_one = False
        for x in reversed(bin(n).lstrip('0b')):
            x = int(x)
            if x == 1:
                count = 0
                preceeding_one = True
                yield count
            if preceeding_one and x == 0:
                count += 1
                yield count
        yield count
    return(max(counter(N)))

