# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
https://www.hackerearth.com/codemonk-sorting/algorithm/monk-and-modulo-based-sorting/
'''


def sort_input(array, k):
    """

    :param array: list to sort
    :param k: number to take modulo with
    :return: sorted array
    """
    return sorted(array, key=lambda x: x % k)

n, k = map(int, raw_input().split(' '))
array = map(int, raw_input().split(' '))
assert len(array) == n
sorted_array = sort_input(array, k)
for i in sorted_array:
    print i,
