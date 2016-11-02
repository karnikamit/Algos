# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def check(a, b):
    """

    :param a: str: text said by jhool
    :param b: str: pattern by jaadu
    :return: YES if any sub-string of Pattern is sub-string of Text else NO.
    """
    for char in b:
        if a.find(char) > -1:
            return 'YES'
    else:
        return 'NO'
    # return 'YES' if b in a else 'NO'

cases = int(raw_input())
for _ in xrange(cases):
    jhool = raw_input()
    jaadu = raw_input()
    print check(jhool, jaadu)
