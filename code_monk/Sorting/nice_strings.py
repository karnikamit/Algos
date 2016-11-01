# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def get_niceness(i, string):
    """

    :param i: index for A
    :param string: lower case English alphabet
    :return:
    """
    global A
    temp = A[1:i]
    element_ord = ord(string)
    values = filter(lambda x: ord(x) < element_ord, temp)
    return len(values)

A = ['']
N = int(raw_input())
count = 0
for _ in xrange(N):
    count += 1
    ip_string = raw_input()
    A.append(ip_string)
    print get_niceness(count, ip_string)
