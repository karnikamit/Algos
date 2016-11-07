# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

fib_string = ''
for i in xrange(11, 20):
    fib_value = fib(i)
    fib_string += str(bin(fib_value)[2:])
print fib_string

'''
1011001100100001110100110111100110011000101111011011110001111011010000110001000001010101
'''