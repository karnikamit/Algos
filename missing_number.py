# -*- coding: utf-8 -*-
__author__ = "karnikamit"
import collections

# This is algorithm is for sorted list only.
# ------------------------========----------


def find_missing_number(a_list, frequency):
    """

    :param a_list: list of numbers
    :return: missing number from the list
    """
    a_dict = dict()
    for i in xrange(len(a_list)):
        a_dict[i] = a_list[i]
    missing_number = None
    for key in a_dict:
        if key <= (len(a_list)-1) - 1:
            if a_dict[key+1] - a_dict[key] != frequency:
                missing_number = a_dict[key+1]-frequency
    return missing_number

if __name__ == '__main__':
    t = [0, 3, 6, 9, 12]
    t.sort()
    v = [x[0]-x[1] for x in zip(t[1:], t[:-1])]

    # get the frequency of items
    counter = collections.Counter(v)
    fq = max(counter.values())
    diff = None
    for key in counter:
        if counter[key] == fq:
            diff = key
    if not all(x == v[0] for x in v):       # check weather an item is missing
        print 'missing number: %d' % find_missing_number(t, diff)
    else:
        print 'No items are missing in %s' % t

