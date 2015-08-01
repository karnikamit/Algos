__author__ = 'karnikamit'
'''
Move spaces in a given string to the front
'''

def move(string):
    count = 0
    for character in string:
        if character == ' ':
            count += 1
            string = string.replace(" ", "")
    spaces = " "*count
    # This is done because 'str' object does not support item assignment
    temp_str = list(string)
    temp_str.insert(0, spaces)
    string = ''.join(temp_str)
    return string

s = "move these spaces to beginning"
print s
print move(s)