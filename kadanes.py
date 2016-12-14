# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
Maximum sum sub array. O(n)
'''


def kadanes(a_list):
    max_current, max_global = a_list[0], a_list[0]
    for i in xrange(1, len(a_list)-1):
        max_current = max([a_list[i], max_current+a_list[i]])
        if max_current > max_global:
            max_global = max_current
    return max_global

print kadanes([3,3,9,9,5])