__author__ = 'karnikamit'


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
    my_list = range(100)
    item = 10
    print linear_search(item, my_list)
