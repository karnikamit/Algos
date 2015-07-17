__author__ = 'CYBORG'
from math import sqrt
from time import time


def is_prime(num):
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

start = time()
s = 0
for i in range(2, 2*(10**6)):
    if is_prime(i):
        s += i
print(s, "time taken", time()-start, "seconds")

