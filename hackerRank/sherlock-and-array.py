# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
determine if there exists an element in the array such that the sum of the elements on its left
is equal to the sum of the elements on its right. If there are no elements to the left/right,
then the sum is considered to be zero.
'''
# TODO Timeout Error! fix this


def find_number(a_list):
    for i in xrange(len(a_list)):
        left = a_list[:i]
        right = a_list[i+1:]
        if sum(left) == sum(right):
            return 'YES'
    else:
        return 'NO'
