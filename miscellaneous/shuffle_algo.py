__author__ = 'karnikamit'
from random import choice

def shuffle_array(a_list):
    n = len(a_list)
    i = 0
    while i < n:
        j = choice(a_list)
        try:
            a_list[i], a_list[a_list.index(j)] = j, a_list[i]
        except IndexError:
            pass
        i += 1
    return a_list

a = range(10)
print 'ori', a
print shuffle_array(a)