__author__ = 'CYBORG'
from time import time
from is_prime import is_prime


def get_prime_factors(n):
    fac = []
    i = 1
    while i < n:
        if n % i == 0 and is_prime(i):
            fac.append(i)
        i += 1
    return fac


start = time()
print(get_prime_factors(600851475143).pop(), "runtime", time()-start)
