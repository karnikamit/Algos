# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


N, K = map(int, raw_input().split(' '))     # N K
A = map(int, raw_input().split(' '))        # Array


class VanyaArray(object):
    def __init__(self, a_list, n, k):
        assert n == len(a_list)
        self.array = a_list
        self.n = n
        self.k = k

    def val(self, i, j):
        return 1 if self.array[i] < self.array[j] else 0

    def f(self, i):
        total = 0
        while i < self.n-1:
            j = i + 1
            total += self.val(i, j)
            i += 1
        else:
            return total

    def final_result(self):
        pairs = []
        for i in xrange(len(self.array)-1):
            if self.f(i) + self.f(i+1) >= self.k:
                pairs.append((i, i+1))
        return pairs
