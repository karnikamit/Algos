# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    print gcd(10, 6)
