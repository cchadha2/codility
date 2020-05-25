from time import perf_counter


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
    
def count_gap(x):
    """
        Perform Find the longest sequence of zeros between ones "gap" in binary representation of an integer

        Parameters
        ----------
        x : int
            input integer value

        Returns
        ----------
        max_gap : int
            the maximum gap length

    """
    try:
        # Convert int to binary
        b = "{0:b}".format(x)
        # Iterate from right to lift 
        # Start detecting gaps after fist "one"
        for i,j in enumerate(b[::-1]):
            if int(j) == 1:
                max_gap = max([len(i) for i in b[::-1][i:].split('1') if i])
                break
    except ValueError:
        print("Oops! no gap found")
        max_gap = 0
    return max_gap

print(bin(32))
start = perf_counter()
print(solution(32))
end = perf_counter() - start
print(end)
start = perf_counter()
print(count_gap(32))
end = perf_counter() - start
print(end)

print(bin(9))
start = perf_counter()
print(solution(9))
end = perf_counter() - start
print(end)
start = perf_counter()
print(count_gap(9))
end = perf_counter() - start
print(end)

print(bin(1041))
start = perf_counter()
print(solution(1041))
end = perf_counter() - start
print(end)
start = perf_counter()
print(count_gap(1041))
end = perf_counter() - start
print(end)

print(bin(2_414_532_323))
start = perf_counter()
print(solution(2_414_532_323))
end = perf_counter() - start
print(end)
start = perf_counter()
print(count_gap(2_414_532_323))
end = perf_counter() - start
print(end)

n = 6_245_232_321_242_414_532_323
print(bin(n))
start = perf_counter()
print(solution(n))
end = perf_counter() - start
print(end)
start = perf_counter()
print(count_gap(n))
end = perf_counter() - start
print(end)


print(bin(529))
print(solution(529))
print(count_gap(529))

print(bin(20))
print(solution(20))
print(count_gap(20))

print(bin(0))
print(solution(0))
print(count_gap(0))
