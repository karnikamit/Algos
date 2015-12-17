__author__ = "karnikamit"


def is_perfect_number(n):
    j = 0
    result = False
    for i in xrange(1, int(n**1/2)+1):
        if n % i == 0:
            j += i
    if j == n:
        result = True
    return result
