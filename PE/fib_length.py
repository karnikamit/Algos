import time
start = time.clock()
f = 0
s = 1
fib = 0
n = 0
a = []
digits = 1000
while len(a) < digits:
    n += 1
    a = []
    fib = f + s
    f = s
    s = fib
    a = list(map(int, str(fib)))
    #print (n,a)
	
print ('the', n,'th term has',digits,'digits')
print ('Runtime:', time.clock()-start,'secs')
	
