#abundant and non-abundant nos

import time
start = time.clock()
my_set = set([i for i in range(1, 20000)])
my_list = list(my_set)
my_l1 = set([])
for i in range(12, my_list[-1]):
    a = 0
    #checking for abundant nos    
    for j in range(1, int(i/2+1)):
        if i%j == 0:
            a += j
        if a > i:
            my_l1.add(i)
            b = i*2
            if b <= my_list[-1]:
                my_l1.add(i*2)
'''
l = 0
my_l2 = list(my_l1)
for d in my_l2:
    l += 1
    while l < len(my_l2):
        a_s = d + my_l2[l]
        my_l1.add(a_s)
'''                   
my_set.difference_update(my_l1)
print(sum(my_l1))
print (time.clock()-start, 'sec')

