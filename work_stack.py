__author__ = 'karnikamit'
import sys
from time import sleep


def stack():
    work = ['1. Add to Stack', '2. Pop from stack', '3. Print stack', '4. Exit']
    stack_list = list()
    flag = True
    while flag:
        for w in work:
            print w
        q = int(raw_input('What do you want to do? '))
        if q == 1:
            item = str(raw_input("Add "))
            stack_list.append(item)
        elif q == 2:
            stack_list.pop(stack_list.index(str(raw_input('item to pop- '))))
        elif q == 3:
            for i in stack_list:
                print i
        elif q == 4:
            dot = '...'
            for c in dot:
                print c,
                sys.stdout.flush()
                sleep(1)
            print 'Bye'
            flag = False
        else:
            print 'Asshole!'
            exit(0)
