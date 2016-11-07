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
    numbers = range(3, n)
    nos_check = range(2, int(math.sqrt(n)+1))
    for i in nos_check:
        numbers = filter(lambda x: x % i, numbers)
    else:
        numbers.insert(0, 2)    # TODO Fix this!
        return numbers

if __name__ == '__main__':
    print get_primes(14)
