__author__ = 'karnikamit'
import time
import random


def linear_search(item, a_list):
    """

    :param item: item to search for
    :param a_list: list of items
    :return: the item with the given properties if present in the list
    """
    response = {"response": "failure", "Msg": "item Not found!"}
    position = 0
    flag = False
    while not flag and position < len(a_list):
        if item == a_list[position]:
            response["response"] = "success"
            response['Msg'] = "item found at index " + str(position)
        position += 1
    return response

if __author__ == 'karnikamit':
    start = time.time()
    my_list = range(10**7)
    random.shuffle(my_list)
    item_sought = 9999999
    print linear_search(item_sought, my_list)
    print 'time taken ' + str(time.time()-start)
