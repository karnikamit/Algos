__author__ = 'karnikamit'

a1 = [1, 2, 3, 4, 5]
b1 = ['a', 'b', 'c', 'd', 'e']


def create_dict(a, b):
    """

    :param a:
    :param b:
    :return:this function creates a dictionary from given two lists,
    it prepares a dict by considering the length of the lists.
    it prepares the dict only to the items present in the 1st list 'a'.
    If length of list 'b' is less than the length of list 'a',
    then it appends 'None' to 'b' to make its length equal to the length of list 'a'.

    """
    d = dict()
    if len(a)-len(b) != 0:
        for i in range(len(a)-len(b)):
            b.append(None)
    for j in range(len(a)):
        d[a[j]] = b[j]
    return d


def dict_create(keys, values):
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))
