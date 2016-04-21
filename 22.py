# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from PE_42 import get_words, get_word_value, clock


def get_name_scores(filename):
    words = get_words(filename)
    sorted_words = sorted(words, key=lambda x: x[0])
    total_score = 0
    for i, name in enumerate(sorted_words):
        value = get_word_value(name)
        total_score += value * i
    return total_score

if __name__ =='__main__':
    start = clock()
    print get_name_scores('p022_names.txt')  # 871198282
    print 'runTime:', clock()-start, 's'
