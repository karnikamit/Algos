__author__ = 'karnikamit'
from itertools import permutations
from time import time


def is_prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1


def find_circular_primes(num):
    circular_primes = 0
    for i in xrange(2, num):
        if is_prime(i):
            i = str(i)
            count = 0
            count_num = 0
            for e in permutations(i):
                count += 1
                n = ','.join(e)
                n = int(n.replace(',', ''))
                if is_prime(n):
                    count_num += 1
            if count == count_num:
                circular_primes += 1
    return circular_primes


start = time()
print find_circular_primes(100000), time()-start, "seconds"
