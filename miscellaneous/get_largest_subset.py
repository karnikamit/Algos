# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
given an array, find the largest good subset.
A good subset is when the integers in the selected subset, divides every other number.
 ie array[i]%array[j] == 0 or array[j]%array[i] == 0
'''
size_of_array = input()
array = []
for i in xrange(size_of_array):
    array.append(input())


def mod(a, b):
    if a > b:
        return a % b
    else:
        return b % a


def get_sub_lists(alist):
    sub_sets = []
    for i in xrange(len(alist)):
        pivot_value = alist[i]
        temp_array = alist[i+1:]
        sub_list = get_sub_set(pivot_value, temp_array)
        if sub_list:
            sub_sets.append((sub_list, len(sub_list)))
    return sub_sets


def get_sub_set(pivot, a_list):
    if not a_list:
        return []
    sub_list = [pivot]
    for i in a_list:
        if mod(i, pivot) == 0:
            sub_list.append(i)
        else:
            return sub_list
sub_lists = get_sub_lists([4, 8, 2, 3])	 # array of tupples==[([], len([])),...]
if sub_lists:
    print len(sorted(sub_lists, key=lambda x: x[1]).pop()[0])
else:
    print None
