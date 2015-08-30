__author__ = 'karnikamit'
from is_prime import is_prime


def get_primes(n):
    primes = []
    for i in xrange(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def find_con_prime(n):
    low = 2
    num = 0
    for i in get_primes(n):
        num += i
        if is_prime(num):
            if num < n:
                low = num
    return low
# print find_con_prime(100)

def get_con_primes(n):
    con_primes = {}
    primes = get_primes(n)
    print primes
    for num in primes:
        print 'num', num
        new_num = 0
        new_list = []
        for k in xrange(2, num):
            new_num += k
            if new_num == num:
                pass        # working!
        # new_primes = primes[:primes.index(num)]
        # new_num = sum(new_primes)
        # if new_num > n:
        #     continue
        # if is_prime(new_num):
        #     con_primes[len(new_primes)] = new_num
    return con_primes

print get_con_primes(1000)