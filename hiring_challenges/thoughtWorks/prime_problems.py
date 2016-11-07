# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
import math


def get_primes(n):
    """

    :return: List of primes
    """
    numbers = range(1, n)
    nos_check = range(2, int(math.sqrt(n)+1))
    for i in nos_check:
        numbers = filter(lambda x: x % i, numbers)
    else:
        numbers.insert(0, 2)    # TODO Fix this!
        return numbers


def solve_prime_problems(n, problems_list):
    """

    :param n: no of problems
    :param problems_list: array of problem points
    :return: max problems that can be solved to get max points
    """
    problems_list.insert(0, None)
    prime_porbs = get_primes(n)
    max_points = 0
    for i in xrange(1, len(prime_porbs)+1):
        max_points += problems_list[i]
    return max_points

# N = int(raw_input())
# probs = map(int, raw_input().split(' '))
# print solve_prime_problems(N, probs)
print get_primes(10)