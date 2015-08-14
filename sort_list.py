__author__ = 'karnikamit'
"""
code to sort a list of lists using particular index.
"""
import random
b = list()
for x in xrange(5):
    a = range(1, 5)
    random.shuffle(a)
    b.append(a)

def sort_list(a_list, index):
    new_list = []
    temp = [i[index] for i in a_list]
    temp.sort()
    for i in temp:
        for j in a_list:
            if j[index] == i:
                new_list.append(j)
                break
    return new_list

# compare
# print sorted(b, key=lambda x: x[2], reverse=False)
print sort_list(b, 2)