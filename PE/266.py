__author__ = 'karnikamit'
from is_prime import is_prime
from numpy import prod
from math import sqrt
from time import time


def get_prod_prime(n):
    i = 0
    primes = []
    while i < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return prod(primes)     # 1456955400340837138 for 190


def get_psr(n):
    psr = 0
    check = sqrt(n)
    for i in xrange(1, int(check+1)):
        if n % i == 0:
            if i > psr and i < check:
                psr = i
    return psr
# print get_psr(3102)   # 47

def main(limit):
    prime_prod = get_prod_prime(limit)
    print 'working now!'
    return get_psr(prime_prod) % 10**16

start = time()
print main(190)
print time()-start, 'seconds'