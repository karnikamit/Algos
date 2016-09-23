# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

'''
Here Bucket Sort uses insertion sort
'''


def insertion_sort(a_list):
    """

    :param a_list:
    :return:
    """
    for i in xrange(1, len(a_list)):
        temp = a_list[i]
        k = i
        while k > 0 and temp < a_list[k - 1]:
            a_list[i] = a_list[k - 1]
            k -= 1
        a_list[k] = temp
