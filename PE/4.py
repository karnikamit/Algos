#Largest palindrome product
import time
start = time.clock()
p = []
pal = []
for i in range(900, 1000):
    for j in range(900, 1000):
        p.append(str(i*j))
for i in p:
    j = len(i)
        
    if j%2 == 0:
        a = int(int(j)/2)
    else:
        a = int(int(j)/2)
    b = list(i[-a:])
    c = list(i[:a])
    c.reverse()
    if b == c:
        pal.append(i)
print (max(pal))
print('Runtime:', time.clock()-start,'sec')
