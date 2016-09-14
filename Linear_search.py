__author__ = 'karnikamit'
import time


def linear_search(item, a_list):
    """

    :param item: item to search for
    :param a_list: list of items
    :return: the item with the given properties if present in the list
    """
    response = {"response": "failure", "Msg": "item Not found!"}
    position = 0
    while position < len(a_list):
        if item == a_list[position]:
            response["response"] = "success"
            response['Msg'] = "item found at index {} ".format(position)
        position += 1
    return response
