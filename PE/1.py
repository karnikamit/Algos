#import math
# print sum(i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)) #--> One Liner
'''n = 0
for i in range(1,1000):
    if not i % 5 or not i % 3:
        n = n + i
        print (n)'''
import time
start_time = time.clock()
i = 0
n = 0
p =0
k=0
while n <= 333:  #3*333= 999<1000
    p = p + 3*n
    n=n+1
    #print (p)
while i <= 199: #5*199=995<1000
    k = k  + 5*i
    i=i+1
    #print(k)
print(p+k,' - ans')
print(time.clock() - start_time,'Seconds')

'''
while n < 334:
    while i < 200:
        o = 5*i
        print(o)
    p = 3*n
    n = n + 1
    print(p)
'''
'''
while i < 200:
    o = 5*i
    i = i+1
    print(o)
print("the ans- ",p+o)
 '''   


    
    
    
