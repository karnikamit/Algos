# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from itertools import permutations


def find_pattern(s, p):
    """

    :param s: string
    :param p: pattern
    :return: YES if pattern is present else NO
    """
    for permutation in get_permutations(p):
        string_permutation = ''.join(permutation)
        if string_permutation in s:
            return 'YES'
    else:
        return 'NO'


def get_permutations(p):
    """
    permutation generator
    :param p: pattern
    :yield: possible permuted pattern.
    """
    pattern_permutations = permutations(p)
    for permutation in pattern_permutations:
        yield permutation


cases = int(raw_input())
for _ in xrange(cases):
    pattern = raw_input()
    ip_string = raw_input()
    print find_pattern(ip_string, pattern)
