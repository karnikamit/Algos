# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from get_primes import get_primes
from is_prime import is_prime
from time import clock



def trunc_left(k):
    should_app = False
    k_str = str(k)
    while len(k_str) != 1:
        k_str = k_str[1:]
        if is_prime(int(k_str)):
            continue
        else:
            break
    else:
        should_app = True

    return should_app


def trubnc_right(j):
    should_app = False
    j_str = str(j)
    while len(j_str) != 1:
        j_str = j_str[:-1]
        if is_prime(int(j_str)):
            continue
        else:
            break
    else:
        should_app = True
    return should_app

def truncatable_primes(n):
    primes = get_primes(n)
    truncatable = 0
    k = 0
    for i in primes:
        if k == 11:
            return truncatable
        prime_string1 = str(i)
        prime_string2 = str(i)
        if len(str(i)) > 1:
            if trunc_left(prime_string1) and trubnc_right(prime_string2):
                truncatable += i
                k += 1


if __name__ == '__main__':
    start = clock()
    print truncatable_primes(800000)
    print 'RunTime:',clock()-start, 's'
