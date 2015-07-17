__author__ = 'CYBORG'
def proper_divisors(n):
    i = 1
    j = []
    while i < n:
        if n % i == 0:
            j.append(i)
        i += 1
    return j
