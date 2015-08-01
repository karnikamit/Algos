__author__ = 'karnikamit'
'''
Given an array of integers, move all the zeros to the end of an array
'''


def move_zeros(a_list):
    i = j = 0
    while i < len(a_list)-1:
        if a_list[i] != 0:
            a_list[j] = a_list[i]
            j += 1
        i += 1
    while j <= len(a_list)-1:
        a_list[j] = 0
        j += 1
    return a_list
