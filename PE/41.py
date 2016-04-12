# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
from is_prime import is_prime


def get_primes(n):
    if n > 3:
        return (i for i in xrange(3, n) if is_prime(i))


def check_for_pandigital(prime_str, digs):
    resp = False
    for j in prime_str:
        if j in digs:
            digs.remove(j)
        else:
            break
    else:
        resp = True
    return resp


def get_pandigital_primes(n):
    pan_digital_prime = 3
    for i in get_primes(n):
        p_len = len(str(i))
        digs = [str(k) for k in xrange(1, p_len+1)]
        prime_string = str(i)
        if check_for_pandigital(prime_string, digs):
            pan_digital_prime = i
    return pan_digital_prime

print 'Largest pandigital found: %d' % get_pandigital_primes(8000000)
