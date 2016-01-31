# -*- coding: utf-8 -*-
__author__ = "karnikamit"

# This is algorithm is for sorted list only.


def find_missing_number(a_list):
    """

    :param a_list: list of numbers
    :return: missing number from the list
    """
    a_list.sort()
    a_dict = dict()
    for i in xrange(len(a_list)):
        a_dict[i] = a_list[i]

    missing_number = None

    for key in a_dict:
        if key <= (len(a_list)-1) - 1:
            if a_dict[key+1] - a_dict[key] != 1:
                missing_number = a_dict[key+1]-1
    return missing_number

if __name__ == '__main__':
    print find_missing_number([-4, -2, -1])
