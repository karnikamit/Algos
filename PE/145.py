__author__ = 'karnikamit'


def is_odd(n):
    if n > 0:
        if n % 2 == 0:
            return False
        else:
            return True
    return False


def get_num(n):
    for num in xrange(11, n+1):
        yield num


def check_num(n):
    n = list(str(n))
    if all(is_odd(int(num)) for num in n):
        return True
    return False

from time import time
count = 0
start = time()
for i in xrange(11, 10**9):
    k = str(i)
    j = k[::-1]
    if j[0] == '0':
        continue
    if check_num(i + int(j)):
        count += 1

print count, '<--count', time()-start, 'seconds'
