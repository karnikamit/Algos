__author__ = 'karnikamit'


def is_power2(num):
    return num != 0 and (num & (num - 1)) == 0
