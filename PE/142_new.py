# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from is_square import is_square


def euler():
    for ai in xrange(5, 1000):
        for bi in xrange(1, ai):
            if ai % 2 != bi % 2:
                continue

            a = ai * ai
            b = bi * bi
            y = (a - b) / 2
            x = a - y

            if x < y:
                continue

            for ci in xrange(1, ai):
                c = ci * ci
                z = c - x
                if z > y or z <= 0:
                    continue
                elif not is_square(x - z):
                    continue
                elif not is_square(y + z):
                    continue
                elif not is_square(y - z):
                    continue
                else:
                    return x + y + z
    return 'Not Found!'

if __name__ == '__main__':
    print euler()

