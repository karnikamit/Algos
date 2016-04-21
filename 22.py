# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from string import ascii_uppercase
from time import clock


def get_names(filename):
    with open(filename) as f:
        names = f.read().split(',')
        names.sort()
        return names


def get_total_score(names_list):
    return sum(i*score(x) for i, x in enumerate(names_list, 1))


def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

if __name__ == '__main__':
    start = clock()
    name_list = get_names('p022_names.txt')
    print get_total_score(name_list)
    print 'runTime:', clock()-start, 's'
