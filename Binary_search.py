__author__ = 'karnikamit'
import random
import time


def binary_search(item, a_list):
    start_time = time.time()
    a_list.sort()
    start, end = 0, len(a_list)-1
    found = False
    resp = {"response": "failure", "msg": "item not found"}
    while start <= end and not found:
        mid = (start + end) // 2
        if a_list[mid] > item:
            end = mid - 1
        elif a_list[mid] < item:
            start = mid + 1
        else:
            resp["response"] = "success"
            resp["msg"] = "item found at " + str(mid)
            resp["time taken"] = str(time.time()-start_time) + " seconds"
            return resp
    return resp

if __author__ == 'karnikamit':
    a = range(10**4)
    random.shuffle(a)
    print binary_search(99, a)
