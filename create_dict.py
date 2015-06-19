__author__ = 'karnikamit'

a1 = [1, 2, 3, 4, 5]
b1 = ['a', 'b', 'c', 'd', 'e']


def create_dict(a, b):
    d = dict()
    if len(a)-len(b) != 0:
        for i in range(len(a)-len(b)):
            b.append(None)
    for j in range(len(a)):
        d[a[j]] = b[j]
    return d


def dict_create(keys, values):
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))
