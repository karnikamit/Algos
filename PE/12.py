# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import itertools
from math import sqrt
from time import clock


def get_divs(n):
    divs = 0
    for i in xrange(1, int(sqrt(n))+1):
        if n % i == 0:
            divs += 2
    if sqrt(n)**2 == n:
        divs -= 1
    return divs


def get_tri_numbers():
    num = 0
    for i in itertools.count(1):
        num += i
        if get_divs(num) > 500:
            return num


if __name__ == '__main__':
    start = clock()
    print get_tri_numbers(), 'runTime:', clock()-start
