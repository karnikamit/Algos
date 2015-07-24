__author__ = 'karnikamit'
from is_prime import is_prime
from time import time


def get_factors(n):
    return len([i for i in xrange(1, n+1) if n % i == 0])


def triangle_numbers():
    flag = True
    n = 0
    t_no = 0
    while flag:
        n += 1
        t_no += n
        if is_prime(t_no):
            continue
        if get_factors(t_no) > 500:
            return t_no

if __author__ == 'karnikamit':
    start = time()
    print triangle_numbers(), time()-start
