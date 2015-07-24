__author__ = 'karnikamit'
from is_prime import is_prime
from time import time
from factors import get_factors


def triangle_numbers():
    flag = True
    n = 0
    t_no = 0
    while flag:
        n += 1
        t_no += n
        if is_prime(t_no):
            continue
        if len(get_factors(t_no)) > 500:
            return t_no

if __author__ == 'karnikamit':
    start = time()
    print triangle_numbers(), time()-start
