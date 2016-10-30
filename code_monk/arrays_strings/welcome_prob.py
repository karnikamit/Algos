# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

N = int(raw_input())
A = map(int, raw_input().split(' '))
B = map(int, raw_input().split(' '))
assert N == len(A) == len(B)


def add(a, b):
    return a + b
total = map(add, A, B)
for i in  total:
    print i,
