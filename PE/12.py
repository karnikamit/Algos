__author__ = 'karnikamit'
from is_prime import is_prime

def get_factors(n):
    factors = []
    for i in xrange(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


def triangle_numbers():
    flag = True
    n = 0
    while flag:
        n += 1
        if is_prime(n):
            continue
        elif len(get_factors(n)) > 5:
            return n

if __author__ == 'karnikamit':
    print triangle_numbers()