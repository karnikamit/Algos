__author__ = 'karnikamit'


def get_factors(n):
    return [i for i in xrange(1, n+1) if n % i == 0]