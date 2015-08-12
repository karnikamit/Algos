import time
start_time = time.clock()
s = 0
for n1 in range(100000, 1000000):
    num = n1
    my_list = []
    while num > 1:
        if num % 2 == 0:
            num /= 2
            my_list.append(num)
        else:
            num = (3*num)+1
            my_list.append(num)
    s1 = len(my_list)
    if s1 > s:
        s = s1
        n2 = n1
                        
print ('Longest c_seq is given by:',  n2)
print (time.clock() - start_time, "seconds")
