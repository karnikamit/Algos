# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import math


def magic_numbers(n, l, r):
    """

    :param n: int range of primes
    :param l: int starting range of magic numbers
    :param r: int ending range of magic numbers
    :return: total number of magic numbers.
    """
    magic_number_count = 0
    primes = get_primes(n+1)
    for number in xrange(l, r+1):
        for prime in primes:
            if not number % prime:
                magic_number_count += 1
                break
    return magic_number_count


def get_primes(n):
    """
    :return: List of primes
    """
    numbers = xrange(3, n)
    nos_check = xrange(2, int(math.sqrt(n)+1))
    for i in nos_check:
        numbers = filter(lambda x: x % i, numbers)
    else:
        numbers.insert(0, 2)    # TODO Fix this!
        return numbers

# cases = int(raw_input())
# for _ in xrange(cases):
#     N, L, R = map(int, raw_input().split(' '))
#     print magic_numbers(N, L, R)

print magic_numbers(5, 1, 10)