# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

vowels = set('aeiou')


def is_present(text):
    """
    Fn to check if all the vowels (eng lowercase are present in text
    :param text: set - string eng lowercase
    :return: YES if vowels(set) is present in b else NO
    """
    global vowels
    return 'YES' if vowels <= set(text) else 'NO'

N = raw_input()
ip_text = raw_input()
print is_present(ip_text)
