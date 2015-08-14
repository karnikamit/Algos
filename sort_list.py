__author__ = 'karnikamit'
"""
code to sort a list of lists using particular index.
"""


def sort_list(a_list, index):
    new_list = []
    temp = [i[index] for i in a_list]
    temp.sort()
    for i in temp:
        for j in a_list:
            if j[index] == i:
                new_list.append(j)
                break
    return new_list
