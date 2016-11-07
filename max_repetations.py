__author__ = 'karnikamit'

# TODO  optimize


def search_max_rep(array):
    temp = dict()
    for element in array:
        try:
            temp[element] += 1
        except KeyError:
            temp[element] = 1
    max_count = max(temp.values())
    items = [key for key in temp if temp[key] == max_count]
    return items
