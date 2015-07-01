__author__ = 'karnikamit'


def partition(my_list, start, end):
    pivot = my_list[start]
    low = start+1
    high = end
    done = False
    while not done:
        while low <= high and my_list[low] <= pivot:
            low += 1
        while my_list[high] >= pivot and high >= low:
            high -= 1
        if high < low:
            done = True
        else:
            my_list[low], my_list[high] = my_list[high], my_list[low]
    my_list[start], my_list[high] = my_list[high], my_list[start]
    return high


def quicksort(my_list, start, end):
    if start < end:
        split = partition(my_list, start, end)
        quicksort(my_list, start, split-1)
        quicksort(my_list, split+1, end)
    return my_list


if __author__ == 'karnikamit':
    import random
    import time
    my_array = range(10**7)
    random.shuffle(my_array)
    start_time = time.time()
    print quicksort(my_array, 0, len(my_array)-1)
    print time.time()-start_time, " seconds"
