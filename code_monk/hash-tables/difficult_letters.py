# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/difficult-characters/
'''
from string import ascii_lowercase as lower_case


def difficult_letters(s):
    """

    :param s: string (English lower letters)
    :return: most difficult letter to the less difficult letter.
    """
    # sort eng lower case letter in asc order using their ascii value
    chars = sorted(lower_case, key=lambda x: ord(x), reverse=True)
    [chars.remove(char) for char in s if char in chars]
    chars.extend(sanitize(s))
    return chars


def sanitize(s):
    temp = {}
    [temp.setdefault(i, []).append(i) for i in s]
    rep_dict = {}
    [rep_dict.setdefault(len(temp[k]), []).append(k) for k in temp]
    max_rep_count, min_rep_count = max(rep_dict), min(rep_dict)
    sanitized_list = []
    while min_rep_count <= max_rep_count:
        if rep_dict.get(min_rep_count):
            sort_list = sorted(rep_dict[min_rep_count], key=lambda x: ord(x), reverse=True)
            sanitized_list.extend(sort_list)
        min_rep_count += 1
    return sanitized_list

cases = int(raw_input())
for _ in xrange(cases):
    difficulties = difficult_letters(raw_input())
    for i in difficulties:
        print i,
    else:
        print
