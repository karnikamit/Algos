# -*- coding: utf-8 -*-
__author__ = "karnikamit"
from time import clock


def get_word_value(word):
    alpa_num = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10,
                'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
                'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    value = 0
    for i in word:
        value += alpa_num[i]
    return value


def isqrt(n):
    x = n
    y = (x+1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def is_tri(n):
    s = isqrt(2*n)
    if s*(s+1) == 2*n:
        return True
    return False


def get_words(filename):
    file_open = open(filename)
    filewords = file_open.readlines()[0].replace('"', '').split(',')
    filewords = [i.lower() for i in filewords]
    file_open.close()
    return filewords

if __name__ == '__main__':
    start = clock()
    c = 0
    words = get_words('PE_42_words.txt')
    for w in words:
        v = get_word_value(w)
        if is_tri(v):
            c += 1
    print c, 'runtime:', clock()-start, 's'
