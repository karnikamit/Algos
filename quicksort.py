# -*- coding: utf-8 -*-
__author__ = "karnikamit"

'''
    Quick Sort Algorithm

    1. select a pivot value [usually the first item in the list.    (Assist with splitting the list)
    2. Partitioning begins by locating two position markers. [leftmost+1, right most]
        (purpose of partioning is to move items that are on the wrong side with respect to the pivot
        value while also converging on the split point.)
    3. Begin by incrementing leftmark until we locate a value that is greater than the pivot value
    4. Then decrement rightmark until we find a value that is less than the pivot value.
    5. Now we can exchange these two items and then repeat the process again.
    6. At the point where rightmark becomes less than leftmark, we stop.
    7. The position of rightmark is now the split point.
    8. The pivot value can be exchanged with the contents of the split point
    9. Repeat
'''


def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)
    return a_list


def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point-1)
        quick_sort_helper(a_list, split_point+1, last)
    return a_list


def partition(a_list, first, last):
    pivot = a_list[first]
    leftmark = first+1
    rightmark = last
    flag = True

    while flag:
        while leftmark <= rightmark and a_list[leftmark] < pivot:
            leftmark += 1
        while a_list[rightmark] > pivot and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            flag = False
        else:
            a_list[leftmark], a_list[rightmark] = a_list[rightmark], a_list[leftmark]
    a_list[first], a_list[rightmark] = a_list[rightmark], a_list[first]
    return rightmark


if __name__ == '__main__':
    a =  [14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
    print quick_sort(a)