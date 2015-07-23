__author__ = 'karnikamit'
from is_prime import is_prime


def get_primes(n):
    for i in xrange(2, n+1):
        if is_prime(i):
            yield i


def find_con_prime(n):
    low = 2
    num = 0
    for i in get_primes(n):
        num += i
        if is_prime(num):
            if num < n:
                low = num
    return low
print find_con_prime(100)
