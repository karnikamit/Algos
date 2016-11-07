# -*- coding: utf-8 -*-
__author__ = 'karnikamit'


def count_numbers(n, m):
    divs = []
    if n > 1:
        min_no, max_no = int('1'+'0'*(n-1)), int('1' + '0'*n)
    else:
        min_no, max_no = 1,  10
    for i in xrange(min_no, max_no):
        if i % m == 0:
            divs.append(i)
    else:
        return divs


def eliminations(x, pairs, divs):
    divs = map(str, divs)
    for i in xrange(x):
        a, b = pairs[i]
        p1 = '{}{}'.format(a, b)
        p2 = '{}{}'.format(b, a)
        divs = filter(lambda k: p1 not in k or p2 not in k, divs)
    else:
        return len(divs)


cases = int(raw_input())
for case in xrange(cases):
    N, M, X = map(int, (raw_input().split(' ')))
    pairs = [(1, 1)]
    for i in xrange(X):
        a, b = map(int, raw_input().split(' '))
        pairs.append((a, b))
    divs = count_numbers(N, M)
    print eliminations(X, pairs, divs) % (10**9 + 7)
