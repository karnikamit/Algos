# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from is_prime import is_prime
import time


def get_prime(n):
    j = 0
    for i in (k for k in xrange(n**2) if is_prime(k)):
        if j == n:
            return i
        j += 1


def euler(pN, check):
    r = ((pN - 1)**n + (pN + 1)**n) % pN**2
    response = True
    if r > check:
        response = False
    return response

if __name__ == '__main__':
    start = time.time()
    n = 7037
    flag = True
    while flag:
        p = get_prime(n)
        flag = euler(p, 10**10)
        if not flag:
            print 'prime you are looking for is %d and appears at %d' % (p, n)
        n += 1
    print 'time took:', time.time() - start
