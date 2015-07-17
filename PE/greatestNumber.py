# Greatest number
import time
start = time.clock()
my_array = []
n1 = 1
d1 = 0
N = input("Input the number- ")
b = int(N)
n = len(N)
a = int(n)
i = 0
while n > 0 :
    q = (b % (10 ** a) // (10**(a-1)))
    n = n - 1
    a = a - 1
    my_array.append(q)
    n1 = n1 * my_array[i]
    d1 = d1 + my_array[i]
    i = i + 1
print (n1)
print (d1)
print (time.clock() - start, 'sec')

