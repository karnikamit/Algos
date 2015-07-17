import time
start = time.clock()
c = 0
for b in range(3,50000):
    a_sum = 0
    b_sum = list(map(int,str(b)))
    for i in b_sum:
        a = 1
        for j in range(1,i+1):
            a *= j
        a_sum += a    
    if a_sum == b:
        c += b   
print (c)
print ('Runtime:', time.clock()- start, 'sec')
