# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
 Mishki will be provided with an integer array A of size
    N and an integer K ,
 where she needs to rotate the array in the right direction by K steps and then print the resultant array.
'''
cases = int(raw_input())
for _ in xrange(cases):
    N, K = map(int, (raw_input().split(' ')))
    ip_array = raw_input().split(' ')
    array = map(int, ip_array)
    for rotate in xrange(K):
        last_element = array.pop()
        array.insert(0, last_element)
    else:
        for i in array:
            print i,
        else:
            print
