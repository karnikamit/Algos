# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def can_be(s):
    """

    :param s: string
    :return: int no of words that can be generated.
    """
    count = 0
    temp = {'r': [], 'u': [], 'b': [], 'y': []}     # maximum number of ruby(ies)
    for i in s:
        try:
            temp[i].append(i)
        except KeyError:
            pass
    if all([True if temp.get(k) else False for k in temp]):
        min_char = min(temp, key=lambda x: len(temp[x]))
        count = len(temp[min_char])
    return count

cases = int(raw_input())
for _ in xrange(cases):
    ip_string = raw_input()
    print can_be(ip_string)
