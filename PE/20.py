import time
start_time = time.time()
num = 100
factorial = 1
for i in range(1,num + 1):
    factorial *=i
print(sum(map(int,str(factorial))))

print ('Runtime:',time.time()-start_time,'Seconds')
