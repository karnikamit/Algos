__author__ = 'karnikamit'


def is_odd(n):
    if n > 0:
        if n % 2 == 0:
            return False
        else:
            return True
    return False

# def get_num(n):
#     for i in xrange(11, n+1):
#         yield i
from time import time
count = 0
# i = get_num(10)
# for k in i:
#     print k
# exit(0)
start = time()
for i in xrange(11, 10**8):
    k = str(i)
    j = k[::-1]
    if j[0] == '0':
        continue
    check = list(str(i + int(j)))
    if all(is_odd(int(num)) for num in check):
        count += 1

print count, '<--count', time()-start, 'seconds'