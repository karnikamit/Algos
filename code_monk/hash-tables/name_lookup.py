# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

cases = int(raw_input())
register_book = {}
for _ in xrange(cases):
    roll_number, name = raw_input().split(' ')
    register_book[int(roll_number)] = name
assert len(register_book) == cases
quries = int(raw_input())

for _ in xrange(quries):
    roll_number = int(raw_input())
    print register_book[roll_number]
