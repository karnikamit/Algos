# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
* Advantages
- Easy to implement
- In place sort (requires no additional sapce)
- Best case complexity O(n)
* Disadvantages
- Worst case complexity O(n^2)

* Algorithm
. find the min value in the list
. swap it with the vale in the current position
. repeat this process for all elements until entire array is sorted
'''


def selection_sort(a_list):
    """

    :param a_list: array of elements
    :return: sorted array by selection sort
    """
    for i in xrange(len(a_list)):
        least = a_list[i]
        for k in xrange(i + 1, len(a_list)):
            if a_list[k] < least:
                least = a_list[k]
                a_list[i], a_list[k] = a_list[k], a_list[i]  # swap the least value with element in current position
    return a_list

