import time
start = time.time()
pow_sum=0
for i in range(1,1001):
    pow_sum += (i**i)
ans = str(pow_sum)
print (ans[-10:])
print (time.time()-start,'sec')
'''
one linear
print str(sum([x**x for x in range(1,1001)]))[-10:]
'''
