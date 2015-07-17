#Finding the smallest even
import time
start_time = time.clock()
i = 1
n = 1
while i in range(1, 21):
        if (n//i)%2!=0:
                n += 1
                #print('incmng N')
                i += 1
print(n,' This is it!')
print(time.clock()- start_time,'Seconds')
	
	
