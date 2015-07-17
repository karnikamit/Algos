import time
start = time.clock()

'''
import math
n = 0
sums = 0
su = 0
a = 0
while n < 100:
    n += 1
    sums += n**2      # sum of the squares of the first one hundred natural numbers
    su += n
a= su**2            # square of the sum of the first one hundred natural numbers
#print (sums)
#print (a)
b = a - sums    #difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
print (b)
'''
a = 0
b = 0
for i in range(1, 101):
    a += i**2
    b += i
print ('ans: ', b**2 - a)
print ('Runtime:', time.clock()-start, 'secs')
