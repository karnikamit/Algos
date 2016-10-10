# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

'''
Given an array of n elements, find three elements in the array such that their sum is equal to given element k
'''
a_list = [1, 6, 45, 4, 10, 18]
k = 22


def three_elements(alist, K):
    """

    :param alist: array of n numbers
    :param K: value
    :return: three numbers whose sum is equal to K
    """
    alist.sort()
    # Build a dict
    table = {k: v for k, v in enumerate(alist) if v < K}
    # {0: 1, 1: 4, 2: 6, 3: 10, 4: 18}
    a_sum = 0
    for key in table:
        pass
if __name__ == '__main__':
    print three_elements(a_list, k)
