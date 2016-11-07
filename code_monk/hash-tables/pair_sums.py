# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/
'''
N, K = map(int, raw_input().split(' '))
array = map(int, raw_input().split(' '))
assert len(array) == N


def pair_sum(array, k):
    """

    :param array: array of integers
    :param k: sum required
    :return: pair of integers
    """
    for pivot in array:
        p_index = array.index(pivot)
        for elem in array[p_index:]:
            if pivot + elem == k:
                return 'Yes'
    else:
        return 'No'
print pair_sum(array, K)
