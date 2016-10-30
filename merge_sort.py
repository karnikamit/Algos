# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


'''
worst case: O(nlog(n))
space complexcity: O(n)
* Access data in sequential manner.
* Insensitive to initial order of ip list
* Does't need stack.
'''


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list)/2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1


if __name__ == '__main__':
    a = [32, 45, 21, 23, 67, 90, 42]
    print 'Before: {}'.format(a)
    merge_sort(a)
    print 'After: {}'.format(a)


