import time
start = time.clock()
'''
n = 0
first = 0
second = 1
fib = 0
s=0
a = ''
while len(a) < 1000:
    fib = first + second    #fib is an integer
    a = str (fib)   #converting fib to string
    first = second
    second = fib
    n += 1
print(n, '- first one to have 1000 digits')
'''

f = 0
s = 1
fib = 0
n = 0
a = ''
digits = 1000
while len(a) < digits:
    n += 1
    fib = f + s
    f = s
    s = fib
    a = str(fib)
    #print (n,a)
	
print ('the', n,'st/nd/rd/th term has',digits,'digits')

print ('Runtime:', time.clock()-start,'secs')
	
   
