# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import random
'''
yet to analyse!
'''

def shell_sort(A):
    sub_list_count = len(A)//2
    while sub_list_count > 0:
        for start_position in xrange(sub_list_count):
            gap_insertion_sort(A, start_position, sub_list_count)
        print 'After increment if size %d, the list is %s' % (len(A), str(A))
        sub_list_count //= 2
    return A


def gap_insertion_sort(A, start, gap):
    for i in xrange(start+gap, len(A), gap):
        current_value = A[i]
        position = i

        while position > gap and A[position-gap] > current_value:
            A[position] = A[position-gap]
            position = position - gap
        A[position] = current_value
    return A

a_list = range(10)
random.shuffle(a_list)
print shell_sort(a_list)