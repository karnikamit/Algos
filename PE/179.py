__author__ = 'karnikamit'

# Consecutive positive divisors
from time import time


def get_div(n):
    divs = [i for i in xrange(1, n+1) if n % i == 0]
    return divs


def find_int():
    prev_divs = []
    result = []
    for i in xrange(1, 10**4):
        curr_divs = get_div(i)
        if len(curr_divs) == len(prev_divs):
            result.append(i-1)
            result.append(i)
        prev_divs = curr_divs
    return len(result)


start = time()
print find_int(), time()-start, 'seconds'