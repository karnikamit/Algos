__author__ = 'CYBORG'


def no_divisors(num):
    divisors = range(1, num+1)
    count = 0
    for i in divisors:
        if num % i == 0:
            count += 1
    if count == 8:
        return num


def count_no(num_range):
    items = 0
    i = 1
    while i <= num_range:
        if no_divisors(i) == i:
            items += 1
        i += 1
    return items

import time
start = time.time()
print(count_no(10**4), "time taken ", time.time()-start)
