__author__ = 'karnikamit'
import time


def binary_search(item, a_list):
    resp = {"response": "failure"}
    position = 0
    start = 0
    end = len(a_list) - 1
    mid_item = (start + end) // 2
    if a_list[mid_item] == item:
        resp["response"] = "success"
        resp["Msg"] = "item found at index " + str(mid_item)
        return resp
    elif a_list[mid_item] > item:
        end = mid_item
    else:
        start = mid_item + 1
    a_list = a_list[start:end + 1]
    while position < len(a_list):
        if a_list[position] == item:
            resp["response"] = "success"
            resp["Msg"] = "item found at position " + str(position)
            return resp
        position += 1
    return resp

if __author__ == 'karnikamit':
    start_time = time.time()
    myList = range(10**6)
    item_sought = 16024
    search = binary_search(item_sought, myList)
    if search["response"] == "success":
        print search['Msg']
    else:
        print 'item Not found'
    print 'time taken ' + str(time.time() - start_time)
