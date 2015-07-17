import math
import time
start = time.clock()
'''
my_list = [6]
a = 2 ** 1000
i = 1
while i < 302:
    #global my_list
    b = ( a % (10 ** (i+1))// 10**i)
    my_list.append(b)
    i = i + 1
print (my_list)

digit_sum = 0
q = 0
while q < len(my_list):
    #global digit_sum, q
    digit_sum = digit_sum + my_list[q]
    q = q + 1
print("digit_sum: ", digit_sum)
'''
#one linear
print(sum(list(map(int, str(2**1000)))))

print ('Runtime:', time.clock()-start, 'Sec')
