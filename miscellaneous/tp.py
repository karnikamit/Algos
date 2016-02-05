# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def rec_sum(a_list):
    if len(a_list) == 1:
        return a_list[0]
    n = a_list.pop()
    return n+rec_sum(a_list)


def sum_n(a_list):
    s = 0
    while a_list:
        s += a_list.pop()
    return s


def for_sum(a_list):
    s = 0
    if a_list:
        for i in a_list:
            s += i
    return s

if __name__ == '__main__':
    print rec_sum(range(5))
    print sum_n(range(5))
    print for_sum(range(5))
    print sum([i for i in range(5)])