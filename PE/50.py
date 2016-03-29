# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from is_prime import is_prime
import time


def main(n):
    primes = [i for i in xrange(n) if is_prime(i)]
    chain = []
    for start in xrange(10):  # WHY?
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > n:
                break
            i += 1
            if is_prime(total):
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    return sum(chain)
    # while primes:
    #     p = sum(primes)
    #     if p < n:
    #         if is_prime(p):
    #             return 'sum: %d' % p
    #     primes.pop()
    # return -1
if __name__ == '__main__':
    start = time.time()
    print main(1000000)
    print 'time took:', time.time()-start


