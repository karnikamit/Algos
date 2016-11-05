# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from itertools import permutations

# TODO Optimize the code, getting time exceed!


def find_pattern(s, p):
    """

    :param s: string
    :param p: pattern
    :return: YES if pattern is present else NO
    """
    permu_dict = {}
    for i in permutations(p):   # getting all possible permutations, converting them to string and creating a dict
        p_string = ''.join(i)
        permu_dict[p_string] = p_string
    len_permu = len(p)
    for i in xrange(len(s)):    # checking every substring with length of pattern
        string_slice = s[i: len_permu]
        if permu_dict.get(string_slice):
            return 'YES'
        len_permu += 1
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
# print find_pattern('imredoc', 'code')
