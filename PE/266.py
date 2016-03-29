# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from is_prime import is_prime
from numpy import prod
from math import sqrt
from time import time
import itertools


def get_prod_primes(n):
    return reduce(lambda x, y: x*y, [i for i in xrange(1, n) if is_prime(i)])

# TEST
# def get_raw_psr(n):
#     check = sqrt(n)
#     divisors = [i for i in xrange(1, int(check+1)) if n % i == 0]
#     return max(divisors)
#
# print get_raw_psr(3102)


def get_psr(n):
    check = sqrt(n)
    psr_list = []
    for i in itertools.count(1):
        if i > int(check):
            break
        if n % i == 0:
            psr_list.append(i)
    return max(psr_list)


def main(limit):
    prime_prod = get_prod_primes(limit)
    return get_psr(prime_prod) % 10**16

if __name__ == '__main__':
    start = time()
    print main(190)
    print time()-start, 'seconds'