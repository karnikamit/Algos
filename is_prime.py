__author__ = 'karnikamit'


def is_prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1
