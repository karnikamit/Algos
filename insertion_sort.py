# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
* Advantages
- stable: maintains relative order of the data if the keys are same
- practically more efficient then selection and bubble sorts
- Online: Can sort the list as it receives

* Algorithm
Every repetition of insertion sort,
removes an element from the ip-data and places it in the correct position

# worst case Complexity O(n^2)
'''


def insertion_sort(a_list):
    for i in xrange(1, len(a_list)):
        temp = a_list[i]
        k = i
        while k > 0 and temp < a_list[k-1]:
            a_list[k] = a_list[k-1]
            k -= 1
        a_list[k] = temp
    return a_list
