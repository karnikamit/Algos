# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def get_taps(n):
    """

    :param n: no of cards
    :return: min no of taps required to flip the cards.
    """
    taps = 0
    while n > 0:
        taps += 1
        n -= 3
    return taps

cases = int(raw_input())
for _ in xrange(cases):
    print get_taps(int(raw_input()))
