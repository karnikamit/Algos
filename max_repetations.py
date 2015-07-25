__author__ = 'karnikamit'


def search_max_rep(array):
    temp = dict()
    resp = {}
    count_max = 1
    for element in array:
        if element not in temp:
            temp[element] = 1
        else:
            temp[element] += 1
    for item in temp:
        if temp[item] > count_max:
            count_max = temp[item]
            resp["maxRepetedItem"] = item
            resp["No_of_rep"] = temp[item]
    return resp
