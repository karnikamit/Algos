__author__ = 'CYBORG'
# 10001st prime
from is_prime import is_prime
from time import time


def main(n):
    i = 1
    num = 2
    nth = n
    while i <= nth:
        if is_prime(num):
            if i == nth:
                return num
            i += 1
        num += 1

start = time()
print(main(10001), "time taken", time()-start, "seconds")
