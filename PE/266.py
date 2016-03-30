# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from is_prime import is_prime
from math import sqrt, ceil
from time import time
import itertools


def get_prod_primes(n):
    return reduce(lambda x, y: x*y, [i for i in xrange(1, n) if is_prime(i)])

# TEST

# def get_raw_psr(n):
#     check = sqrt(n)
#     divisor = [i for i in xrange(1, int(check+1)) if n % i == 0][-1]
#     return divisor
# print get_raw_psr(3102)
# exit(0)


def get_psr(num):
    print 'getting divisors for %d' % num
    n, i = sqrt(num), 1
    divs = 0
    while i < n:
        if num % i == 0:
            divs = i
        i += 1
    return divs


def euler(limit):
    prime_prod = get_prod_primes(limit)
    return get_psr(prime_prod) % 10**16

if __name__ == '__main__':
    start = time()
    print euler(50)
    print time()-start, 'seconds'
