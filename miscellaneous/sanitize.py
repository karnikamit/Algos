__author__ = 'karnikamit'


def sanitize(function):
    def wrap_function(string):
        if " " in string:
            string = string.replace(" ", '')
        if '.' in string:
            string = string.replace('.', '')
        if ',' in string:
            string = string.replace(',', '')
        return function(string.lower())
    return wrap_function
