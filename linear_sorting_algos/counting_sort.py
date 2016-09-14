# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
Time complexity: O(n)

Assumption: Each value in the list is an integer in the range 0 - k
'''


def counting_sort(a_list, k):
    """

    :param a_list: Elements to sort
    :param k: Max of Elements in the given list
    :return: sorted list
    """
    b_list = [0 for _ in a_list]
    c_list = [0 for _ in xrange(k+1)]

    for j in a_list:
        c_list[j] += 1

    for i in xrange(1, k+1):
        c_list[i] += c_list[i - 1]

    for m in xrange(len(a_list)-1, -1, -1):
        tmp = a_list[m]
        tmp2 = c_list[tmp] - 1
        b_list[tmp2] = tmp
        c_list[tmp] -= 1
    return b_list

if __name__ == '__main__':
    a = [23, 54, 21, 56, 90, 3]
    print counting_sort(a, 100)
