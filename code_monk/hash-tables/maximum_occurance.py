# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/maximum-occurrence-9/
'''


def get_min_char(rep_list):
    """

    :param rep_list: list of max repeated items
    :return: char having min ASCII value
    """
    min_ord = min(map(ord, rep_list))
    return chr(min_ord)


def max_repetitions(s):
    """

    :param s: String
    :return: max repetitions count
    """
    counter_dict = {}
    [counter_dict.setdefault(i, []).append(i) for i in s]
    key = max(counter_dict, key=lambda x: len(counter_dict[x]))
    max_length = len(counter_dict[key])
    max_count = filter(lambda x: len(counter_dict[x]) == max_length, counter_dict)
    char = get_min_char(max_count)
    return char, max_length

char, char_rep_count = max_repetitions('Pulkit is a dog!!!!!!!!!!!!')
print '{} {}'.format(char, char_rep_count)
