__author__ = 'karnikamit'

'''
Given an array of file sizes, merge the files
'''
# Using recursion

def add_files(a_list):
    if len(a_list) > 1:
        a = a_list.pop(0)
        b = a_list.pop(0)
        a_list.insert(0, a+b)
        print a_list
    else:
        return a_list
    return add_files(a_list)


def merge_files(array):
    array.sort()
    return add_files(array)


f = [10, 5, 100, 50, 20, 15]
merge_files(f)
