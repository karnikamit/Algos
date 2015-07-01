__author__ = 'karnikamit'
import random


def bubble_sort(my_list):
    flag = True
    while flag:
        flag = False
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                flag = True     # setting flag = true for more swaps
    return my_list

if __author__ == 'karnikamit':
    a = range(10)
    random.shuffle(a)
    print bubble_sort(a)
