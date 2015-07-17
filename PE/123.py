__author__ = 'karnikamit'


def is_prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1

def get_prime(num):
    return [i for i in range(2, num**2) if is_prime(i)][num-1]

def form_primes(num):
    primes = []
    for i in xrange(2, num+1):
        if is_prime(i):
            primes.append(i)
    return primes

primes = form_primes(9999)

def get_prime_sq_remainders(n):
    global primes
    p = primes[n-1]
    print p, 'p'
    return ((p-1)**n + (p+1)**n)/(p**2)


for i in xrange(2, 10000):
    r = get_prime_sq_remainders(i)
    print 'r', r
    if r >= 1000000000:
        print i, 'here'
        exit(0)


# if is_prime(get_prime_sq_remainders(3)):
#     print 'yes!'
