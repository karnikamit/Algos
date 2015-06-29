__author__ = 'karnikamit'


def linear_search(item, a_list):
    """

    :param item: item to search for
    :param a_list: list of items
    :return: the item with the given properties if present in the list
    """
    position = 0
    flag = False
    while not flag and position < len(a_list):
        if item == a_list[position]:
            return "Item found at index " + str(a_list.index(item))
        position += 1
    return "Item not found"
