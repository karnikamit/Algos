# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
"""
Find all primes upto given number.
"""
import math


def get_primes(n):
    """

    :return: List of primes
    """
    numbers = range(2, n)
    nos_check = range(2, int(math.sqrt(n)+1))
    for i in nos_check:
        numbers = filter(lambda x: x % i != 0, numbers)
    else:
        return numbers

if __name__ == '__main__':
    print get_primes(10000)
