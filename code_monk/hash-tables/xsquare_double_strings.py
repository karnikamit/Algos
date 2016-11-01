# -*- coding: utf-8 -*-
__author__ = 'karnikamit'

'''
https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/xsquare-and-double-strings-1/
'''
def is_double_string(s):
    """

    :param s: special string S consisting of lower case English letters.
    :return: Yes if string s can be converted to double string else No
    """
    string_list = list(s)
    string_length = len(string_list)
    if string_length >= 2:
        if string_length == 2:
            return 'Yes' if string_list[0] == string_list[1] else 'No'
        else:
            if not len(string_list) % 2:
                mid = string_length/2
                A = string_list[:mid]
                B = string_list[mid:]
                if A == B:
                    return 'Yes'
                else:
                    A = {k: v for k, v in enumerate(A)}
                    a = A.copy()
                    B = {k: v for k, v in enumerate(B)}
                    for key in a:
                        if A[key] != B[key]:
                            del A[key]
                            del B[key]
                    A = ''.join(A.values())
                    B = ''.join(B.values())
                    return 'Yes' if A == B else 'No'
            else:
                temp = {}
                {temp.setdefault(i, []).append(i) for i in string_list}
                res = filter(lambda x: len(temp[x]) % 2, temp)
                if res:
                    for i in res:
                        string_list.remove(i)
                new_string = ''.join(string_list)
        return is_double_string(new_string)
    return 'No'

cases = int(raw_input())
for _ in xrange(cases):
    print is_double_string(raw_input())
