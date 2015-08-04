__author__ = 'karnikamit'
from is_prime import is_prime


def get_primes(n):
    primes = []
    for i in xrange(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


print get_primes(100)