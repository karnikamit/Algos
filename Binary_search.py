__author__ = 'karnikamit'


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
            resp['New_List'] = a_list
            resp["Msg"] = "item found at position " + str(position)
            return resp
        position += 1
    return resp

if __author__ == 'karnikamit':
    myList = range(10)
    item = 6
    search = binary_search(item, myList)
    if search["response"] == "success":
        print 'List ', search['New_List']
        print search['Msg']
    else:
        print 'item Not found'