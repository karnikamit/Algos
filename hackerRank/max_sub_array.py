# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def find_max_sub_array_sum(array, mod_operand):
    current, result = array[0], 0
    for i in xrange(1, len(array)-1):
        current = max(array[i], current+array[i])
        mod_sum = current % mod_operand
        if mod_sum > result:
            result = mod_sum
    return result

print find_max_sub_array_sum([3,3,9,9,5], 7)
