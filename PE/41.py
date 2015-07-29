__author__ = 'karnikamit'
from is_prime import is_prime
from time import time


def get_pandigital_prime(n):
    nums = range(1, n+1)
    start = int('1'*n)
    fin = int('9'*n)+1
    p = 0
    for i in xrange(start, fin):
        i = str(i)
        listA = list(i)
        if all(str(item) in listA for item in nums):
            i = int(i)
            if is_prime(i):
                if i > p:
                    p = i
    return p

start = time()
def euler():
    pand_prime = 0
    for i in xrange(1, 8):
        num = get_pandigital_prime(i)
        if num > pand_prime:
            pand_prime = num
    return pand_prime

print euler(), time()-start, 'seconds'
# 7652413 13.6643049717 seconds