# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
'''
Little monk loves good string. Good String is a string that only contains vowels
(a,e,i,o,u). Now, his teacher gave him a string S.
Little monk is wondering what is the length of the longest good string which is a substring of S.
'''


def find_good_substring(s):
    good_string = 'aeiou'
    g_string, ret_g_string = '', ''
    for i in xrange(len(s)):
        if s[i] in good_string:
            g_string += s[i]
        else:
            if len(g_string) > len(ret_g_string):
                ret_g_string = g_string
                g_string = ''
    return len(ret_g_string)

print find_good_substring('abaac')
