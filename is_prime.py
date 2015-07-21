__author__ = 'karnikamit'
from math import sqrt

# def is_prime(n):
#     return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n > 1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
