__author__ = 'karnikamit'


def is_palindrome(data):
    i = 0
    j = len(data)-1
    while data[i] == data[j] and i < j:
        print data[i], data[j]
        i += 1
        j -= 1
    if i < j:
        return False
    return True

print is_palindrome('helloolleh')