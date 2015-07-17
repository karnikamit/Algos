#Powerful digit counts
import time
start = time.clock()
count  = 0
for i in range(1, 100):
    for x in range(1,100):
        if len(str(i**x)) == x:
            count += 1
print (count)
print('Runtime:', time.clock()- start, 'sec')
            
