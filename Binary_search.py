__author__ = 'karnikamit'


def binary_search(a_list, item):
    """

    :param a_list: sorted list
    :param item: item to search for
    :return: position of the item if found, else -1
    """
    if len(a_list) > 1:
        mid = len(a_list)/2
        mid_item = a_list[mid]
        if item < mid_item:
            s_list = a_list[:mid]
        elif item > mid_item:
            s_list = a_list[mid:]
        else:
            return a_list[mid]
        return binary_search(s_list, item)
    else:
        return -1
