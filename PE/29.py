import time
start_time = time.time()

a1 = set([])
for a in range(2, 101):
    for b in range(2, 101):
        c = a**b
        a1.add(c)
        
print (len(a1), 'sum of', a,' factorial/s')
'''
a = []
factorial = 1
for i in range(1, 101):
    factorial *= i
    a.append(factorial)
print (sum(a))
'''
print (time.time()-start_time,'Seconds')
