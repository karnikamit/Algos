# -*- coding: utf-8 -*-
__author__ = "karnikamit"


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def euler(limit):
    p_s = set()
    limit_to = int(limit ** 0.5)
    for i in xrange(1, limit_to):
        num = i ** 2
        while num < limit:
            i += 1
            num += i ** 2
            if is_palindrome(num) and num < limit:
                p_s.add(num)
    return sum(p_s)

if __name__ == '__main__':
    print euler(10 ** 8)    # 2906969179
