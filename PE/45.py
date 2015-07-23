__author__ = 'karnikamit'
from time import time


def triangle(n):
    return (n*(n+1))/2


def pentagonal(n):
    return (n*(3*n-1))/2


def hexagonal(n):
    return n*(2*n-1)


t = [triangle(i) for i in xrange(2, 100000)]
p = [pentagonal(i) for i in xrange(2, 100000)]
h = [hexagonal(i) for i in xrange(2, 100000)]
start = time()
count = 0
for elem in t:
    if elem in p and elem in h:
        count += 1
        if count == 2:
            print elem, time()-start, 'seconds'
            break
