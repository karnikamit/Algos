import time
start_time = time.clock()
a, b = int(input('Range from- ')), int(input('Range to- '))
first = 0
second = 1
next1 = 0
even_sum = 2
c = []
for i  in range(a, b):
    next1 = first + second	
    first = second
    second = next1
    if (next1 % 2) == 0:
        even_sum += next1
        c.append(str(next1))
        #print (even_sum)
print(even_sum,' -Sum of even values.')
print(time.clock() - start_time,'Seconds')
	
        
    
