__author__ = 'karnikamit'
'''
get the first repeated character from the string
'''
def get_first(string):
    dic_string = dict()
    for cahr in string:
        if cahr in dic_string:
            return cahr
        else:
            dic_string[cahr] = 1
    return -1

# print get_first('hello my name is Amit')

'''
get the count of characters
'''

def get_count(string):
    dic_string = dict()
    if " " in string:
        string = string.replace(" ", "")
    for char in string.lower():
        if char in dic_string:
            dic_string[char] += 1
        else:
            dic_string[char] = 1
    return dic_string

# print get_count('hello my name is Amit')

'''
get max repeated character
'''


def get_max(string):
    count = get_count(string)
    max_count = 0
    for rep in count.values():
        if rep > 1:
            if rep > max_count:
                max_count = rep
    for key in count.keys():
        if count[key] == max_count:
            return key
    return -1

print get_max('name is Amit')